from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the models
try:
    with open('vsmodel.pkl', 'rb') as diabetes_file:
        diabetes_classifier = pickle.load(diabetes_file)
    with open('logregmodel.pkl', 'rb') as heart_file:
        heart_classifier = pickle.load(heart_file)
except Exception as e:
    print(f"Error loading models: {e}")
    diabetes_classifier = None
    heart_classifier = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overview')
def overview():
    return render_template('overview.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/vision')
def vision():
    return render_template('vision.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/working')
def working():
    return render_template('working.html')

@app.route('/choose')
def choose():
    return render_template('choose.html')

@app.route('/doctors1')
def doctors1():
    return render_template('doctors1.html')  # Template for Dr. K.K. Khandelwal

@app.route('/doctors2')
def doctors2():
    return render_template('doctors2.html')  # Template for Dr. S.K. Sinha

@app.route('/doctors3')
def doctors3():
    return render_template('doctors3.html')  # Template for Dr. R.P. Singh

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Template for Contact Us page

@app.route('/diabetes')
def diabetes():
    return render_template('diabetes.html')  # Template for Diabetes Prediction form

@app.route('/heart')
def heart():
    return render_template('heart.html')  # Template for Heart Disease Prediction form

@app.route('/portfolio1')
def portfolio1():
    return render_template('portfolio1.html')  # Template for Cancer Prediction

@app.route('/portfolio2')
def portfolio2():
    return render_template('portfolio2.html')  # Template for Kidney Disease Prediction

@app.route('/portfolio3')
def portfolio3():
    return render_template('portfolio3.html')  # Template for Liver Disease Prediction

@app.route('/portfolio4')
def portfolio4():
    return render_template('portfolio4.html')  # Template for Stroke Prediction

# Diabetes prediction endpoint
@app.route('/predict_diabetes', methods=['POST'])
def predict_diabetes():
    if diabetes_classifier is None:
        return jsonify({'error': 'Diabetes model is not loaded'}), 500

    try:
        # Get JSON data from request
        data = request.json
        print(f"Received data for diabetes prediction: {data}")

        # Required features for diabetes model
        required_features = ['pregnancies', 'glucose', 'blood_pressure', 'insulin', 'bmi', 'age']
        features = []

        for feature in required_features:
            if feature not in data:
                return jsonify({'error': f"'{feature}' is missing"}), 400
            features.append(float(data[feature]))

        print(f"Features for diabetes: {features}")
        
        # Convert to numpy array
        data_array = np.array(features).reshape(1, -1)
        print(f"Data array for diabetes: {data_array}")

        # Make prediction
        prediction = diabetes_classifier.predict(data_array)
        print(f"Diabetes prediction: {prediction}")

        # Map prediction to "Diabetic" or "Non-Diabetic"
        output = "Diabetic" if prediction[0] == 1 else "Non-Diabetic"

        # Return prediction
        return jsonify({'prediction': output})

    except Exception as e:
        print(f"Error in diabetes prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500

# Heart disease prediction endpoint
@app.route('/predict_heart', methods=['POST'])
def predict_heart():
    if heart_classifier is None:
        return jsonify({'error': 'Heart disease model is not loaded'}), 500

    try:
        # Get JSON data from request
        data = request.json
        print(f"Received data for heart disease prediction: {data}")

        # Extract required features and apply mappings
        required_features = {
            'age': float(data.get('age', 0)),
            'sex': int(data.get('sex', 0)),  # 0 for male, 1 for female
            'cp': int(data.get('cp', 0)),    # 0, 1, 2, 3 for chest pain types
            'trestbps': float(data.get('trestbps', 0)),
            'chol': float(data.get('chol', 0))
        }

        # Check if any feature is missing or invalid
        for feature, value in required_features.items():
            if value is None or (isinstance(value, float) and value < 0) or (isinstance(value, int) and value < 0):
                return jsonify({'error': f"Invalid value for '{feature}'"}), 400

        features = [required_features[feature] for feature in ['age', 'sex', 'cp', 'trestbps', 'chol']]

        print(f"Features for heart disease: {features}")

        # Convert to numpy array
        data_array = np.array(features).reshape(1, -1)
        print(f"Data array for heart disease: {data_array}")

        # Make prediction
        prediction = heart_classifier.predict(data_array)
        print(f"Heart disease prediction: {prediction}")

        # Map prediction to "Low Risk" or "High Risk"
        output = "High Risk" if prediction[0] == 1 else "Low Risk"

        # Return prediction
        return jsonify({'prediction': output})

    except Exception as e:
        print(f"Error in heart disease prediction: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
