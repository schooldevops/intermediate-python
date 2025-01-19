from kafka import KafkaConsumer, KafkaProducer
import json
from datetime import datetime
from typing import Dict, Any
import logging

class StreamProcessor:
    def __init__(self, kafka_config: Dict[str, Any]):
        self.kafka_config = kafka_config
        self.setup_logging()
        self.setup_kafka()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def setup_kafka(self):
        self.consumer = KafkaConsumer(
            self.kafka_config['input_topic'],
            bootstrap_servers=self.kafka_config['bootstrap_servers'],
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )

        self.producer = KafkaProducer(
            bootstrap_servers=self.kafka_config['bootstrap_servers'],
            value_serializer=lambda x: json.dumps(x).encode('utf-8')
        )

    def process_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        """메시지 처리 로직"""
        processed_message = {
            'timestamp': datetime.now().isoformat(),
            'original_data': message,
            'processed_value': message.get('value', 0) * 2,
            'status': 'processed'
        }
        return processed_message

    def run(self):
        """스트림 처리 시작"""
        logging.info("Starting stream processing...")
        try:
            for message in self.consumer:
                try:
                    processed_data = self.process_message(message.value)
                    self.producer.send(
                        self.kafka_config['output_topic'],
                        value=processed_data
                    )
                    logging.info(f"Processed message: {processed_data}")
                except Exception as e:
                    logging.error(f"Error processing message: {str(e)}")
        except Exception as e:
            logging.error(f"Stream processing failed: {str(e)}")
        finally:
            self.consumer.close()
            self.producer.close()

if __name__ == "__main__":
    kafka_config = {
        'bootstrap_servers': ['localhost:9092'],
        'input_topic': 'raw_data',
        'output_topic': 'processed_data'
    }
    
    processor = StreamProcessor(kafka_config)
    processor.run()