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
        st.write("ab")

    if st.button("Ein anderer Golfplatz ⛳"):
        st.write("a")
if st.button("A"):
    st.write("aaaa")
