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
  
import pandas as pd

uploaded_file = st.file_uploader("Lade deine bestehende CSV hoch (optional)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])

if "daten" not in st.session_state:
    st.session_state.daten = []

if st.button("Speichern"):
    neuer_eintrag = {
        "Ort": eintrag_ort,
        "Datum": datum,
        "Bewertung": sterne,
        "Gut": gutes
    }
    st.session_state.daten.append(neuer_eintrag)
    st.success("Gespeichert!")

# Download anbieten
if st.session_state.daten:
    df = pd.DataFrame(st.session_state.daten)
    st.download_button("Download CSV", df.to_csv(index=False), "golf.csv")
      
      
