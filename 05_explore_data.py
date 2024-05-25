import logging
from config import data_dir
from src.metadata import get_data_sample
from src.helpers.data_stats_helper import explore_data
from src.helpers.log_helper import add_logger

# Add Logger
add_logger(file_name='05_explore_data.log')

# Selected Data Files
data_file_dir = data_dir
data_samples = [
    get_data_sample(dataset_name='S04', rows_per_dataset_file=10_000),
    #get_data_sample(dataset_name='S16', rows_per_dataset_file=5_000_000),
]
explore_data(data_file_dir,
             data_samples=data_samples,
             explore_data_sample=True,
             explore_split_data=True,
             plot_corr=True,
             plot_cls_dist=True,
             plot_attr_dist=True)

print('Step 05: The end.')
quit()
