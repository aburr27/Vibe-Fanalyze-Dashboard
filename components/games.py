# UI component for displaying games

import pandas as pd
import streamlit as st  # type: ignore[import-not-found]
from services.api_client import get_games


def show_games():
    """
    Displays games in the UI
    """

    st.header("📊 Games Analytics")

    games = get_games()

    if not games:
        st.warning("No games found")
        return

# Convert list of dicts → DataFrame
    df = pd.DataFrame(games)

    # --- BASIC METRICS ---
    st.subheader("📈 Summary Stats")

    total_games = len(df)
    avg_home_score = df["home_score"].mean()
    avg_away_score = df["away_score"].mean()

    st.write(f"Total Games: {total_games}")
    st.write(f"Avg Home Score: {avg_home_score:.2f}")
    st.write(f"Avg Away Score: {avg_away_score:.2f}")

    # --- CHART: SCORES ---
    st.subheader("📊 Score Comparison")

    st.line_chart(df[["home_score", "away_score"]])

    # --- TABLE VIEW ---
    st.subheader("📋 Raw Data")
    st.dataframe(df)

    for game in games:
        st.write(
            f"Game {game['id']} | "
            f"Home: {game['home_team_id']} vs Away: {game['away_team_id']} | "
            f"Score: {game['home_score']} - {game['away_score']}"
        )
