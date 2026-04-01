import streamlit as st
import pandas as pd
from io import StringIO

st.title("Golf 🏌️⛳")

menue = st.sidebar.selectbox("Wähle:", ["Aufzeichnen", "Daten ansehen"])

uploaded_file = st.file_uploader("Vorhandene CSV hochladen (optional)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])

if menue == "Aufzeichnen":
    st.header("Neues Ereignis eintragen")
    ort_aus = st.radio("Trage hier den Ort ein",["Gastein", "Anderer Ort"])
    if radio_input=="Gastein":
        ort="Gastein"
    if radio_input=="Anderer Ort":
        ort= st.text_input("Gib hier den Ort ein")
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

# ----------------------------
# Menü: Daten ansehen
# ----------------------------
elif menue == "Daten ansehen":
    st.header("Alle bisherigen Einträge")
    st.dataframe(df)

# ----------------------------
# CSV zum Download anbieten
# ----------------------------
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)
st.download_button(
    label="CSV herunterladen (alle Daten)",
    data=csv_buffer.getvalue(),
    file_name="golf.csv",
    mime="text/csv"
)
