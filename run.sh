#!/bin/bash

source venv/bin/activate

echo "Starting watcher..."
python app/watcher.py &
WATCHER_PID=$!

echo "Starting dashboard..."
streamlit run app/app.py

kill $WATCHER_PID