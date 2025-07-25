import streamlit as st
import pandas as pd
from datetime import date

# Titel & Startseite
st.set_page_config(page_title="Trainingstagebuch", layout="wide")
st.title("📋 Trainingstagebuch")
st.markdown(f"**📅 Heute ist:** {date.today().strftime('%A, %d.%m.%Y')} – Plan B")

# Button zum Starten
if st.button("🔥 Einheit starten"):
    st.success("✅ Einheit gestartet – Viel Erfolg!")

# Dummy-Daten Plan B
data = [
    {"Übung": "Squat", "Last (kg)": 50.0, "Reps": 7, "RIR": 2},
    {"Übung": "Squat", "Last (kg)": 50.0, "Reps": 7, "RIR": 1},
    {"Übung": "Squat", "Last (kg)": 50.0, "Reps": 4, "RIR": 1},
    {"Übung": "LH-Schrägbank", "Last (kg)": 40.0, "Reps": 5, "RIR": 0},
    {"Übung": "LH-Schrägbank", "Last (kg)": 40.0, "Reps": 4, "RIR": 0},
    {"Übung": "LH-Schrägbank", "Last (kg)": 40.0, "Reps": 4, "RIR": 0},
    {"Übung": "Latzug", "Last (kg)": 63.0, "Reps": 13, "RIR": 3},
    {"Übung": "Latzug", "Last (kg)": 77.0, "Reps": 6, "RIR": 1},
    {"Übung": "Latzug", "Last (kg)": 77.0, "Reps": 6, "RIR": 0},
    {"Übung": "Reverse Fly", "Last (kg)": 13.75, "Reps": 9, "RIR": 2},
    {"Übung": "Reverse Fly", "Last (kg)": 13.75, "Reps": 9, "RIR": 1},
    {"Übung": "Seitheben", "Last (kg)": 9.0, "Reps": 10, "RIR": 2},
    {"Übung": "Seitheben", "Last (kg)": 10.0, "Reps": 9, "RIR": 1}
]
df = pd.DataFrame(data)

# Tabelle zur Bearbeitung
st.markdown("### 🏋️‍♂️ Trainingseinheit – Eingabe")
edited_df = st.data_editor(df, num_rows="dynamic")

# CSV Export
st.markdown("### 💾 Export")
csv = edited_df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Export als CSV", csv, file_name="trainingseinheit.csv", mime="text/csv")
