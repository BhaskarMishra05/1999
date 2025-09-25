from src.components.data_ingestion import DATA_INGESTION

data_ingestion_obj = DATA_INGESTION()
train_path, test_path = data_ingestion_obj.data_ingestion()