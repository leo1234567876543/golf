import streamlit as st
import pandas as pd
import dropbox
import io

# --- Titel ---
st.title("Golf 🏌️⛳")

# --- Menü ---
menue = st.sidebar.selectbox("Wähl bitte zwischen", ["Aufzeichnen", "Lesen"])

# --- Dropbox Setup ---
DROPBOX_TOKEN = st.secrets["DROPBOX_TOKEN"]
dbx = dropbox.Dropbox(DROPBOX_TOKEN)

FILE_PATH = "/GolfApp/aufzeichnung.csv"

# --- CSV laden ---
def load_data():
    try:
        metadata, res = dbx.files_download(FILE_PATH)
        df = pd.read_csv(io.BytesIO(res.content))
        return df
    except:
        return pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])

# --- CSV speichern ---
def save_data(df):
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    dbx.files_upload(
        csv_buffer.getvalue().encode(),
        FILE_PATH,
        mode=dropbox.files.WriteMode.overwrite
    )

# --- Daten laden ---
df = load_data()

# --- AUFZEICHNEN ---
if menue == "Aufzeichnen":
    st.header("Neues Ereignis eintragen")

    ort = st.radio("Wähl hier bitte den Ort aus", ["Gastein", "Anderer Ort"])
    if ort == "Gastein":
        eintrag_ort = "Gastein"
    else:
        eintrag_ort = st.text_input("Gib hier den Ort ein")

    datum = st.date_input("Gib hier das Datum ein")
    sterne = st.slider("Bewertung (1 schlecht - 10 gut)", 1, 10, 5)
    gutes = st.text_input("Schreibe mind. 1 gute Sache")

    if st.button("Speichern"):
        if eintrag_ort and gutes:
            neuer_eintrag = {
                "Ort": eintrag_ort,
                "Datum": str(datum),
                "Bewertung": sterne,
                "Gut": gutes
            }

            df = pd.concat([df, pd.DataFrame([neuer_eintrag])], ignore_index=True)
            save_data(df)

            st.success("✅ Erfolgreich in Dropbox gespeichert!")
        else:
            st.error("Bitte alle Felder ausfüllen!")

# --- LESEN ---
elif menue == "Lesen":
    st.header("Deine Golf Runden")

    if df.empty:
        st.info("Noch keine Einträge vorhanden.")
    else:
        df_anzeige = df.copy()
        df_anzeige["Bewertung"] = df_anzeige["Bewertung"].apply(lambda x: "⭐"*int(x))

        st.dataframe(df_anzeige)
