import streamlit as st
import pandas as pd
import requests
import base64
import json

# --- Einstellungen GitHub ---
GITHUB_USER = "deinBenutzername"
REPO = "deinRepoName"
BRANCH = "main"  # oder master
FILE_PATH = "aufzeichnung.csv"
TOKEN = st.secrets["GITHUB_TOKEN"]  # sicher im Streamlit-Secrets speichern

# --- GitHub Funktionen ---
def get_github_file():
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO}/contents/{FILE_PATH}?ref={BRANCH}"
    r = requests.get(url, headers={"Authorization": f"token {TOKEN}"})
    if r.status_code == 200:
        content = base64.b64decode(r.json()["content"]).decode("utf-8")
        df = pd.read_csv(pd.compat.StringIO(content))
        sha = r.json()["sha"]
        return df, sha
    else:
        # Datei existiert noch nicht
        df = pd.DataFrame(columns=["Ort", "Datum", "Bewertung", "Gut"])
        return df, None

def update_github_file(df, sha=None):
    url = f"https://api.github.com/repos/{GITHUB_USER}/{REPO}/contents/{FILE_PATH}"
    content = df.to_csv(index=False)
    content_b64 = base64.b64encode(content.encode()).decode()
    data = {
        "message": "Update Golf Aufzeichnung",
        "content": content_b64,
        "branch": BRANCH
    }
    if sha:
        data["sha"] = sha
    r = requests.put(url, headers={"Authorization": f"token {TOKEN}"}, data=json.dumps(data))
    return r.status_code == 201 or r.status_code == 200

# --- Streamlit App ---
st.title("Golf 🏌️⛳")
menue = st.sidebar.selectbox("Wähl bitte zwischen", ["Aufzeichnen", "Lesen"])

# --- GitHub Datei laden ---
df, sha = get_github_file()

if menue == "Aufzeichnen":
    st.header("Neues Ereignis eintragen")
    ort = st.radio("Ort auswählen", ["Gastein", "Anderer Ort"])
    if ort == "Gastein":
        eintrag_ort = "Gastein"
    else:
        eintrag_ort = st.text_input("Gib den Ort ein")
    datum = st.date_input("Datum der Runde")
    sterne = st.slider("Bewertung (1 schlecht - 10 gut)", 1, 10, 3)
    gutes = st.text_input("Eine gute Sache vom Spiel")

    if st.button("Speichern"):
        neuer_eintrag = {
            "Ort": eintrag_ort,
            "Datum": datum,
            "Bewertung": sterne,
            "Gut": gutes
        }
        df = pd.concat([df, pd.DataFrame([neuer_eintrag])], ignore_index=True)
        success = update_github_file(df, sha)
        if success:
            st.success("✅ Runde erfolgreich in GitHub gespeichert!")
        else:
            st.error("❌ Fehler beim Speichern in GitHub")

elif menue == "Lesen":
    st.header("Alle Aufzeichnungen")
    if df.empty:
        st.info("Noch keine Daten vorhanden")
    else:
        st.dataframe(df)
