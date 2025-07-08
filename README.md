
# 🌾 Crop Recommendation System

A machine learning-based web application that recommends the most suitable crop to cultivate based on various soil and environmental parameters.

## 🚀 Project Overview

This project uses supervised learning (Random Forest, Decision Tree, etc.) to help farmers and agriculturists make informed decisions about which crop to grow. The model predicts the best crop based on input features like Nitrogen, Phosphorus, Potassium, temperature, humidity, pH, and rainfa

## 🧠 Features

- Predicts the best crop using trained ML models
- User-friendly web interface built with Flask
- Real-time predictions based on user input
- Heatmap visualization of correlation
- Confusion matrix and classification report for evaluation
- Grid Search for hyperparameter tuning

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Python, Flask
- **ML Algorithms:** Random Forest, Decision Tree
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn

## 📊 Input Parameters

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- pH
- Rainfall (mm)


## 🖥️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/navinyadav8919/Crop_recomendation_System.git
   cd Crop_recomendation_System

2. Create and activate a virtual environment:

 
   python -m venv env
   env\Scripts\activate   # On Windows
  
3. Install dependencies:

  
   pip install -r requirements.txt
  

4. Run the Flask app:

   
   python app.py
  

5. Open your browser and go to:

  
   http://127.0.0.1:5000
  


## PROJECT LINK
https://croprecomendationsystem-naveen.streamlit.app/


*Add screenshots of your UI here.*

## ✅ Results

* Accuracy: **95+%** on test data using Random Forest
* Evaluated with confusion matrix and classification report
* Feature importance and heatmaps for insights

## 📁 Project Structure

Crop_recommendation_System/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── model.pkl
├── requirements.txt
└── README.md

# 🙋‍♂️ Author

**Naveen Yadav**
🔗 [GitHub](https://github.com/navinyadav8919)

## 📜 License

This project is licensed under the MIT License.



