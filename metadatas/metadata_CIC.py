# .csv files
# mixed classes 
# only one folder
# dropped all rows containing nan value in label

import re

column_index = 46

iot23_metadata = {
    "file_name_pattern": "/**/*.csv",
    "file_header": "",
    "all_columns": ['flow_duration', 'Header_Length', 'Protocol Type', 'Duration', 
                    'Rate', 'Srate', 'Drate', 'fin_flag_number', 'syn_flag_number', 
                    'rst_flag_number', 'psh_flag_number', 'ack_flag_number', 
                    'ece_flag_number', 'cwr_flag_number', 'ack_count', 'syn_count', 
                    'fin_count', 'urg_count', 'rst_count', 'HTTP', 'HTTPS', 'DNS', 
                    'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 
                    'ICMP', 'IPv', 'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 
                    'Tot size', 'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                    'Variance', 'Weight', 'label'],

    "numeric_columns": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight'],

}

data_cleanup = {
    "classification_col": "label",
    "drop_cols": ['label'],
    "replace_values": {},
    "replace_values_in_col": {},
    "transform_to_numeric": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight'], 
    "class_labels": {
        0: 'DDoS-TCP_Flood', 
        1: 'DoS-UDP_Flood', 2: 'DDoS-ICMP_Fragmentation', 3: 'DDoS-RSTFINFlood', 
        4: 'BenignTraffic', 5: 'DDoS-SynonymousIP_Flood', 6: 'DDoS-UDP_Flood', 
        7: 'DDoS-ICMP_Flood', 8: 'DoS-TCP_Flood', 9: 'DDoS-PSHACK_Flood', 
        10: 'DDoS-SYN_Flood', 11: 'DoS-SYN_Flood', 12: 'MITM-ArpSpoofing', 
        13: 'DDoS-SlowLoris', 14: 'Mirai-greeth_flood', 15: 'Mirai-udpplain', 
        16: 'Recon-PortScan', 17: 'DDoS-UDP_Fragmentation', 18: 'Mirai-greip_flood', 
        19: 'DDoS-ACK_Fragmentation', 20: 'Recon-HostDiscovery', 21: 'Recon-PingSweep', 
        22: 'DNS_Spoofing', 23: 'DoS-HTTP_Flood', 24: 'SqlInjection', 25: 'DictionaryBruteForce', 
        26: 'Backdoor_Malware', 27: 'Recon-OSScan', 28: 'DDoS-HTTP_Flood', 29: 'VulnerabilityScan', 
        30: 'BrowserHijacking', 31: 'CommandInjection', 32: 'XSS', 33: 'Uploading_Attack'

    },
    "category_encodings": {
        "label": {
            'DDoS-TCP_Flood': 1, 'DoS-UDP_Flood': 1, 'DDoS-ICMP_Fragmentation': 1, 
            'DDoS-RSTFINFlood': 1, 'BenignTraffic': 0, 'DDoS-SynonymousIP_Flood': 1, 
            'DDoS-UDP_Flood': 1, 'DDoS-ICMP_Flood': 1, 'DoS-TCP_Flood': 1, 
            'DDoS-PSHACK_Flood': 1, 'DDoS-SYN_Flood': 1, 'DoS-SYN_Flood': 1, 
            'MITM-ArpSpoofing': 1, 'DDoS-SlowLoris': 1, 'Mirai-greeth_flood': 1, 
            'Mirai-udpplain': 1, 'Recon-PortScan': 1, 'DDoS-UDP_Fragmentation': 1, 
            'Mirai-greip_flood': 1, 'DDoS-ACK_Fragmentation': 1, 
            'Recon-HostDiscovery': 1, 'Recon-PingSweep': 1, 'DNS_Spoofing': 1, 
            'DoS-HTTP_Flood': 1, 'SqlInjection': 1, 'DictionaryBruteForce': 1, 
            'Backdoor_Malware': 1, 'Recon-OSScan': 1, 'DDoS-HTTP_Flood': 1, 
            'VulnerabilityScan': 1, 'BrowserHijacking': 1, 'CommandInjection': 1, 
            'XSS': 1, 'Uploading_Attack': 1,
        },
    },
}

feature_selections = {
    # EXP_FL16_FT14_R_ / EXP_FL4_FT14_R_
    # All without:
    # 'label'
    "F14": {
        "description": 'F14',
        "features": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight']
        },

    # EXP_FL16_FT17_R_ / EXP_FL4_FT17_R_
    # All without:
    # 'label'
    "F17": {
        "description": 'F17',
        "features": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight']
        },

    # EXP_FL16_FT18_R_ / EXP_FL4_FT18_R_
    # All without:
    # 'label'
    "F18": {
        "description": 'F18',
        "features": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight']
        },

    # All without:
    # 'label'
    "F19": {
        "description": 'F19',
        "features": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight']
        },
}

datasets = {
    'S16': [],
    'S04': [
        "SqlInjection.csv",
        "DictionaryBruteForce.csv",
        "BenignTraffic.csv",
        "XSS.csv",
    ]
}


def get_data_sample(dataset_name='S04', rows_per_dataset_file=100_000):
    sample_name = dataset_name + ('_R_' + str(format(rows_per_dataset_file, '_d')))
    return {
        "description": sample_name,
        "files": datasets[dataset_name],  # empty => combine all source files
        "max_rows_per_file": rows_per_dataset_file,
        "combined_data_file_name": sample_name + '.csv',
        "clean_data_file_name": sample_name + '_clean.csv'}


def get_feature_selection(experiment_name):
    features_code = experiment_name.split("_", 1)[0]
    return feature_selections[features_code]['features']


def get_train_data_path(file_path):
    return file_path + '_train.csv'


def get_test_data_path(file_path):
    return file_path + '_test.csv'


def format_line(line, new_sep=','):
    line = __replace_whitespaces(line, replace_with=new_sep)
    line = line.rstrip(new_sep) + '\n'
    return line


def __replace_whitespaces(s, replace_with=','):
    return re.sub(r"\s+", replace_with, s)


def get_exp_data_dir(exp_name):
    return exp_name + "//data//"


def get_exp_models_dir(exp_name):
    return exp_name + "//models//"


def get_exp_results_dir(exp_name):
    return exp_name + "//results//"


def get_exp_name(data_combination, feature_selection_name):
    return feature_selection_name + '_' + data_combination['description']


def get_feat_selection_name(experiment_name):
    return experiment_name.split("_S", 1)[0]


def get_data_sample_name(experiment_name):
    return experiment_name.split("_", 1)[1]


def get_data_sample_name_short(experiment_name):
    return experiment_name.split("_")[1]


def get_sample_row_count(experiment_name):
    return float(experiment_name.split("R_", 1)[1])


def decode_labels(keys):
    class_labels = data_cleanup['class_labels']
    labels = [class_labels[key] for key in keys]
    return labels


def decode_cls_label(key):
    return data_cleanup['class_labels'][key]