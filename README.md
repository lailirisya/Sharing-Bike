# Setup Enviroment  
conda create -n submission python=3.9
conda activate submission
pip freeze requirements

# Cara menjalankan dashboard di vscode (localhost)
streamlit run dashboard.py
