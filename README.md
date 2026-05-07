# 📊 Vibe-Fanalyze Dashboard

An interactive sports analytics dashboard built with Streamlit that consumes the Vibe-Fanalyze FastAPI backend.

---

## 🚀 Overview

The Vibe-Fanalyze Dashboard provides a user-friendly interface to:

- Explore teams, players, and games
- Visualize sports data
- Interact with backend analytics
- Serve as the frontend layer of a full-stack analytics platform

This project demonstrates **frontend data consumption, API integration, and interactive UI development**.

---

## 🧱 Tech Stack

- **Streamlit** – interactive UI framework
- **Requests** – API communication
- **Pandas** – data handling and transformation

---

vibe-fanalyze-dashboard/
│
├── app.py                # Main dashboard entry point
├── services/             # API communication layer
│   └── api_client.py
├── components/           # UI components
│   ├── teams.py
│   ├── players.py
│   └── games.py
├── requirements.txt
└── README.md

---

## 🔗 Backend Dependency

This dashboard connects to:

👉 Vibe-Fanalyze API (FastAPI backend)

Make sure your API is running:

```bash
uvicorn app.main:app --reload
