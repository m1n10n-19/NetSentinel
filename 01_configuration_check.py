from config import scenarios_dir, attacks_dir, experiments_dir, data_dir
from src.metadata import data_metadata
from src.helpers.config_helper import check_config
from src.helpers.log_helper import add_logger

# Add Logger
add_logger(file_name='01_config_check.log')

# Check Config
scenarios_location = scenarios_dir
file_name_pattern = data_metadata['file_name_pattern']
attack_files_location = attacks_dir
data_dir = data_dir
experiments_location = experiments_dir
check_config(scenarios_location,
             file_name_pattern,
             attack_files_location,
             data_dir,
             experiments_location)

print('Step 01: The End')
quit()
