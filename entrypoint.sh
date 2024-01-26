
# the command to install all the packages and dependecies that are required
pip install -r requirements.txt
# Start the gunicorn server t0 serve the webapplication
gunicorn -b 0.0.0.0:8000 app:app