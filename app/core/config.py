from pydantic_settings import BaseSettings
from typing import Optional
from pydantic import model_validator, Field

class Settings(BaseSettings):
    app_name: str = "multitenant-SaaS"
    environment: str = "dev"
    debug: Optional[bool] = Field(default=None)
    log_level: Optional[str] = Field(default=None)

    class Config:
        env_file = ".env"

    @model_validator(mode='after')
    def set_debug_and_log_level(self):
        if self.debug is None:
            self.debug = self.environment in ['dev', 'test']
        if self.log_level is None:
            if self.environment == 'prod':
                self.log_level = 'INFO'
            else:
                self.log_level = 'DEBUG'
        return self

settings = Settings()
