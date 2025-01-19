import psutil
import time
import logging
from typing import Dict, List
from datetime import datetime
import smtplib
from email.message import EmailMessage

class SystemMonitor:
    def __init__(self, config: Dict):
        self.config = config
        self.setup_logging()
        self.thresholds = config.get('thresholds', {})
        self.alert_history = []

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename='system_monitor.log'
        )

    def get_system_metrics(self) -> Dict:
        """시스템 메트릭 수집"""
        return {
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_percent': psutil.disk_usage('/').percent,
            'timestamp': datetime.now().isoformat()
        }

    def check_thresholds(self, metrics: Dict) -> List[str]:
        """임계값 확인"""
        alerts = []
        if metrics['cpu_percent'] > self.thresholds.get('cpu_percent', 90):
            alerts.append(f"CPU 사용률이 {metrics['cpu_percent']}%로 임계값을 초과했습니다.")
        if metrics['memory_percent'] > self.thresholds.get('memory_percent', 90):
            alerts.append(f"메모리 사용률이 {metrics['memory_percent']}%로 임계값을 초과했습니다.")
        if metrics['disk_percent'] > self.thresholds.get('disk_percent', 90):
            alerts.append(f"디스크 사용률이 {metrics['disk_percent']}%로 임계값을 초과했습니다.")
        return alerts

    def send_alert(self, message: str):
        """알림 전송"""
        try:
            email_msg = EmailMessage()
            email_msg.set_content(message)
            email_msg['Subject'] = 'System Alert'
            email_msg['From'] = self.config['email']['from']
            email_msg['To'] = self.config['email']['to']

            with smtplib.SMTP(self.config['email']['smtp_server']) as server:
                server.send_message(email_msg)
            
            logging.info(f"Alert sent: {message}")
        except Exception as e:
            logging.error(f"Failed to send alert: {str(e)}")

    def run(self):
        """모니터링 시작"""
        logging.info("Starting system monitoring...")
        try:
            while True:
                metrics = self.get_system_metrics()
                alerts = self.check_thresholds(metrics)
                
                for alert in alerts:
                    self.send_alert(alert)
                    self.alert_history.append({
                        'timestamp': datetime.now().isoformat(),
                        'message': alert
                    })

                time.sleep(self.config.get('interval', 60))
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user")
        except Exception as e:
            logging.error(f"Monitoring failed: {str(e)}")

if __name__ == "__main__":
    config = {
        'thresholds': {
            'cpu_percent': 80,
            'memory_percent': 80,
            'disk_percent': 80
        },
        'interval': 60,
        'email': {
            'smtp_server': 'smtp.gmail.com',
            'from': 'monitor@example.com',
            'to': 'admin@example.com'
        }
    }
    
    monitor = SystemMonitor(config)
    monitor.run()