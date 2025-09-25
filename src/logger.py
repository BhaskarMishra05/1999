import sys
import logging
import os
from datetime import datetime

file_name = f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.LOG'
file_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(file_path, exist_ok=True)
end_path = os.path.join(file_path, file_name)

logging.basicConfig(
    filename=end_path,
    format="[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s",
    level=logging.DEBUG
)