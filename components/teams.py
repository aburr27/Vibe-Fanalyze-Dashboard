# UI component for displaying teams

import streamlit as st
from services.api_client import get_teams


def show_teams():
    """
    Displays teams in the UI
    """

    # Page header
    st.header("🏀 Teams")

    # Fetch data from API
    teams = get_teams()

    # If no data returned
    if not teams:
        st.warning("No teams found")
        return

    # Loop through each team and display it
    for team in teams:
        st.write(f"**{team['name']}** - {team['city']}")
