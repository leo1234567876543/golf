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
  sterne=st.slider("Gib hier deine eigene Bewertung ein (1 Schlecht - 10 Gut)", 1, 10, 3)
  gutes=st.text_input("Schreibe mind. 1 Gute Sache von deinem Spiel auf")
  if st.button("Speichern"):
      st.text("ab")
