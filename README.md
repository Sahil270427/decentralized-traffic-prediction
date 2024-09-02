
# Decentralized Traffic Congestion Prediction System

This repository contains the implementation of a secure, decentralized traffic congestion prediction system developed for smart transportation networks. It integrates Artificial Intelligence (AI), Federated Learning (FL), Blockchain, and the InterPlanetary File System (IPFS) to enhance data privacy, scalability, and system efficiency.

## 🧠 Project Overview

Urban traffic congestion remains a persistent challenge in major cities. This project proposes a decentralized system where vehicles and roadside units (RSUs) collaborate to predict traffic congestion using AI models, without sharing raw data. Blockchain and IPFS are used for secure, immutable, and decentralized data management.

## 🔧 Technologies Used

- **Artificial Intelligence (AI)**: For traffic prediction using models like Random Forest, LSTM, and Gradient Boosting.
- **Federated Learning (FL)**: To train models locally at nodes and aggregate them globally without centralizing sensitive data.
- **Blockchain**: To store model metadata, manage contributor reputations, and enforce smart contract-based rewards.
- **IPFS (via Pinata)**: For decentralized and tamper-proof storage of machine learning models.

## 📁 Project Structure

```
decentralized-traffic-prediction/
├── Blockchain_Final/
│   ├── Blockchain_Final.ipynb           # Main notebook for blockchain and FL integration
│   ├── contributor_1_dataset.csv        # ↓ See 'Data Access' below
│   ├── contributor_2_dataset.csv        # ↓
│   ├── contributor_3_dataset.csv        # ↓
│   ├── contributor_4_dataset.csv        # ↓
├── TX1_5m_Preprocessed.csv              # ↓
├── Data_Upload_Download/
│   ├── First1m.csv                      # ↓
├── Data_Preprocessing/
│   ├── TX_1_5m.csv                      # ↓
```

## 📥 Data Access

All large CSV datasets are hosted externally due to GitHub’s file size limits.

👉 [Download all CSV files here (Google Drive Folder)](https://drive.google.com/drive/folders/1MxtXHvBQkqjMFUr3VxZOxkZLTUCnWBoL?usp=sharing)

After downloading, place the files into the following project subdirectories:

| File Name                 | Folder                    |
|---------------------------|---------------------------|
| contributor_1_dataset.csv | Blockchain_Final/         |
| contributor_2_dataset.csv | Blockchain_Final/         |
| contributor_3_dataset.csv | Blockchain_Final/         |
| contributor_4_dataset.csv | Blockchain_Final/         |
| TX1_5m_Preprocessed.csv   | root folder               |
| First1m.csv               | Data_Upload_Download/     |
| TX_1_5m.csv               | Data_Preprocessing/       |


## ⚙️ Setup Instructions

1. **Clone this Repository**:
```bash
git clone https://github.com/Sahil270427/decentralized-traffic-prediction.git
cd decentralized-traffic-prediction
```

2. **Create a Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Requirements**:
```bash
pip install -r Blockchain_Final/requirements.txt
```

4. **Run the Jupyter Notebook**:
```bash
jupyter notebook Blockchain_Final/Blockchain_Final.ipynb
```

## 📊 Data Description

The primary dataset is derived from the **Large-Scale Traffic and Weather Events (LSTW)** dataset focusing on traffic data in Texas. It includes various features such as event type, severity, time, and location.

## 🔐 Key Features

- **Privacy-Preserving AI** using Federated Learning.
- **Tamper-Proof Data** through blockchain immutability.
- **Decentralized Storage** using IPFS with Pinata integration.
- **Smart Contracts** to manage model registration and contributor incentives.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

## 📣 Acknowledgements

Developed as part of the MSc dissertation at the University of Sussex (2024) under the supervision of Dr. Naercio Magaia.

---

Built for smart cities and scalable traffic solutions. 🌍🚦
