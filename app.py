import numpy as np
import pickle
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
scale = pickle.load(open('encoder.pkl', 'rb')) 
@app.route('/')  
def home():
    return render_template("index.html")  
@app.route('/predict', methods=["POST", "GET"])  
def predict():
    try:
        input_feature = [float(x) for x in request.form.values()]
        
        categorical_columns = ['holiday', 'temp', 'rain', 'snow', 'weather', 'year', 'month', 'day','hours', 'minutes', 'seconds']
        if len(input_feature) != len(categorical_columns):
            return jsonify({"error": "Feature mismatch. Expected {}, but got {}.".format(len(categorical_columns), len(input_feature))})

        
        data = pd.DataFrame([input_feature], columns=categorical_columns)
        print("Feature names in input data:", data.columns) 
        data = scale.transform(data.to_numpy())  # Convert DataFrame to NumPy array
        prediction = model.predict(data)
        return render_template("output.html", prediction_text="Estimated Traffic Volume: " + str(prediction[0]))
    except Exception as e:
        return jsonify({"error": str(e)})
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)
    
