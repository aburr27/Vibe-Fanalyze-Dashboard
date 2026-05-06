# Main dashboard application

import streamlit as st

# Import UI components
from components.teams import show_teams
from components.players import show_players
from components.games import show_games

# Set page configuration (browser tab settings)
st.set_page_config(
    page_title="Vibe-Fanalyze Dashboard",
    layout="wide"
)

# Main title
st.title("🔥 Vibe-Fanalyze Dashboard")

# Sidebar navigation menu
option = st.sidebar.selectbox(
    "Select View",
    ["Teams", "Players", "Games"]
)

# Route to the selected component
if option == "Teams":
    show_teams()

elif option == "Players":
    show_players()

elif option == "Games":
    show_games()
