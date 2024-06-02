#DDoS_Botnet

import re


data_metadata = {
    "file_name_pattern": "*.csv",
    "file_header": "pkSeqID,stime,flgs,flgs_number,proto,proto_number,saddr,sport,"
                    "daddr,dport,pkts,bytes,state,state_number,ltime,seq,dur,mean,"
                    "stddev,sum,min,max,spkts,dpkts,sbytes,dbytes,rate,srate,drate,"
                    "TnBPSrcIP,TnBPDstIP,TnP_PSrcIP,TnP_PDstIP,TnP_PerProto,"
                    "TnP_Per_Dport,AR_P_Proto_P_SrcIP,AR_P_Proto_P_DstIP,"
                    "N_IN_Conn_P_DstIP,N_IN_Conn_P_SrcIP,AR_P_Proto_P_Sport,"
                    "AR_P_Proto_P_Dport,Pkts_P_State_P_Protocol_P_DestIP,"
                    "Pkts_P_State_P_Protocol_P_SrcIP,attack,category,subcategory",
    "all_columns": ['pkSeqID', 'stime', 'flgs', 'flgs_number', 'proto', 'proto_number', 
                    'saddr', 'sport', 'daddr', 'dport', 'pkts', 'bytes', 'state', 
                    'state_number', 'ltime', 'seq', 'dur', 'mean', 'stddev', 'sum', 
                    'min', 'max', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 'srate', 
                    'drate', 'TnBPSrcIP', 'TnBPDstIP', 'TnP_PSrcIP', 'TnP_PDstIP', 
                    'TnP_PerProto', 'TnP_Per_Dport', 'AR_P_Proto_P_SrcIP', 'AR_P_Proto_P_DstIP', 
                    'N_IN_Conn_P_DstIP', 'N_IN_Conn_P_SrcIP', 'AR_P_Proto_P_Sport', 
                    'AR_P_Proto_P_Dport', 'Pkts_P_State_P_Protocol_P_DestIP', 
                    'Pkts_P_State_P_Protocol_P_SrcIP', 'attack', 'category', 'subcategory'],
        
    "numeric_columns": ['pkSeqID', 'stime', 'flgs_number', 'proto_number', 
                        'pkts', 'bytes', 'state_number', 'ltime', 'seq', 
                        'dur', 'mean', 'stddev', 'sum', 'min', 'max', 
                        'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 
                        'srate', 'drate', 'TnBPSrcIP', 'TnBPDstIP', 
                        'TnP_PSrcIP', 'TnP_PDstIP', 'TnP_PerProto', 
                        'TnP_Per_Dport', 'AR_P_Proto_P_SrcIP', 
                        'AR_P_Proto_P_DstIP', 'N_IN_Conn_P_DstIP', 
                        'N_IN_Conn_P_SrcIP', 'AR_P_Proto_P_Sport', 
                        'AR_P_Proto_P_Dport', 'Pkts_P_State_P_Protocol_P_DestIP', 
                        'Pkts_P_State_P_Protocol_P_SrcIP', 'attack',],

    "column_index": 45,
    "sep": ",",
}

data_cleanup = {
    "classification_col": "subcategory",
    "drop_cols": ['pkSeqID', 'category', 'attack'],
    "replace_values": {},
    "replace_values_in_col": {
    },
    "transform_to_numeric": [
        'pkSeqID', 'stime', 'flgs_number', 'proto_number', 
                        'pkts', 'bytes', 'state_number', 'ltime', 'seq', 
                        'dur', 'mean', 'stddev', 'sum', 'min', 'max', 
                        'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 
                        'srate', 'drate', 'TnBPSrcIP', 'TnBPDstIP', 
                        'TnP_PSrcIP', 'TnP_PDstIP', 'TnP_PerProto', 
                        'TnP_Per_Dport', 'AR_P_Proto_P_SrcIP', 
                        'AR_P_Proto_P_DstIP', 'N_IN_Conn_P_DstIP', 
                        'N_IN_Conn_P_SrcIP', 'AR_P_Proto_P_Sport', 
                        'AR_P_Proto_P_Dport', 'Pkts_P_State_P_Protocol_P_DestIP', 
                        'Pkts_P_State_P_Protocol_P_SrcIP', 'attack',
    ],
    "class_labels": {
        3: "HTTP",
        1: "TCP",
        2: "UDP",
        0: "Normal" 
    },
    "category_encodings": {
        "flgs": {
        "e": 0,
        "e s": 1,
        "e *": 2,
        "e d": 3,
        "e g": 4,
        "eU": 5,
        "e &": 6
        },
        "proto": {
        "tcp": 0,
        "arp": 1,
        "udp": 2,
        "icmp": 3,
        "ipv6-icmp": 4
        },
        "state": {
        "RST": 0,
        "CON": 1,
        "FIN": 2,
        "REQ": 3,
        "ACC": 4,
        "INT": 5,
        "URP": 6,
        "NRS": 7
        },
        "subcategory": {
        "HTTP": 3,
        "TCP": 1,
        "UDP": 2,
        "Normal": 0
        },
    },
}

feature_selections = {
    # EXP_FL16_FT14_R_ / EXP_FL4_FT14_R_
    # All without:
    # 'ts', 'uid', 'label', 'id.orig_h', 'local_orig',
    # 'local_resp', 'missed_bytes',  'tunnel_parents'
    "F14": {
        "description": 'F14',
        "features": ['saddr', 'daddr', 'dport', 'pkts', 'bytes', 'state', 
                    'seq', 'dur', 'mean', 'stddev', 'sum', 
                    'min', 'max', 'spkts', 'dpkts', 'sbytes', 'dbytes', 'rate', 'srate', 
                    'drate',
        ]},

    # EXP_FL16_FT17_R_ / EXP_FL4_FT17_R_
    # All without:
    # 'ts', 'uid', 'label', 'id.orig_h', 'id.resp_h'
    "F17": {
        "description": 'F17',
        "features": [
        ]},

    # EXP_FL16_FT18_R_ / EXP_FL4_FT18_R_
    # All without:
    # 'ts', 'uid', 'label', 'id.orig_h'
    "F18": {
        "description": 'F18',
        "features": [
        ]},

    # All without:
    # 'ts', 'uid', 'label'
    "F19": {
        "description": 'F19',
        "features": [
        ]},
}

datasets = {
    'S16': [],
    'S04': [
        "HTTP.csv",
        "TCP.csv",
        "Normal.csv",
        "UDP.csv"
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