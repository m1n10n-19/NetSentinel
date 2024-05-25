import logging

from src.helpers.log_helper import add_logger
from src.helpers.shuffle_content_helper import shuffle_files_content
from config import attacks_dir

# Add Logger
add_logger(file_name='03_shuffle_data.log')

source_files_dir = attacks_dir
source_files_pattern = source_files_dir + "*.csv"

shuffle_files_content(source_files_pattern)

print('Step 03: The end')
quit()
