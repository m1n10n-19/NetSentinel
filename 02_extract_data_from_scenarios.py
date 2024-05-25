import logging

from config import attacks_dir, scenarios_dir
from src.metadata import data_metadata
from src.helpers.file_helper import delete_dir_content
from src.helpers.log_helper import add_logger
from src.helpers.scenario_helper import split_scenarios_by_label

# Add Logger
add_logger(file_name='02_extract_data.log')

# Delete existing files in target dir
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

print('Step 02: The End')
quit()
