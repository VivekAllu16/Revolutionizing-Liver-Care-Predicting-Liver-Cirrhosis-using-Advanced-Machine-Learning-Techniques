This HTML file defines a web form interface for a Liver Cirrhosis Prediction web application. Users can input various medical and lifestyle-related features that are relevant for liver disease prediction. The form collects numerical values such as:

Demographic info: Age, Gender

Alcohol use: Duration and Quantity

Infections: Hepatitis B & C

Health markers: Diabetes status, Bilirubin, Albumin, and SGOT/AST levels

Once the form is filled, it sends the data via a POST request to /predict, where a backend (likely built with Flask) processes the data using a machine learning model and returns a prediction (e.g., presence or risk of cirrhosis). The result is displayed dynamically using the placeholder {{ prediction_text }} rendered via Jinja2 templating.

This form is linked to an external CSS file (style.css) to manage its styling.