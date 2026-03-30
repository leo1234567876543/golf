import os
import random
import streamlit as st

st.title("Golf merker")
st.text("Wähle aus was du machen möchtest!")

if st.button("Aufzeichnung Platz"):
    datei=open("aufzeichnung.txt", "a")
    st.info("Auf welche Goflplatz hast du gerade gespielt?")
