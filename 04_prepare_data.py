import logging

from config import attacks_dir, data_dir
from src.metadata import data_metadata, data_cleanup, get_data_sample
from src.helpers.log_helper import add_logger
from src.helpers.data_helper import prepare_data

# Add Logger
add_logger(file_name='04_prepare_data.log')

# Prepare data
source_files_dir = attacks_dir
output_files_dir = data_dir

data_samples = [
    get_data_sample(dataset_name='S04', rows_per_dataset_file=10_000),  
    #get_data_sample(dataset_name='S16', rows_per_dataset_file=5_000_000),  
]
prepare_data(source_files_dir,
             output_files_dir,
             data_metadata["file_header"],
             data_cleanup,
             test_size=0.2,
             data_samples=data_samples,
             overwrite=True)

print('Step 04: The end.')
quit()
