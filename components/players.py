# UI component for displaying players

import streamlit as st
from services.api_client import get_players


def show_players():
    """
    Displays players in the UI
    """

    st.header("👤 Players")

    players = get_players()

    if not players:
        st.warning("No players found")
        return

    for player in players:
        st.write(
            f"{player['name']} | "
            f"Position: {player['position']} | "
            f"Team ID: {player['team_id']}"
        )
