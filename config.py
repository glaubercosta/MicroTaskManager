from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MicroTaskManager"
    database_url: str = "sqlite:///./db.sqlite3"
    debug: bool = False

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
