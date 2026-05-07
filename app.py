# Main dashboard application

import streamlit as st  # type: ignore[import-not-found]

# Import UI components
from components.teams import show_teams
from components.players import show_players
from components.games import show_games
from components.login import show_login

# Set page configuration (browser tab settings)
st.set_page_config(
    page_title="Vibe-Fanalyze Dashboard",
    layout="wide"
)

# Main title
st.title("🔥 Vibe-Fanalyze Dashboard")

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# --- LOGIN GATE ---
if not st.session_state["logged_in"]:
    show_login()
    st.stop()  # stop app until logged in

# Sidebar navigation menu
option = st.sidebar.selectbox(
    "Navigation",
    ["Teams", "Players", "Games"]
)

# --- LOGOUT BUTTON ---
if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

# Route to the selected component
if option == "Teams":
    show_teams()

elif option == "Players":
    show_players()

elif option == "Games":
    show_games()
