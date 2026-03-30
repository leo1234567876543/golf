# golf_tracker_app.py
import streamlit as st
import os

DATEI = "aufzeichnung.txt"

# --- Funktion zum Aufzeichnen ---
def aufzeichnen(ort, datum, sterne):
    with open(DATEI, "a", encoding="utf-8") as datei:
        datei.write(f"{ort},{datum},{sterne}\n")

# --- Funktion zum Lesen ---
def lesen():
    if not os.path.exists(DATEI):
        return []
    with open(DATEI, "r", encoding="utf-8") as datei:
        text = datei.readlines()
    daten = []
    for zeile in text:
        ort, datum, sterne = zeile.strip().split(",")
        daten.append({"Ort": ort, "Datum": datum, "Bewertung": sterne})
    return daten

# --- Streamlit UI ---
st.title("⛳ Golf-Tracker")

menu = st.sidebar.selectbox("Menü auswählen", ["Aufzeichnen", "Lesen"])

if menu == "Aufzeichnen":
    st.header("Neue Runde eintragen")
    
    ort_option = st.radio("Ort auswählen oder eigenen Ort eingeben", ["Gastein", "Anderer Ort"])
    if ort_option == "Gastein":
        ort = "Gastein"
    else:
        ort = st.text_input("Gib den Ort ein")
    
    datum = st.date_input("Datum der Runde")
    sterne = st.slider("Bewertung (1=schlecht, 5=sehr gut)", 1, 5, 3)
    
    if st.button("Speichern"):
        if ort:
            aufzeichnen(ort, datum, sterne)
            st.success(f"Runde auf {ort} am {datum} mit {sterne} Stern(en) gespeichert!")
        else:
            st.error("Bitte Ort eingeben!")

elif menu == "Lesen":
    st.header("Alle Aufzeichnungen")
    daten = lesen()
    if daten:
        st.table(daten)
    else:
        st.info("Noch keine Aufzeichnungen vorhanden.")
