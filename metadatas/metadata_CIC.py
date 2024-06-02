#CIC

import re


data_metadata = {
    "file_name_pattern":"*.csv",
    "file_header": "flow_duration,Header_Length,Protocol Type,Duration,Rate,Srate,"
                    "Drate,fin_flag_number,syn_flag_number,rst_flag_number,psh_flag_number,"
                    "ack_flag_number,ece_flag_number,cwr_flag_number,ack_count,syn_count,"
                    "fin_count,urg_count,rst_count,HTTP,HTTPS,DNS,Telnet,SMTP,SSH,IRC,"
                    "TCP,UDP,DHCP,ARP,ICMP,IPv,LLC,Tot sum,Min,Max,AVG,Std,Tot size,"
                    "IAT,Number,Magnitue,Radius,Covariance,Variance,Weight,label,Binary_label",
    "all_columns": ['flow_duration', 'Header_Length', 'Protocol Type', 'Duration', 
                    'Rate', 'Srate', 'Drate', 'fin_flag_number', 'syn_flag_number', 
                    'rst_flag_number', 'psh_flag_number', 'ack_flag_number', 
                    'ece_flag_number', 'cwr_flag_number', 'ack_count', 'syn_count', 
                    'fin_count', 'urg_count', 'rst_count', 'HTTP', 'HTTPS', 'DNS', 
                    'Telnet', 'SMTP', 'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 
                    'ICMP', 'IPv', 'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 
                    'Tot size', 'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                    'Variance', 'Weight', 'label', 'Binary_label'],

    "numeric_columns": ['flow_duration', 'Header_Length', 'Protocol Type', 
                        'Duration', 'Rate', 'Srate', 'Drate', 'fin_flag_number', 
                        'syn_flag_number', 'rst_flag_number', 'psh_flag_number', 
                        'ack_flag_number', 'ece_flag_number', 'cwr_flag_number', 
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count', 'HTTP', 'HTTPS', 'DNS', 'Telnet', 'SMTP', 
                        'SSH', 'IRC', 'TCP', 'UDP', 'DHCP', 'ARP', 'ICMP', 'IPv', 
                        'LLC', 'Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight', 'Binary_label'],
    "column_index": 46, #column index of label
    "sep": ',', #seperater for csv
}

data_cleanup = {
    "classification_col": "label",
    "drop_cols": ['Binary_label'],
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
                        'Variance', 'Weight', 'Binary_label'], 
    "class_labels": {
        4: 'DDoS-TCP_Flood', 
        1: 'DoS-UDP_Flood', 2: 'DDoS-ICMP_Fragmentation', 3: 'DDoS-RSTFINFlood', 
        0: 'BenignTraffic', 5: 'DDoS-SynonymousIP_Flood', 6: 'DDoS-UDP_Flood', 
        7: 'DDoS-ICMP_Flood', 8: 'DoS-TCP_Flood', 9: 'DDoS-PSHACK_Flood', 
        10: 'DDoS-SYN_Flood', 11: 'DoS-SYN_Flood', 12: 'MITM-ArpSpoofing', 
        13: 'DDoS-SlowLoris', 14: 'Mirai-greeth_flood', 15: 'Mirai-udpplain', 
        16: 'Recon-PortScan', 17: 'DDoS-UDP_Fragmentation', 18: 'Mirai-greip_flood', 
        19: 'DDoS-ACK_Fragmentation', 20: 'Recon-HostDiscovery', 21: 'Recon-PingSweep', 
        22: 'DNS_Spoofing', 23: 'DoS-HTTP_Flood', 24: 'SqlInjection', 25: 'DictionaryBruteForce', 
        26: 'Backdoor_Malware', 27: 'Recon-OSScan', 28: 'DDoS-HTTP_Flood', 29: 'VulnerabilityScan', 
        30: 'BrowserHijacking', 31: 'CommandInjection', 32: 'XSS', 33: 'Uploading_Attack',

    },
    "category_encodings": {
        "label": {
            'DDoS-TCP_Flood': 4, 'DoS-UDP_Flood': 1, 'DDoS-ICMP_Fragmentation': 2, 
            'DDoS-RSTFINFlood': 3, 'BenignTraffic': 0, 'DDoS-SynonymousIP_Flood': 5, 
            'DDoS-UDP_Flood': 6, 'DDoS-ICMP_Flood': 7, 'DoS-TCP_Flood': 8, 
            'DDoS-PSHACK_Flood': 9, 'DDoS-SYN_Flood': 10, 'DoS-SYN_Flood': 11, 
            'MITM-ArpSpoofing': 12, 'DDoS-SlowLoris': 13, 'Mirai-greeth_flood': 14, 
            'Mirai-udpplain': 15, 'Recon-PortScan': 16, 'DDoS-UDP_Fragmentation': 17, 
            'Mirai-greip_flood': 18, 'DDoS-ACK_Fragmentation': 19, 
            'Recon-HostDiscovery': 20, 'Recon-PingSweep': 21, 'DNS_Spoofing': 22, 
            'DoS-HTTP_Flood': 23, 'SqlInjection': 24, 'DictionaryBruteForce': 25, 
            'Backdoor_Malware': 26, 'Recon-OSScan': 27, 'DDoS-HTTP_Flood': 28, 
            'VulnerabilityScan': 29, 'BrowserHijacking': 30, 'CommandInjection': 31, 
            'XSS': 32, 'Uploading_Attack': 33,
        },
    },
}

feature_selections = {
    # EXP_FL16_FT14_R_ / EXP_FL4_FT14_R_
    # All without:
    # 'label'
    "F14": {
        "description": 'F14',
        "features": ['flow_duration', 'Header_Length', 
                        'Duration', 'Rate', 'Srate', 'Drate',
                        'ack_count', 'syn_count', 'fin_count', 'urg_count', 
                        'rst_count','Tot sum', 'Min', 'Max', 'AVG', 'Std', 'Tot size', 
                        'IAT', 'Number', 'Magnitue', 'Radius', 'Covariance', 
                        'Variance', 'Weight',
                        ]
        },

    # EXP_FL16_FT17_R_ / EXP_FL4_FT17_R_
    # All without:
    # 'label'
    "F17": {
        "description": 'F17',
        "features": []
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
        "DDoS-ICMP_Flood.csv",
        "DDoS-TCP_Flood.csv",
        "BenignTraffic.csv",
        "DoS-UDP_Flood.csv",
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
    if new_sep != data_metadata['sep']:
        line = __replace_old_sep(line, replace_with=new_sep)
    line = line.rstrip(new_sep) + '\n'
    return line


def __replace_old_sep(s, replace_with=','):
    return re.sub(data_metadata['sep'], replace_with, s)


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