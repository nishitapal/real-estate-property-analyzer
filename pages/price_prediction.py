import streamlit as st
import joblib
import pickle
import gdown
import pandas as pd
import numpy as np
import os 
if not os.path.exists("pipeline.pkl"):
    url = "https://drive.google.com/uc?id=1MLOZfANe6aaunddIprItZMc-pnUcoACw"  
    gdown.download(url, "pipeline.pkl", quiet=False)

# --- Step 2: pipeline.pkl load karo ---
with open("pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)





st.set_page_config(page_title="Viz Demo")
st.header("Property Price Prediction")
st.subheader('Enter your inputs')

with open('df.pkl','rb') as file:
    df = pickle.load(file)


# 
# url = "https://drive.google.com/uc?id=1MLOZfANe6aaunddIprItZMc-pnUcoACw"
# output = "pipeline.pkl"
# gdown.download(url, output, quiet=False)


with open("pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)


property_type = st.selectbox('Property Type',['flat','house'])


sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

bedrooms = float(st.selectbox('Number of Bedroom',sorted(df['bedRoom'].unique().tolist())))

bathroom = float(st.selectbox('Number of Bathrooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servant_room = float(st.selectbox('Servant Room',[0.0, 1.0]))
store_room = float(st.selectbox('Store Room',[0.0, 1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))
floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']
    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22


    st.text("The price of the flat is between {} Cr and {} Cr".format(round(low,2),round(high,2)))