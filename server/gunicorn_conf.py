"""Production server configuration"""
# Importing necessary module for the Gunicorn BaseApplication
from gunicorn.app.base import BaseApplication

class CounterApplication(BaseApplication):
    """Custom Gunicorn Application for running a Flask app."""
    def __init__(self, app, options=None):
        """ Initialize the CounterApplication."""
        self.options = options or {}
        self.application = app
        super(CounterApplication, self).__init__()

    def load_config(self):
        """Load Gunicorn configuration from the provided options."""
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)
    def load(self):
        """Load the CounterApplication application."""
        return self.application