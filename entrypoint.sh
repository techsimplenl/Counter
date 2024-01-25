# create a virtual environment 
python3 -m venv venv
# activate the environment that was created
source venv/bin/activate
# Upgrade pip package to the latest version
pip install --upgrade pip 
# the command to install all the packages and dependecies that are required
pip install -r requirements.txt
# Start the gunicorn server t0 serve the webapplication
gunicorn -b 0.0.0.0:8000 app:app