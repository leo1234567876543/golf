import os
import random
import streamlit as st

st.title("Golf merker")
st.text("Wähle aus was du machen möchtest!")


datei=open("aufzeichnung.txt", "a")
st.write("🏌️⛳")
if st.button("Aufzeichnen"):
    st.write("Auf welche Goflplatz hast du gerade gespielt?")

    if st.button("Golfplatz Gastein ⛳"):
        ort = ("Golfplatz Gastein")
        
    if st.button("Ein anderer Golfplatz ⛳"):
        ort = st.text_input("Gib hier den Platz ein")
if st.button("A"):
    st.write("aaaa")
