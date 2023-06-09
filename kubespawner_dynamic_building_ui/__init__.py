import os
from tornado.web import StaticFileHandler


HERE = os.path.dirname(__file__)

TEMPLATE_PATHS = [os.path.join(HERE, 'templates')]

STATIC_HANDLER_TUPLE = (
    '/kubespawner-dynamic-building-ui/static/(.*)',
    StaticFileHandler,
    {"path": os.path.join(HERE, "static")}
)


def setup_ui(c):
    """
    Setup config to enable the UI provided by this package.

    Expects to be called from a `jupyterhub_config.py` file, with `c`
    the config object being passed in.
    """
    c.KubeSpawner.additional_profile_form_template_paths = TEMPLATE_PATHS

    # Add extra handler to serve JS & CSS assets
    c.JupyterHub.extra_handlers.append(STATIC_HANDLER_TUPLE)
