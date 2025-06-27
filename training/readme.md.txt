This project integrates a machine learning model trained in Jupyter Notebook with a Flask web application to predict liver cirrhosis based on user inputs.

 Model Training: The dataset was cleaned and normalized, and a machine learning model was trained to classify whether a patient shows signs of liver cirrhosis.

 Model Saving: The trained model and normalizer were saved using pickle for later use in the Flask backend.

 Frontend Design: An HTML form collects patient data such as age, gender, alcohol consumption, and lab results. CSS styling ensures a clean and user-friendly interface.

 Backend Integration (Flask): The app.py file loads the saved model and normalizer. When the form is submitted, Flask receives the input, preprocesses it, makes a prediction, and displays the result on the webpage.

 Real-time Prediction: The system returns either “Cirrhosis Detected” or “No Cirrhosis Detected” instantly based on the model's output.

This setup provides a complete end-to-end liver disease prediction system—from data input to live prediction—using Python, Flask, HTML, and machine learning.