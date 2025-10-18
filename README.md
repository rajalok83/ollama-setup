Basic Streamlit App to connect to Ollama Models running locally and converse with them.

# Requirements

1. Windows 10 or later
2. Python 3.13 or later
3. OLLAMA installed and configured (refer to [README.MD](https://github.com/rajalok83/ollama-setup/blob/main/README.md) for setup instructions)

# Setup Instructions

1. Setup a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install required Python packages:

   ```bash
    pip install streamlit
    pip install pypdf2
    pip install langchain-community
    pip install ollama
    pip install langchain-ollama
   ```
3. Before running the app, make sure you have completed the [setup]((https://github.com/rajalok83/ollama-setup/blob/main/README.md) with the OLLAMA models in [app.py](./app.py) and running OLLAMA
   ```bash
    ollama serve
   ```  

4. Run the Streamlit app:
   ```bash
    streamlit run app.py
   ```
