import streamlit as st  # type: ignore[reportMissingImports]
from services.api_client import login, set_token


def show_login():
    """
    Login form UI
    """

    st.subheader("🔐 Login")

    # Input fields
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        result = login(email, password)

        # If token exists → success
        if "access_token" in result:
            set_token(result["access_token"])

            # Save login state in session
            st.session_state["logged_in"] = True

            st.success("Logged in successfully")

        else:
            st.error("Invalid credentials")