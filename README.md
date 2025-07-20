# 🏠 House Price Predictor

This is a machine learning web application that predicts house prices based on area, number of bedrooms, bathrooms, and location type.  
It uses a **Linear Regression** model trained with **scikit-learn**, and features a clean interactive UI built with **Streamlit**.  
Ideal for practicing regression, data preprocessing, and model deployment.

---

## 📁 Project Structure
house-price-predictor/
├── app.py # Streamlit web app
├── train_model.py # Script to train and save the model
├── house_model.pkl # Trained Linear Regression model (pickled)
├── house_data.csv # Dataset used for training
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## 📊 Tech Stack

- Python
- Pandas
- NumPy
- scikit-learn
- Streamlit

---

## 🚀 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Maariak-cs/house-price-predictor.git
   cd house-price-predictor
   
2. **Create a virtual environment (optional but recommended)**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   ```bash
    pip install -r requirements.txt

4. **Train the model (if not already trained)**
    ```bash
    python train_model.py

5. **Run the app**
    ```bash  
    streamlit run app.py

---

## 🧠 How It Works
Input features: area, bedrooms, bathrooms, and location
The train_model.py script uses a pipeline with:
    OneHotEncoder for location
    LinearRegression for modeling
The trained model is saved as house_model.pkl
The Streamlit app (app.py) loads the model and provides a simple web interface to predict house prices in ₹ Lakhs

---

## 🙋‍♀️ Author
Maaria Khan
Final Year Computer Science Engineering Student
🔗www.linkedin.com/in/maariak-cs

