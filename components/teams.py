# UI component for displaying teams

try:
    import streamlit as st  # type: ignore[import-not-found]
except ImportError:
    class _StreamlitFallback:
        def header(self, *_args, **_kwargs):
            pass

        def warning(self, message):
            print(message)

        def write(self, message):
            print(message)

    st = _StreamlitFallback()

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
