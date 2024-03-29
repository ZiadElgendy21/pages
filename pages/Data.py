import pandas as pd 
import streamlit as st 

st.markdown("<h1> <center> German Cars DataSet </center> </h1>",unsafe_allow_html= True)
df = pd.read_csv("./Sources/autoscout24-germany-dataset.csv")
st.markdown('<a href= "https://www.kaggle.com/datasets/ander289386/cars-germany"> <center> Link to DataSet </center> </a>',unsafe_allow_html= True)
st.write(df)