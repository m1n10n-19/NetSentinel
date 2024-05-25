import logging
import warnings
import sklearn

from config import experiments_dir, data_dir
from src.metadata import feature_selections, get_data_sample
from src.helpers.log_helper import add_logger
from src.helpers.model_stats_helper import export_model_stats

# Setup warnings
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)
warnings.filterwarnings("ignore", category=sklearn.exceptions.ConvergenceWarning)

add_logger(file_name='07_explore_exp_results.log')

# Setup warnings
warnings.filterwarnings("ignore", category=sklearn.exceptions.UndefinedMetricWarning)
warnings.filterwarnings("ignore", category=sklearn.exceptions.ConvergenceWarning)
#np.seterr(divide='ignore', invalid='ignore')

# Explore data
data_dir = data_dir
exp_home_dir = experiments_dir
data_samples = [
    get_data_sample(dataset_name='S04', rows_per_dataset_file=10_000),
    #get_data_sample(dataset_name='S16', rows_per_dataset_file=5_000_000),
]

# Selected Features
feature_selections = [
    feature_selections['F14'],
    #feature_selections['F17'],
    #feature_selections['F18'],
    #feature_selections['F19'],
]

export_model_stats(data_dir,
                   exp_home_dir,
                   data_samples,
                   feature_selections,
                   enable_score_tables=True,
                   enable_score_charts=True,
                   enable_model_insights=False)

print('Step 07: The end.')
quit()
