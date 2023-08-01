class OARepoPublishedService(object):
    """OARepo extension of published service."""

    def __init__(self, app=None):
        """Extension initialization."""
        self.service = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
        app.extensions["oarepo-published-service"] = self

    def init_services(self, app):
        """Initialize services."""
        self.service = app.config["OAREPO_PUBLISHED_SERVICE"](
            config=app.config["OAREPO_PUBLISHED_SERVICE_CONFIG"](),
        )

    def init_config(self, app):
        """Initialize configuration."""
        from . import ext_config

        for k in dir(ext_config):
            if k.startswith("OAREPO_"):
                app.config.setdefault(k, getattr(ext_config, k))
