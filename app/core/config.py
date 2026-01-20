from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "multitenant-SaaS"
    environment: str = "dev"

    class Config:
        env_file = ".env"

settings = Settings()
