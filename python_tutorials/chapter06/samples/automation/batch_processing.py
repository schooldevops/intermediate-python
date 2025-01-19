from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging
from datetime import datetime
from typing import Dict, List, Callable
import time

class BatchJob:
    def __init__(self, name: str, func: Callable, retry_count: int = 3):
        self.name = name
        self.func = func
        self.retry_count = retry_count
        self.last_run = None
        self.last_status = None
        self.error_count = 0

    def execute(self):
        """작업 실행"""
        self.last_run = datetime.now()
        try:
            result = self.func()
            self.last_status = 'success'
            self.error_count = 0
            return result
        except Exception as e:
            self.last_status = 'failed'
            self.error_count += 1
            raise

class BatchProcessor:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.jobs: Dict[str, BatchJob] = {}
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='batch_processor.log'
        )

    def add_job(self, name: str, func: Callable, schedule: str, retry_count: int = 3):
        """작업 추가"""
        job = BatchJob(name, func, retry_count)
        self.jobs[name] = job
        
        def job_wrapper():
            try:
                logging.info(f"Starting job: {name}")
                job.execute()
                logging.info(f"Job completed successfully: {name}")
            except Exception as e:
                logging.error(f"Job failed: {name}, Error: {str(e)}")
                if job.error_count < job.retry_count:
                    logging.info(f"Retrying job: {name}")
                    time.sleep(60)  # 1분 후 재시도
                    job_wrapper()

        self.scheduler.add_job(
            job_wrapper,
            trigger=CronTrigger.from_crontab(schedule),
            id=name
        )

    def start(self):
        """배치 처리 시작"""
        try:
            self.scheduler.start()
            logging.info("Batch processor started")
        except Exception as e:
            logging.error(f"Failed to start batch processor: {str(e)}")
            raise

    def stop(self):
        """배치 처리 중지"""
        self.scheduler.shutdown()
        logging.info("Batch processor stopped")

    def get_job_status(self) -> List[Dict]:
        """작업 상태 조회"""
        return [{
            'name': name,
            'last_run': job.last_run,
            'last_status': job.last_status,
            'error_count': job.error_count
        } for name, job in self.jobs.items()]

if __name__ == "__main__":
    def sample_job():
        print(f"Running sample job at {datetime.now()}")

    processor = BatchProcessor()
    processor.add_job(
        name="sample_job",
        func=sample_job,
        schedule="*/5 * * * *"  # 5분마다 실행
    )
    
    try:
        processor.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        processor.stop()