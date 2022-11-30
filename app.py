import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome All"

def main():
  st.title("OddEven")
  html_temp = """
  <div style="background-color:tomato;padding:10px">
  <h2 style="color:white;text-align:center;">Subtraction of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  if is_integer(num1):  
    result = num1%2
    if result==0:  
        st.success('The number is even')
    else: 
        st.success('The number is odd')
  else: 
    st.success('The number is neither even nor odd')
  if st.button("Made By"):
      st.text("Harimanjunathan")
      st.text("21f1001836")

if __name__=='__main__':
  main()
