import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier = pickle.load(pickle_in)

def welcome():
  return "Welcome All"

def predict_note_authentication(variance, skewness,curtois, entropy):

  """Let's Authenticate the Banks Note 
  This is using docstrings for specifications.
  ---
  parameters:  
    - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """

  prediction = classifier.predict([[variance,skewness,curtois,entropy]])
  print(prediction)
  return prediction


def main():
  st.title("Bank Authenticator")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
  </div>
  """

  
  st.markdown(html_temp,unsafe_allow_html=True)
  variance = st.text_input("Variance","Type Here")
  skewness = st.text_input("Skewness","Type Here")
  curtois = st.text_input("Curtosis","Type Here")
  entropy = st.text_input("Entropy","Type Here") 
  result = ""
  if st.button("Predict"):
    result = predict_note_authentication(variance,skewness,curtois,entropy)
    st.success('The output is {}'.format(result))
  if st.button("About"):
    st.text("Leats Earn")
    st.text("Build with streamlit")

if __name__ == '__main__':
  main()
