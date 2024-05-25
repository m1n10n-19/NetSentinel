import logging

from numpy import sort

from config import experiments_dir
from src.helpers.file_helper import list_folder_names
from src.helpers.log_helper import add_logger
from src.helpers.report_helper import combine_reports

add_logger(file_name='08_combine_results.log')

# Combine reports
exp_dir = experiments_dir
exp_list_all = sort(list_folder_names(exp_dir))
combine_reports(exp_dir, exp_list_all, 'S04_S16_all_scores.xlsx')

print('Step 08: The end.')
quit()
