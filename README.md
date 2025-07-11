
# 🌾 Crop Recommendation System

A machine learning-based web application that recommends the most suitable crop to cultivate based on various soil and environmental parameters.

---

## 🚀 Project Overview

This project uses **supervised learning** (Random Forest, Decision Tree, etc.) to help farmers and agriculturists make informed decisions about which crop to grow. The model predicts the most suitable crop based on input features like **Nitrogen**, **Phosphorus**, **Potassium**, **temperature**, **humidity**, **pH**, and **rainfall**.

---

## 🧠 Features

- 🌱 Predicts the best crop using trained ML models
- 💡 Real-time predictions through an easy-to-use web interface
- 📊 Heatmap visualization for correlation analysis
- 📈 Confusion matrix and classification report for evaluation
- 🔍 Grid Search for hyperparameter tuning

---

## 🛠️ Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Frontend     | HTML, CSS, Bootstrap      |
| Backend      | Flask (Python)            |
| ML Models    | Random Forest, Decision Tree |
| Libraries    | pandas, numpy, matplotlib, seaborn, scikit-learn |

---

## 📊 Input Parameters

- **Nitrogen (N)**
- **Phosphorus (P)**
- **Potassium (K)**
- **Temperature (°C)**
- **Humidity (%)**
- **pH**
- **Rainfall (mm)**

---

## 🖥️ How to Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/navinyadav8919/Crop_recomendation_System.git
cd Crop_recommendation_System
````

### 2. Create and activate a virtual environment

```bash
python -m venv env
env\Scripts\activate        # On Windows
# source env/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask app

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

## 🌐 Live App

✅ Try the deployed app here:
👉 [https://croprecomendationsystem-naveen.streamlit.app/](https://croprecomendationsystem-naveen.streamlit.app/)

---

## ✅ Results

* ✅ Accuracy: **95+%** on test data using Random Forest
* 📊 Evaluated using confusion matrix and classification report
* 🔍 Feature importance and heatmaps used for model interpretation

---

## 📁 Project Structure

```
Crop_recommendation_System/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── model.pkl
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Author

**Naveen Yadav**
🔗 GitHub: [@navinyadav8919](https://github.com/navinyadav8919)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

