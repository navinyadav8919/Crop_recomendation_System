
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('crop_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(request.form.get(i)) for i in ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
        prediction = model.predict([np.array(features)])
        result = f"✅ Recommended Crop: {prediction[0].capitalize()}"
    except Exception as e:
        result = f"❌ Error: {str(e)}"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
