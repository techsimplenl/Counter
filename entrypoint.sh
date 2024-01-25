python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

gunicorn -b 0.0.0.0:8000 app:app