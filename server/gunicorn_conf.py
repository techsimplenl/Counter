"""Production server configuration"""
from gunicorn.app.base import BaseApplication
class FlaskApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(FlaskApplication, self).__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)
        # for key, value in self.options.items():
        #     if key in self.cfg.settings and value is not None:
        #         self.cfg.set(key.lower(), value)
    def load(self):
        return self.application