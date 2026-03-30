import os
import random
import streamlit as st

st.title("Golf merker")
st.text("Wähle aus was du machen möchtest!")

st.session_state.step = 0
datei=open("aufzeichnung.txt", "a")
st.write("🏌️⛳")
if st.button("Aufzeichnen"):
    butt = 1
    st.write("Auf welche Goflplatz hast du gerade gespielt?")
    
    if butt == 1:
        if st.buton("Golfplatz Gastein): 
            ort = ("Golfplatz Gastein")
            st.success("Gastein")            
            
           
        if st.button("Option B"):
           
            ort=  st.write_input("")

  
