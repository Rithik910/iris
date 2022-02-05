import streamlit as st
import joblib
model = joblib.load('iris')
st.title('Iris flower Classifier')
ip = st.text_input('enter sepal_length')
ip1 = st.text_input('enter sepal_width')
ip2 = st.text_input('enter petal_length')
ip3 = st.text_input('enter petal_width')
op = model.predict([ip,ip1,ip2,ip3])
if st.button('Predict'):
	st.title(op[0])
