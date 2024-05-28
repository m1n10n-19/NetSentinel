# .csv files
# attack and normal folders
# different types of attacks labels and normal label

import re



data_metadata = {
    "file_name_pattern": "/*.csv",
    "file_header": "frame.time,ip.src_host,ip.dst_host,arp.dst.proto_ipv4,arp.opcode,arp.hw.size,"
    "arp.src.proto_ipv4,icmp.checksum,icmp.seq_le,icmp.transmit_timestamp,icmp.unused,"
    "http.file_data,http.content_length,http.request.uri.query,http.request.method,http.referer,"
    "http.request.full_uri,http.request.version,http.response,http.tls_port,tcp.ack,tcp.ack_raw,"
    "tcp.checksum,tcp.connection.fin,tcp.connection.rst,tcp.connection.syn,tcp.connection.synack,"
    "tcp.dstport,tcp.flags,tcp.flags.ack,tcp.len,tcp.options,tcp.payload,tcp.seq,tcp.srcport,"
    "udp.port,udp.stream,udp.time_delta,dns.qry.name,dns.qry.name.len,dns.qry.qu,dns.qry.type,"
    "dns.retransmission,dns.retransmit_request,dns.retransmit_request_in,mqtt.conack.flags,"
    "mqtt.conflag.cleansess,mqtt.conflags,mqtt.hdrflags,mqtt.len,mqtt.msg_decoded_as,mqtt.msg,"
    "mqtt.msgtype,mqtt.proto_len,mqtt.protoname,mqtt.topic,mqtt.topic_len,mqtt.ver,mbtcp.len,"
    "mbtcp.trans_id,mbtcp.unit_id,Attack_label,Attack_type",

    "all_columns": ['frame.time', 'ip.src_host', 'ip.dst_host', 'arp.dst.proto_ipv4', 
                    'arp.opcode', 'arp.hw.size', 'arp.src.proto_ipv4', 'icmp.checksum', 
                    'icmp.seq_le', 'icmp.transmit_timestamp', 'icmp.unused', 
                    'http.file_data', 'http.content_length', 'http.request.uri.query', 
                    'http.request.method', 'http.referer', 'http.request.full_uri', 
                    'http.request.version', 'http.response', 'http.tls_port', 
                    'tcp.ack', 'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin', 
                    'tcp.connection.rst', 'tcp.connection.syn', 'tcp.connection.synack', 
                    'tcp.dstport', 'tcp.flags', 'tcp.flags.ack', 'tcp.len', 
                    'tcp.options', 'tcp.payload', 'tcp.seq', 'tcp.srcport', 
                    'udp.port', 'udp.stream', 'udp.time_delta', 'dns.qry.name', 
                    'dns.qry.name.len', 'dns.qry.qu', 'dns.qry.type', 
                    'dns.retransmission', 'dns.retransmit_request', 
                    'dns.retransmit_request_in', 'mqtt.conack.flags', 
                    'mqtt.conflag.cleansess', 'mqtt.conflags', 'mqtt.hdrflags', 
                    'mqtt.len', 'mqtt.msg_decoded_as', 'mqtt.msg', 'mqtt.msgtype', 
                    'mqtt.proto_len', 'mqtt.protoname', 'mqtt.topic', 'mqtt.topic_len', 
                    'mqtt.ver', 'mbtcp.len', 'mbtcp.trans_id', 'mbtcp.unit_id', 
                    'Attack_label', 'Attack_type'],
    "numeric_columns": ['arp.opcode', 'arp.hw.size', 'icmp.checksum', 
                        'icmp.seq_le', 'icmp.transmit_timestamp', 
                        'icmp.unused', 'http.content_length', 
                        'http.response', 'http.tls_port', 'tcp.ack', 
                        'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin', 
                        'tcp.connection.rst', 'tcp.connection.syn', 
                        'tcp.connection.synack', 'tcp.dstport', 'tcp.flags', 
                        'tcp.flags.ack', 'tcp.len', 'tcp.seq', 'udp.port', 
                        'udp.stream', 'udp.time_delta', 'dns.qry.name', 
                        'dns.qry.qu', 'dns.qry.type', 'dns.retransmission', 
                        'dns.retransmit_request', 'dns.retransmit_request_in', 
                        'mqtt.conflag.cleansess', 'mqtt.conflags', 
                        'mqtt.hdrflags', 'mqtt.len', 'mqtt.msg_decoded_as', 
                        'mqtt.msgtype', 'mqtt.proto_len', 'mqtt.topic_len', 
                        'mqtt.ver', 'mbtcp.len', 'mbtcp.trans_id', 
                        'mbtcp.unit_id', 'Attack_label'],

    "column_index": 62, #column index of attack_type
    "sep": ',', #seperater for csv
}

