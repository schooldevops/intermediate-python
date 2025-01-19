import dask.dataframe as dd
import dask.array as da
from dask.distributed import Client
import logging
from typing import List, Tuple

class DistributedProcessor:
    def __init__(self, cluster_config: dict):
        self.cluster_config = cluster_config
        self.setup_logging()
        self.client = None

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def connect_cluster(self):
        """Dask 클러스터 연결"""
        try:
            self.client = Client(self.cluster_config['scheduler_address'])
            logging.info(f"Connected to Dask cluster: {self.client.dashboard_link}")
        except Exception as e:
            logging.error(f"Failed to connect to cluster: {str(e)}")
            raise

    def process_data(self, data_files: List[str]) -> Tuple[dd.DataFrame, dict]:
        """분산 데이터 처리"""
        try:
            # 데이터 로드
            df = dd.read_csv(data_files)
            
            # 계산 수행
            results = {
                'mean': df.mean().compute(),
                'sum': df.sum().compute(),
                'count': len(df.compute())
            }
            
            return df, results
        except Exception as e:
            logging.error(f"Data processing failed: {str(e)}")
            raise

    def run_analysis(self, data_files: List[str]):
        """분산 분석 실행"""
        try:
            self.connect_cluster()
            df, results = self.process_data(data_files)
            
            logging.info("Analysis completed successfully")
            logging.info(f"Results: {results}")
            
            return results
        except Exception as e:
            logging.error(f"Analysis failed: {str(e)}")
            raise
        finally:
            if self.client:
                self.client.close()

if __name__ == "__main__":
    cluster_config = {
        'scheduler_address': 'localhost:8786'
    }
    
    data_files = ['data/*.csv']
    processor = DistributedProcessor(cluster_config)
    processor.run_analysis(data_files)