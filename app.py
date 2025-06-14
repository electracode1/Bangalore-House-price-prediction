import streamlit as st
import pickle
import pandas as pd

# Load the trained model and dataset
model = pickle.load(open('random_forest_house_price_model.pkl', 'rb'))
dataset = pickle.load(open('dataset.pkl', 'rb'))
locations = dataset['location'].unique()

st.title("Bangalore House Price Prediction")

# User inputs
location = st.selectbox('Location', locations)
total_sqft = st.number_input('Total Square Foot', min_value=0.0, value=1000.0)
col1, col2 = st.columns(2)
with col1:
    bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
with col2:
    bhk = st.number_input('Number of Bedrooms (BHK)', min_value=1, max_value=10, value=2)

# Optional input for balcony
balcony = st.number_input('Number of Balconies', min_value=0, max_value=5, value=1)

# Prediction
if st.button('Predict'):
    # Create input_data with all required columns
    input_data = pd.DataFrame(
        [[location, total_sqft, bath, bhk, balcony, 'Super built-up Area', 'Ready To Move', '2 BHK', 'NA']],
        columns=['location', 'total_sqft', 'bath', 'BHK', 'balcony', 'area_type', 'availability', 'size', 'society']
    )
    

    
    # Make prediction
    try:
        prediction = model.predict(input_data)[0]
        st.write(f"The predicted price is {prediction:.2f} lakhs")
    except Exception as e:
        st.error(f"Error during prediction: {e}")

#The error indicates that Windows can't find the `streamlit` command because the installation directory isn't in your system's PATH. Here's how to fix it:

#1. Add this directory to your PATH:
# ```
# C:\Users\mayur\AppData\Roaming\Python\Python312\Scripts
# ```

# Two ways to run streamlit until you update PATH:

# 1. Use full path:
# ```
# C:\Users\mayur\AppData\Roaming\Python\Python312\Scripts\streamlit.exe run app.py
# ```

# 2. Use Python module:
# ```
# python -m streamlit run app.py
# ```

# Need help updating your PATH variable?