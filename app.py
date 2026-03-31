import streamlit as st
import os

st.title("Golf 🏌️⛳")
st.text("Wähle aus")
menue=st.sidebar.selectbox("Wähl bitte zwischen", ["Aufzeichnen", "Lesen"])

if menue=="Aufzeichnen":
  st.text("Neues Ereigniss eintragen")
  ort=st.radio("Wähl hier bitte den Ort aus wo du gespielt hast", ["Gastein", "In einen anderen Ort"])
  if ort=="Gastein":
        eintrag_ort="Gastein"
  if ort=="In einen anderen Ort":
        eintrag_ort=st.text_input("Gib hier den Ort ein")
  datum=st.date_input("Gib hier das Datum ein")
  sterne=st.stars_input("Gib hier deine eigene bewertung ein")
