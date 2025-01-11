# Flood Monitoring System

## Description
The Flood Monitoring System is a web application built using Streamlit that utilizes machine learning models to predict the risk of floods based on various environmental factors such as rainfall, river water levels, temperature, and time-related factors like year and month. The model predicts the likelihood of flood occurrence and provides valuable information to help in flood management and disaster preparedness.

## How to Run the Application
1. Ensure you have Python installed on your machine.
2. Install the required dependencies:
   ```bash
   pip install streamlit pandas numpy scikit-learn joblib
   ```
3. Run the application using the following command:
   ```bash
   streamlit run main2.py
   ```
4. Open your web browser and navigate to the URL provided in the terminal.

## Usage
- Enter the environmental data such as year, month, rainfall, river water level, and temperature.
- Click on the "Predict Flood Occurrence" button to get the flood risk prediction.
- The application will display whether the flood risk is high or low along with appropriate warnings.

## Images
![Flood Monitoring System](image.jpg)

![Flood Monitoring System](image1.jpg)

## License
This project is licensed under the MIT License.
