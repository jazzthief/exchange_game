from src.engine.app import App
from src.engine.config import get_app_config


def launch() -> None:
    app_config = get_app_config()
    app = App(app_config)

    app.run()
