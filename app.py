import streamlit as st
import joblib
model = joblib.load('iris')
st.title('Iris flower Classifier')
ip = st.text_input('enter sepal_length,sepal_width,petal_length,petal_width')
op = model.predict(list(ip))
if st.button('Predict'):
	st.title(op[0])
