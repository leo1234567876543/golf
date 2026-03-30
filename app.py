import os
import random
import streamlit as st

st.title("Golf merker")
st.text("Wähle aus was du machen möchtest!")

st.session_state.step = 0
datei=open("aufzeichnung.txt", "a")
st.write("🏌️⛳")
if st.button("Aufzeichnen"):
    st.session_state.step = 1
    st.write("Auf welche Goflplatz hast du gerade gespielt?")
    
    if st.session_state.step >= 1:
        col1, col2 = st.columns(2)
        if col1.button("Golfplatz Gastein):
            st.session_state.step = 2
            ort = ("Golfplatz Gastein")
           
        if col2.button("Option B"):
            st.session_state.step = 2
            ort=  st.write_input("")

  
