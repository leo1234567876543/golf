import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Golf 🏌️⛳ - Einfacher Tracker für Oma")

# CSV oder Excel hochladen (optional)
uploaded_file = st.file_uploader("Vorhandene Excel-Datei hochladen (optional)", type=["xlsx", "csv"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.read_csv(uploaded_file)
else:
    # Neue Tabelle, falls keine Datei hochgeladen
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
        df = pd.concat([df, pd.DataFrame([neuer_eintrag])], ignore_index=True)
        st.success("✅ Gespeichert!")

# Tabelle anzeigen
st.subheader("Alle bisherigen Einträge")
st.dataframe(df)

# Excel-Datei zum Download anbieten (immer alle Daten enthalten)
output = BytesIO()
with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
    df.to_excel(writer, index=False, sheet_name="GolfSpiele")
    writer.save()
    processed_data = output.getvalue()

st.download_button(
    label="Excel herunterladen (alle Daten)",
    data=processed_data,
    file_name="golf.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
