"""Production server configuration"""
from gunicorn.app.base import BaseApplication
class FlaskApplication(BaseApplication):
    """Server class"""
    def __init__(self, app, options):
        self.options = options or {}
        self.application = app
        super(FlaskApplication, self).__init__()
    def load_config(self):
        """Function load configuration configuration"""
        for key, value in self.options.items():
            if key in self.cfg.settings and value is not None:
                self.cfg.set(key.lower(), value)
    def load(self):
        """Function load configuration"""
        return self.application
