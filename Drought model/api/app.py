# from flask import Flask, request, jsonify
# import pandas as pd
# import joblib
# from utils.preprocessing import preprocess_data
# from utils.predictions import make_prediction

# app = Flask(__name__)
# import os
# model = joblib.load(os.path.abspath("../models/Drought_model.pkl"))

# # model = joblib.load("../models/Drought_model.pkl")


import os
from flask import Flask, request, jsonify
import pandas as pd
import joblib
from utils.preprocessing import preprocess_data
from utils.predictions import make_prediction

app = Flask(__name__)

# Correct the path to the model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "../models/Drought_model.pkl")
model = joblib.load(model_path)



@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    processed_data = preprocess_data(df)
    prediction = make_prediction(model, processed_data)
    return jsonify({"DroughtCategory": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)


