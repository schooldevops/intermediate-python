import pandas as pd
from sqlalchemy import create_engine
import logging
from typing import Dict, List

class ETLPipeline:
    def __init__(self, source_config: Dict, target_config: Dict):
        self.source_config = source_config
        self.target_config = target_config
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def extract(self) -> pd.DataFrame:
        """데이터 소스에서 데이터 추출"""
        logging.info("Extracting data from source")
        try:
            df = pd.read_csv(self.source_config['file_path'])
            return df
        except Exception as e:
            logging.error(f"Extraction failed: {str(e)}")
            raise

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """데이터 변환 및 정제"""
        logging.info("Transforming data")
        try:
            # 결측치 처리
            df = df.fillna(0)
            # 데이터 타입 변환
            df['date'] = pd.to_datetime(df['date'])
            # 중복 제거
            df = df.drop_duplicates()
            return df
        except Exception as e:
            logging.error(f"Transformation failed: {str(e)}")
            raise

    def load(self, df: pd.DataFrame):
        """변환된 데이터를 대상 시스템에 적재"""
        logging.info("Loading data to target system")
        try:
            engine = create_engine(self.target_config['db_url'])
            df.to_sql(
                name=self.target_config['table_name'],
                con=engine,
                if_exists='append',
                index=False
            )
        except Exception as e:
            logging.error(f"Loading failed: {str(e)}")
            raise

    def run(self):
        """ETL 파이프라인 실행"""
        try:
            df = self.extract()
            transformed_df = self.transform(df)
            self.load(transformed_df)
            logging.info("ETL process completed successfully")
        except Exception as e:
            logging.error(f"ETL process failed: {str(e)}")
            raise

if __name__ == "__main__":
    source_config = {
        'file_path': 'data/source.csv'
    }
    target_config = {
        'db_url': 'postgresql://user:password@localhost:5432/db',
        'table_name': 'processed_data'
    }
    
    pipeline = ETLPipeline(source_config, target_config)
    pipeline.run()