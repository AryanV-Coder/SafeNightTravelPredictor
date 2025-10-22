import streamlit as st
import joblib
import pandas as pd

# Load the saved models and encoders
@st.cache_resource
def load_models():
    model = joblib.load('model_training/models/tuned_logistic_model.pkl')
    oe = joblib.load('model_training/models/ordinal_encoder.pkl')
    ohe = joblib.load('model_training/models/onehot_encoder.pkl')
    le = joblib.load('model_training/models/label_encoder.pkl')

    return model, oe, ohe, le

# Load models
model, oe, ohe, le = load_models()

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

# Predict button
if st.button("🔮 Predict Safety", type="primary"):
    data = pd.DataFrame(
        [[time,gender,location_familiarity,mode_of_transport,presence_of_companions,phone_battery_level,previous_incident_area]],
        columns=['Time','Gender','LocationFamiliarity','ModeOfTransport', 'PresenceOfCompanions','PhoneBatteryLevel','PreviousIncidentArea']
    )

    # Encoding Binary Features using Ordinal Encoder
    binary_features = ['LocationFamiliarity', 'PresenceOfCompanions', 'PreviousIncidentArea']
    data[binary_features] = oe.transform(data[binary_features])

    # Encoding Multi-Categorical Features using One-Hot-Encoder
    encoded_columns = ohe.transform(data[["Gender","ModeOfTransport"]]).toarray()
    encoded_columns = pd.DataFrame(encoded_columns,columns = ohe.get_feature_names_out())
    data = pd.concat([data, encoded_columns], axis=1)
    data.drop(['Gender', 'ModeOfTransport'], axis=1,inplace=True)

    prediction = model.predict(data)
    
    # Decode using label encoder
    decoded_result = le.inverse_transform(prediction)[0]
    
    # Display result
    st.markdown("---")
    if decoded_result == "yes":
        st.success("✅ It is SAFE to travel!")
    else:
        st.error("⚠️ It is NOT SAFE to travel!")