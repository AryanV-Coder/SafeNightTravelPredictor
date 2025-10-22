import streamlit as st
import pickle
import pandas as pd

# Load the saved models and encoders
@st.cache_resource
def load_models():
    with open('model_training/models/tuned_logistic_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model_training/models/ordinal_encoder.pkl', 'rb') as f:
        oe = pickle.load(f)
    with open('model_training/models/onehot_encoder.pkl', 'rb') as f:
        ohe = pickle.load(f)
    return model, oe, ohe

# Load models
model, oe, ohe = load_models()

# Title
st.title("🌚 Safe Night Travel Predictor 🌝")
st.subheader("Enter your details to predict if it's safe to travel at this time👇🏼")

# First row: 2 inputs
col1, col2 = st.columns(2)
with col1:
    time = st.number_input("Time at which you are travelling (1-24 hours)", 
                           min_value=1, max_value=24, value=12, step=1)
with col2:
    phone_battery_level = st.number_input("Phone Battery Level", 
                                          min_value=0, max_value=100, value=50, step=1)

# Second row: 2 inputs
col3, col4 = st.columns(2)
with col3:
    gender = st.selectbox("Gender", ["M", "F", "Other"])
with col4:
    mode_of_transport = st.selectbox("Mode of Transport", ["4-wheeler", "2-wheeler", "walk", "auto"])

# Third row: 3 inputs
col5, col6, col7 = st.columns(3)
with col5:
    location_familiarity = st.selectbox("Are you familiar with the location?", ["yes", "no"])
with col6:
    presence_of_companions = st.selectbox("Will you have companions?", ["yes", "no"])
with col7:
    previous_incident_area = st.selectbox("Any previous incidents in this area?", ["yes", "no"])

if st.button("Anaylse Safety") :
    data = pd.DataFrame(
        [[time,gender,location_familiarity,mode_of_transport,presence_of_companions,phone_battery_level,previous_incident_area]],
        columns=['Time','Gender','LocationFamiliarity','ModeOfTransport', 'PresenceOfCompanions','PhoneBatteryLevel','PreviousIncidentArea']
    )

    


