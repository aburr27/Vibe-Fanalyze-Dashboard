# UI component for displaying games

import streamlit as st
from services.api_client import get_games


def show_games():
    """
    Displays games in the UI
    """

    st.header("📊 Games")

    games = get_games()

    if not games:
        st.warning("No games found")
        return

    for game in games:
        st.write(
            f"Game {game['id']} | "
            f"Home: {game['home_team_id']} vs Away: {game['away_team_id']} | "
            f"Score: {game['home_score']} - {game['away_score']}"
        )