data_cleanup = {
    "classification_col": "Attack_type",
    "drop_cols": ['Attack_label', 'http.file_data', 'mqtt.msg', 'dns.qry.name.len'], #columns (11,51,39) have mixed types and non categorical
    "replace_values": {},
    "replace_values_in_col": {},
    "transform_to_numeric": ['arp.opcode', 'arp.hw.size', 'icmp.checksum', 
                'icmp.seq_le', 'icmp.transmit_timestamp', 
                'icmp.unused', 'http.content_length', 
                'http.response', 'http.tls_port', 'tcp.ack', 
                'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin', 
                'tcp.connection.rst', 'tcp.connection.syn', 
                'tcp.connection.synack', 'tcp.dstport', 'tcp.flags', 
                'tcp.flags.ack', 'tcp.len', 'tcp.seq', 'udp.port', 
                'udp.stream', 'udp.time_delta', 'dns.qry.name', 
                'dns.qry.qu', 'dns.qry.type', 'dns.retransmission', 
                'dns.retransmit_request', 'dns.retransmit_request_in', 
                'mqtt.conflag.cleansess', 'mqtt.conflags', 
                'mqtt.hdrflags', 'mqtt.len', 'mqtt.msg_decoded_as', 
                'mqtt.msgtype', 'mqtt.proto_len', 'mqtt.topic_len', 
                'mqtt.ver', 'mbtcp.len', 'mbtcp.trans_id', 
                'mbtcp.unit_id', 'Attack_label'],

    "class_labels": {
        0: 'Normal', 1: 'Fingerprinting', 
        2: 'DDoS_ICMP', 3: 'Ransomware', 4: 'Port_Scanning', 
        5: 'DDoS_UDP', 6: 'Uploading', 7: 'DDoS_HTTP', 
        8: 'MITM', 9: 'Password', 10: 'XSS', 
        11: 'SQL_injection', 12: 'DDoS_TCP', 
        13: 'Vulnerability_scanner', 14: 'Backdoor',
    },
    "category_encodings": {
        "http.request.method": {
            '0.0': 0,
            '0': 0,
            'GET': 1,
            'POST': 2, 
            'OPTIONS': 3, 
            'TRACE': 4, 
            0.0: 0,
        },
        "http.referer":{'0.0':0, 
                        '0':0, 
                        '127.0.0.1':1},
        "http.request.full_uri":{'0.0': 0, 
                                 '0': 0, 
                                 'http://192.168.0.128/dvwa/vulnerabilities/': 1,
                                'http://192.168.0.128/DVWA/login.php': 2},
        "http.request.version":{'0.0':0, 
                                '0':0, 
                                'HTTP/1.1':1, 
                                'HTTP/1.0':2},
        "mqtt.conack.flags": {'0.0':0, 
                              '0':0, 
                              '0x00000000':1},
        "mqtt.protoname": {'0.0':0, 
                           '0':0, 
                           'MQTT':1},
        "mqtt.topic": {'0.0':0, 
                       '0':0, 
                       'Temperature_and_Humidity':1},
        "Attack_type": {
            'Normal': 0, 'Fingerprinting': 1, 
            'DDoS_ICMP': 2, 'Ransomware': 3, 'Port_Scanning': 4, 
            'DDoS_UDP': 5, 'Uploading': 6, 'DDoS_HTTP': 7, 
            'MITM': 8, 'Password': 9, 'XSS': 10, 
            'SQL_injection': 11, 'DDoS_TCP': 12, 
            'Vulnerability_scanner': 13, 'Backdoor': 14, 
        },
        "Attack_label": {
            0: 0,
            1: 1,
        },
    },
}

feature_selections = {
    # EXP_FL16_FT14_R_ / EXP_FL4_FT14_R_
    # All numeric columns:
    # along with 'http.request.method'
    "F14": {
        "description": 'F14',
        "features": [
            'arp.opcode', 'arp.hw.size', 'icmp.checksum', 
                        'icmp.seq_le', 'icmp.transmit_timestamp', 
                        'icmp.unused', 'http.content_length', 'http.request.method',
                        'http.response', 'http.tls_port', 'tcp.ack', 
                        'tcp.ack_raw', 'tcp.checksum', 'tcp.connection.fin', 
                        'tcp.connection.rst', 'tcp.connection.syn', 
                        'tcp.connection.synack', 'tcp.dstport', 'tcp.flags', 
                        'tcp.flags.ack', 'tcp.len', 'tcp.seq', 'udp.port', 
                        'udp.stream', 'udp.time_delta', 'dns.qry.name', 
                        'dns.qry.qu', 'dns.qry.type', 'dns.retransmission', 
                        'dns.retransmit_request', 'dns.retransmit_request_in', 
                        'mqtt.conflag.cleansess', 'mqtt.conflags', 
                        'mqtt.hdrflags', 'mqtt.len', 'mqtt.msg_decoded_as', 
                        'mqtt.msgtype', 'mqtt.proto_len', 'mqtt.topic_len', 
                        'mqtt.ver', 'mbtcp.len', 'mbtcp.trans_id', 
                        'mbtcp.unit_id', 'Attack_type',
        ]},

    # EXP_FL16_FT17_R_ / EXP_FL4_FT17_R_
    # All without:
    # 
    "F17": {
        "description": 'F17',
        "features": [
            
        ]},

    # EXP_FL16_FT18_R_ / EXP_FL4_FT18_R_
    # All without:
    # 
    "F18": {
        "description": 'F18',
        "features": [
            
        ]},

    # All without:
    # 
    "F19": {
        "description": 'F19',
        "features": [
            
        ]},
}

datasets = {
    'S16': [],
    'S04': [
        "Fingerprinting.csv",
        "Password.csv",
        "Backdoor.csv",
        "Normal.csv", 
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