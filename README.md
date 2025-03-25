# NYC 311 Service Request Response Time Prediction

This project analyzes NYC 311 service request data to predict response times using machine learning techniques. It includes data cleaning, feature engineering, and model development with XGBoost.

## Project Structure

- `01_data_loading_cleaning.ipynb`: Initial data loading and cleaning processes
- `02_feature_engineering.ipynb`: Creation of temporal, spatial, and operational features
- `03_eda.ipynb`: Exploratory data analysis, visualization, and model training

## Key Features

- Uses Polars for efficient data processing of large datasets
- Comprehensive feature engineering including:
  - Temporal features (time of day, day of week, season)
  - Spatial features (borough analysis)
  - Operational workload metrics
  - Weather data integration
  - COVID-19 period indicators
- XGBoost model with hyperparameter tuning via Optuna
- Visualization of key factors affecting response times

## Model Performance

- R² score: 0.74
- MAE: 20.96 hours
- RMSE: 38.46 hours

## Key Findings

1. Escalated requests take approximately 10x longer to resolve
2. Priority scoring shows strong correlation with response times
3. Geographic variation is relatively small (8-hour maximum difference between boroughs)
4. Significant temporal patterns in response times by day of week and hour of day
5. Seasonal effects with winter showing the longest response times

## Setup and Installation

### Using Poetry

```bash
# Install dependencies using Poetry
poetry install

# Activate the virtual environment
poetry shell
```

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
