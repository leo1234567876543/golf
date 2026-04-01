import streamlit as st
import pandas as pd

st.title("Golf 🏌️⛳ - Einfacher Tracker")

# Datei hochladen, falls schon vorhanden
uploaded_file = st.file_uploader("Vorhandene CSV hochladen (optional)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])

# Neues Ereignis eintragen
st.header("Neues Spiel eintragen")
ort = st.text_input("Ort")
datum = st.date_input("Datum")
sterne = st.slider("Bewertung (1 schlecht - 10 gut)", 1, 10, 5)
gut = st.text_input("Mind. 1 gute Sache")

if st.button("Speichern"):
    if ort and gut:
        neuer_eintrag = {
            "Ort": ort,
            "Datum": datum,
            "Bewertung": sterne,
            "Gut": gut
        }
        df = pd.concat([df, pd.DataFrame([neuer_eintrag])], ignore_index=True)
        st.success("✅ Gespeichert!")

# CSV zum Download anbieten
st.download_button("CSV herunterladen", df.to_csv(index=False), "golf.csv")
st.dataframe(df)
