# Landslide Prediction System

## Overview

The *Landslide Prediction System* is a machine learning-based solution designed to predict the likelihood of landslides in specific regions. It uses environmental data, such as rainfall, soil moisture, to provide accurate and timely warnings, helping to mitigate the impact of landslides on lives and property.

## Features

- *Data Collection*: Integrates real-time and historical environmental data.
- *Machine Learning Models*: Predicts landslide risks based on collected data.
- *Visualization*: Provides easy-to-understand risk maps and warnings.
- *Scalability*: Adaptable for multiple regions with diverse terrains.
- *Integration*: Can be integrated with disaster early warning systems.

## Tech Stack

- *Programming Language*: Python
- *Machine Learning Frameworks*: TensorFlow, Scikit-learn
- *Web Framework*: Flask(for API)
- *Database*: MongoDB
- *Front-end*: React (for visualization)
- *Deployment*: Docker

## How It Works

1. *Data Preprocessing*:
   - Collects data from weather stations, satellites, and sensors.
   - Cleans and processes the data for training models.

2. *Model Training*:
   - Uses machine learning algorithms like Random Forest, Gradient Boosting, or Neural Networks.
   - Trained on features such as rainfall intensity, slope stability, soil type, etc.

3. *Prediction*:
   - Predicts the probability of a landslide in specific regions.
   - Provides early warnings based on real-time data.

4. *Visualization*:
   - Displays risk zones on an interactive map.
   - Sends notifications via SMS, email, or app alerts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IT21241550/Research_project
   cd Landslide

2. Navigate to the project directory.
cd Landslide

3. Install dependencies:
    ```bash
    pip install -r api/requirements.txt
    ```
4. Train the model:
    ```bash
    python models/train_model.py
    ```
5. Start the API:
    ```bash
    python api/app.py
    ```


