import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('NLP_Final.pkl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()

st.title("Disaster Tweets Predictor")
st.markdown("**This application helps you to identify any disaster related things.**")
st.markdown("**You can enter your disaster related tweets in the text box and click on Predict button to get the result.**")
input_test = st.text_input("Enter your Tweet here", '')

button_clicked = st.button("Predict Tweet")
#if button_clicked:
def showResults():
    Model_Predict = Lrdetect_Model.predict([input_test])

    if Model_Predict[0]==1:
     st.text("This Tweet is a Disaster")

    else:
     st.text("This Tweet is not a Disaster")

if(button_clicked):
    showResults()

#footer
footer = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 40%;
    background-color: #B5C3C1;
    padding: 10px;
    text-align: center;
}
</style>
<div class="footer">
    Made by Sasanka Pasanjith
</div>
"""
st.markdown(footer, unsafe_allow_html=True)



