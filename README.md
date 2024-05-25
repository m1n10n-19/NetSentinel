# NetSentinel

## Datasets

#### Edge-IIoTset Cyber Security Dataset

Source: [https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot](https://www.kaggle.com/datasets/mohamedamineferrag/edgeiiotset-cyber-security-dataset-of-iot-iiot)

Description:

Comprehensive dataset of IoT and IIoT applications for machine learning-based intrusion detection systems.

Organized into seven layers with various IoT devices and technologies.

Includes 14 identified attacks related to IoT and IIoT connectivity protocols.

Purpose: Used for evaluating machine learning approaches in both centralized and federated learning modes.

#### IoT-23 Dataset

Source: [https://www.stratosphereips.org/datasets-iot23](https://www.stratosphereips.org/datasets-iot23)

Description:

Contains network traffic from IoT devices.

Includes 20 captures of IoT malware and 3 captures of benign IoT traffic.

Captured in the Stratosphere Laboratory, CTU University, Czech Republic.

Purpose: Provides labeled data for developing machine learning algorithms for IoT malware detection.

### CIC IoT Dataset

Source: [https://www.unb.ca/cic/datasets/iotdataset-2023.html](https://www.unb.ca/cic/datasets/iotdataset-2023.html)

Description:

Consists of 33 attacks executed in an IoT topology with 105 devices.

Attacks classified into DDoS, DoS, Recon, Web-based, Brute Force, Spoofing, and Mirai categories.

Purpose: Aims to foster the development of security analytics applications in real IoT operations.

#### IoT Network Intrusion Dataset

Source: [https://ieee-dataport.org/open-access/iot-network-intrusion-dataset](https://ieee-dataport.org/open-access/iot-network-intrusion-dataset)

Description:

Contains network attacks in an IoT environment.

Consists of 42 raw network packet files (pcap) captured at different time points.

Includes simulated attacks using tools such as Nmap, with one category involving manipulation to simulate originating from IoT devices.

Purpose: Created for academic purposes to study network attacks in IoT environments.

# Step by Step Overview

## Network Traffic Extraction

Wireshark along with Python is used for Feature Extraction from .pcap files. .csv files are generated.

## Metadata Generation

The metadata corressponding to various datasets are generated using Python and stored in metadata.py

## Setting Up config.py

The desired file location for storing data and results are set up in config.py. This is verified by running 01_configuration_check.py

## Data Extraction from various Scenarios

Run 02_extract_data_from_scenarios.py for this task. Data will be stored according to attack type(label) in seperate files.

## Data Shuffling after Extraction

Executed by 03_shuffle_file_content.py. The stored data is shuffled randomly.

## Data Preparation

Includes shuffling file content and splitting into train and test data

## Training Models

A dictionary of pipelines was created for the five models selected

## Experimentation Results

# Demo

A sample experiment is given in demo.py. Custom experiments can be run by doing minimal alterations to this code based on metadata.py
