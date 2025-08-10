#!/bin/bash

# Ensure the Mistral model is downloaded
ollama pull mistral

# Start FastAPI backend in the background
uvicorn backend.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Start Streamlit frontend in the background
streamlit run frontend/app.py --server.address 0.0.0.0 --server.port 8501 &
FRONTEND_PID=$!

# Wait for both processes to exit
wait $BACKEND_PID $FRONTEND_PID 