from src.helpers.scenario_helper import split_scenarios_by_label
from src.helpers.file_helper import delete_dir_content
from src.helpers.shuffle_content_helper import shuffle_files_content
from src.helpers.config_helper import check_config
from src.metadata import data_metadata
from config import attacks_dir, data_dir, experiments_dir, scenarios_dir

# Run step1_configuration_check.py
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

# Run step2_extract_data_from_scenarios.py
output_dir = attacks_dir
delete_dir_content(output_dir)

# Split scenarios
source_dir = scenarios_dir
file_name_pattern = data_metadata['file_name_pattern']
header_line = data_metadata['file_header']
split_scenarios_by_label(source_dir,
                         file_name_pattern,
                         output_dir,
                         header_line)


# Run step3_shuffle_file_content.py
source_files_dir = attacks_dir
source_files_pattern = source_files_dir + "*.csv"

shuffle_files_content(source_files_pattern)