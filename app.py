import streamlit as st
import requests
from datetime import datetime

st.title('Taxi Fare Predictor')
st.markdown('Please enter the details of your ride to get an estimated fare.')

d = st.date_input("Date of ride", datetime.now())
t = st.time_input('Time of ride', datetime.time(datetime.now()))
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.number_input('Passenger count', min_value=1, max_value=8)

if st.button('Get Estimated Fare'):
    url = 'https://taxifare.lewagon.ai/predict'

    params = {
        "pickup_datetime": f"{d} {t}",
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    response = requests.get(url, params=params)

    prediction = response.json()

    st.success(f'The estimated fare is : $ {prediction["fare"]:.2f}')
