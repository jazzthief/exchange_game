from src.config import get_app_config
from src.engine.app import App


def launch() -> None:
    app_config = get_app_config()
    app = App(app_config)

    app.run()


if __name__ == "__main__":
    launch()
