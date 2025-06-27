from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and normalizer
model = joblib.load('rf_acc_68.pkl')           # Your trained RandomForest model on 10 features
normalizer = joblib.load('normalizer.pkl')     # Your fitted Normalizer or StandardScaler

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Define the order of features as per training
        feature_order = [
            'Age', 
            'Gender', 
            'Duration of alcohol consumption(years)', 
            'Quantity of alcohol consumption (quarters/day)', 
            'Hepatitis B infection', 
            'Hepatitis C infection', 
            'Diabetes Result', 
            'Total Bilirubin (mg/dl)', 
            'Albumin (g/dl)', 
            'SGOT/AST (U/L)'
        ]

        # Collect input values in correct order
        input_features = [float(request.form[feature]) for feature in feature_order]

        # Convert to array and normalize
        input_array = np.array([input_features])
        input_normalized = normalizer.transform(input_array)

        # Make prediction
        prediction = model.predict(input_normalized)
        result = 'Positive for Cirrhosis' if prediction[0] == 1 else 'Negative for Cirrhosis'

        return render_template('index.html', prediction_text=f'Result: {result}')

    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
