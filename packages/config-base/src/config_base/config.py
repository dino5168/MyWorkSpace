# packages/config-base/src/config_base/__init__.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class CommonSettings(BaseSettings):
    """所有專案都有的通用設定"""
    env: str = "dev"
    log_level: str = "INFO"
    
    # 這裡可以定義通用的 .env 讀取邏輯
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore",      # 忽略多餘的變數
        env_ignore_empty=True
    )