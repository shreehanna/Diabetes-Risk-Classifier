import joblib
from data_loader import load_and_clean_data
from model import train_and_evaluate_model
df = load_and_clean_data('diabetes.txt')
model = train_and_evaluate_model(df)
joblib.dump(model, 'diabetes_model.pkl')
print("✅ Model trained and saved as diabetes_model.pkl")


