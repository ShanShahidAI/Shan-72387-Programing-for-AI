
# Week 09 - Introduction to Machine Learning

## Dataset
machines_ml.csv contains synthetic machine data.

## Features
- temp_c
- vibration
- runtime
- pressure

## Target
fault (0 = Normal, 1 = Faulty)

## Machine Learning Model
DecisionTreeClassifier from scikit-learn.

## Method
- Dataset validation
- 75% training and 25% testing
- Stratified train-test split
- Decision Tree training
- Accuracy and confusion matrix evaluation
- Tree depth comparison
- Model saving using joblib
- Predictions on new machine records

## Results
Training and testing accuracies are printed
by ml_pipeline.py.

Depth comparison results are saved in:
reports/model_comparison.csv

The selected model is saved in:
models/machine_predictor.joblib

## Limitations
- Synthetic dataset
- Limited machine features
- A single split cannot establish reliability
- Test-set model selection may bias evaluation
- Real-world validation is required
