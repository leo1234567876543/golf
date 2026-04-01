import streamlit as st
import pandas as pd
from io import StringIO

st.title("Golf 🏌️⛳ - Einfacher Tracker für Oma")

# CSV hochladen (optional)
uploaded_file = st.file_uploader("Vorhandene CSV hochladen (optional)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    # Neue DataFrame, falls keine Datei hochgeladen
    df = pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])

# Neues Spiel eintragen
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
        # Neuen Eintrag an bestehende DataFrame anhängen
        df = pd.concat([df, pd.DataFrame([neuer_eintrag])], ignore_index=True)
        st.success("✅ Gespeichert!")

# Tabelle anzeigen
st.subheader("Alle bisherigen Einträge")
st.dataframe(df)

# CSV zum Download anbieten (immer alle Daten enthalten)
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
st.download_button(
    label="CSV herunterladen (alle Daten)",
    data=csv_buffer.getvalue(),
    file_name="golf.csv",
    mime="text/csv"
)
