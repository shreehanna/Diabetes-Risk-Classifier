# 🩺 Diabetes Risk Classifier

A machine learning app that predicts the likelihood of diabetes based on patient health metrics.  
Built with **Python**, **scikit-learn**, and deployed with **Streamlit**.  

🔗 **[Live Demo](https://diabetes-risk-classifier-mrwytgb6wv2wb8p3uvjzmv.streamlit.app/)**

---

## 📌 Project Overview
This project uses the **Pima Indians Diabetes Dataset** to train models that classify whether a patient is at risk for diabetes.  
It demonstrates:
- Data preprocessing & feature engineering
- Model training & evaluation
- Comparative analysis between algorithms
- Deployment of an interactive web app

---

## 🧠 Models Used
- **Logistic Regression**
- **Random Forest Classifier**

Both models were compared based on:
- Accuracy
- Precision
- Recall
- F1-score

---

## 📂 Repository Structure
├── app.py # Streamlit app script
├── train_model.py # Script to train and save models
├── model.py # Model training & evaluation logic
├── data_loader.py # Loads and preprocesses the dataset
├── diabetes_model.pkl # Saved trained model
├── requirements.txt # Project dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation (Local Run)
Clone the repository and install dependencies:
```bash
git clone https://github.com/shreehanna/Diabetes-Risk-Classifier.git
cd Diabetes-Risk-Classifier
pip install -r requirements.txt
To train the model:

bash
Copy
Edit
python train_model.py
To launch the app locally:

bash
Copy
Edit
streamlit run app.py
📊 Results
Model	Accuracy	Precision	Recall	F1-score
Logistic Regression	0.78	0.74	0.71	0.72
Random Forest	0.81	0.77	0.75	0.76

🌟 Future Improvements
Hyperparameter tuning

Gradient boosting models

Integration with NVIDIA Clara healthcare pipelines

Enhanced visualization of predictions
