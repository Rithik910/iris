import streamlit as st
import numpy as np
import joblib
model = joblib.load('iris')
st.title('Iris flower Classifier')
ip = st.text_input('enter sepal_length')
ip1 = st.text_input('enter sepal_width')
ip2 = st.text_input('enter petal_length')
ip3 = st.text_input('enter petal_width')

if st.button('Predict'):
	if(ip!="" and ip1!="" and ip2!="" and ip3!=""):
		op = model.predict([[float(ip),float(ip1),float(ip2),float(ip3)]])
		if op== 0:
			st.title("Iris-setosa")
		elif op== 1:
			st.title("Iris-versicolor")
		elif op== 2:
			st.title("Iris-verginica")
		
else:
	print("Program ended")

