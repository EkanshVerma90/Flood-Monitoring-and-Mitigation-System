import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load('flood_prediction_random_forest.pkl')

# Title of the app
st.title('Flood Monitoring System')

# About section
# Add an image for the system (replace 'flood_image.jpg' with your image file)
st.sidebar.title('ABOUT')
st.sidebar.image('image.jpg', caption='Flood Monitoring System', use_column_width=True)
st.sidebar.write("This Flood Monitoring System uses machine learning models to predict the risk of floods based on various environmental factors such as rainfall, river water levels, temperature, and time-related factors like year and month.The model predicts the likelihood of flood occurrence and provides valuable information to help in flood management and disaster preparedness.")

# Add an image for the system (replace 'flood_image.jpg' with your image file)
st.image('image1.jpg', caption='Flood Monitoring System',width=500)

# Input fields for the user to enter data
st.header('Enter Environmental Data')

year = st.number_input('Year', min_value=2004, max_value=2024, value=2004)
month = st.selectbox('Month', 
                     ["January", "February", "March", "April", "May", "June", 
                      "July", "August", "September", "October", "November", "December"])

rainfall = st.number_input('Rainfall (in mm)', min_value=0, max_value=1000, value=0)
river_level = st.number_input('River Water Level (in meters)', min_value=0.0, max_value=1000.0, value=0.0)
temperature = st.number_input('Temperature (in °C)', min_value=0.0, max_value=200.0, value=0.0)


# Convert the month into numerical value (1 = January, 2 = February, etc.)
month_num = ["January", "February", "March", "April", "May", "June", 
             "July", "August", "September", "October", "November", "December"].index(month) + 1

# Prepare input data for prediction
input_data = np.array([[year, month_num, rainfall, river_level, temperature]])



# Prediction
if st.button('Predict Flood Occurrence'):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.write("Flood Risk: High")
        st.warning("High Risk Flood Warning: Severe flooding expected.Evacuate immediately, avoid floodwaters, move to higher ground, and stay informed.")
    else:
        st.write("Flood Risk: Low")
        st.warning("Low risk of flooding due to moderate rainfall. Localized water accumulation possible. Stay alert and avoid low-lying areas.")


