
# Weather Forecasting with Machine Learning

This repository contains my diploma thesis project on **Weather Forecasting using Machine Learning Algorithms**.

The goal of the project is to explore how different machine learning methods can be used to analyze and predict meteorological variables such as rainfall, temperature, humidity, atmospheric pressure, wind speed, and wind direction.

## Project Overview

Weather forecasting is an important real-world problem with applications in agriculture, transport, energy, and public safety.  
In this project, I used Greek meteorological data and compared multiple approaches from:

- **Supervised learning**
- **Unsupervised learning**
- **Deep learning for time-series prediction**

The repository includes exploratory data analysis, preprocessing, classical machine learning models, clustering methods, and neural-network-based forecasting.

## Dataset

The dataset used in this project comes from the **Hellenic Data Service** and contains CSV files from meteorological stations in Greece, covering the years **2010 to 2019**.

Example columns in the original dataset include:

- `date`
- `mean_temp`
- `max_temp`
- `min_temp`
- `mean_hum`
- `max_hum`
- `min_hum`
- `mean_pres`
- `max_pres`
- `min_pres`
- `rain`
- `mean_speed_wind`
- `dir_wind`
- `max_gust_wind`

For the experiments, the main variables used were:

- `mean_temp`
- `mean_pres`
- `mean_hum`
- `rain`
- `mean_speed_wind`
- `dir_wind`

## Methods

### Exploratory Data Analysis
The project includes scripts for exploratory analysis and visualization of:
- temperature
- humidity
- pressure
- rainfall
- wind speed
- wind direction

### Classification
The following classical machine learning methods were used:

- K-Nearest Neighbors (KNN)
- Regression / Logistic Regression
- Random Forest
- Decision Tree
- Support Vector Machine (SVM)
- Naive Bayes

### Clustering
The following clustering methods were applied:

- K-Means
- Agglomerative Clustering

### Deep Learning
For sequential weather prediction, I implemented:

- Recurrent Neural Network (RNN)
- Long Short-Term Memory network (LSTM)

## Main Findings

The main conclusions of the project were:

- The most useful classification results were obtained for **rain prediction**
- Classification performance for rainfall was around **0.7**
- The remaining target variables produced weaker classification results
- **LSTM achieved better loss values than RNN**
- This suggests that LSTM is a more suitable architecture than a simple RNN for this weather-forecasting task

## Tools and Libraries

The implementation was developed in Python using libraries such as:

- `csv`
- `pandas`
- `numpy`
- `matplotlib`
- `scikit-learn`

## Repository Structure

```text
.
├── data/               # dataset files
├── src/                # source code for EDA, ML, clustering, RNN, and LSTM
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/jimvak/weather-forecasting-ml.git
cd weather-forecasting-ml
pip install -r requirements.txt


**How to Run**  
This is the most important missing section. Your README describes the scripts conceptually, but it does not tell the reader which command runs which part. :contentReference[oaicite:3]{index=3}

```markdown
## How to Run

Place the dataset inside the `data/` folder and run the scripts from the project root.

Example commands:

```bash
python src/weather_classification_models.py
python src/weather_clustering.py
python src/rnn_weather_forecasting.py
python src/lstm_weather_forecasting.py
