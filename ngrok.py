import os
import time
from pyngrok import ngrok
import threading

# Function to run Streamlit app
def run_streamlit():
    os.system("streamlit run app.py")

# Start Streamlit in background
streamlit_thread = threading.Thread(target=run_streamlit)
streamlit_thread.start()

# Wait for Streamlit to boot up
time.sleep(5)

# Create a tunnel to the Streamlit app
public_url = ngrok.connect(8501)
print("App is live at:", public_url)
