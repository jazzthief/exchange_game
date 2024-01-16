from dataclasses import dataclass
from functools import lru_cache


@dataclass
class AppConfig:
    resolution: tuple[int, int] = (1280, 720)


@lru_cache
def get_app_config() -> AppConfig:
    return AppConfig()
