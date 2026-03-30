import streamlit as st
from github import Github

# --- KONFIGURATION (Hier deine Daten eintragen) ---
REPO_NAME = "DEIN_NUTZERNAME/DEIN_REPO"
DATEI_PFAD = "aufzeichnung.txt"

# Session State initialisieren, damit die Seite sich merkt, wo wir sind
if 'step' not in st.session_state:
    st.session_state.step = "start"

st.title("🏌️ Golf Merker")

# SCHRITT 1: Start-Button
if st.session_state.step == "start":
    if st.button("Aufzeichnen"):
        st.session_state.step = "platz_wahl"
        st.rerun()

# SCHRITT 2: Golfplatz wählen
if st.session_state.step == "platz_wahl":
    st.write("Auf welchem Golfplatz hast du gespielt?")
    col1, col2 = st.columns(2)
    
    if col1.button("Golfplatz Gastein"):
        st.session_state.ort = "Golfplatz Gastein"
        st.session_state.step = "details"
        st.rerun()
    if col2.button("Anderer Platz"):
        st.session_state.ort = "Anderer Platz"
        st.session_state.step = "details"
        st.rerun()

# SCHRITT 3: Details eingeben (Datum, Bewertung)
if st.session_state.step == "details":
    st.subheader(f"Details für {st.session_state.ort}")
    
    datum = st.date_input("Wann hast du gespielt?")
    bewertung = st.feedback("stars") # 0-4 Sterne (entspricht 1-5)

    if st.button("Speichern"):
        # Daten für die Datei formatieren
        eintrag = f"{datum} | {st.session_state.ort} | Sterne: {bewertung + 1}\n"
        
        # --- GITHUB SPEICHER-LOGIK ---
        try:
            g = Github(st.secrets["GITHUB_TOKEN"])
            repo = g.get_repo(REPO_NAME)
            contents = repo.get_contents(DATEI_PFAD)
            
            # Neue Zeile an bestehenden Inhalt anhängen
            neuer_inhalt = contents.decoded_content.decode() + eintrag
            repo.update_file(contents.path, "Neuer Golf-Eintrag", neuer_inhalt, contents.sha)
            
            st.success("Erfolgreich in der Cloud gespeichert!")
            st.session_state.step = "start" # Zurück zum Anfang
        except Exception as e:
            st.error(f"Fehler beim Speichern: {e}")

# OPTIONAL: Daten wieder ausgeben
if st.button("Meine Spiele anzeigen"):
    # Hier könntest du die Datei von GitHub laden und mit st.text() anzeigen
    st.info("Diese Funktion kann die Daten aus der 'aufzeichnung.txt' laden.")

