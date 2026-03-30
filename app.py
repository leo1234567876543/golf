# golf_tracker_app.py
import streamlit as st
import os

DATEI = "aufzeichnung.txt"


def aufzeichnen(ort, datum, sterne):
    with open(DATEI, "a") as datei:
        datei.write(f"{ort},{datum},{sterne}\n")

st.title("⛳ Golf")

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
            st.success(f"Runde in {ort} am {datum} mit {sterne} Stern(en) gespeichert!")
        else:
            st.error("Bitte Ort eingeben!")


