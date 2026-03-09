from pathlib import Path
from config_base.config import CommonSettings
from pydantic_settings import SettingsConfigDict

# 1. 自動計算 apps/a01 的絕對路徑
# 假設此檔案在: D:/MyWorkSpace/apps/a01/config/config.py
# .parent 1次 = config/
# .parent 2次 = a01/ (這就是我們要的專案根目錄)
APP_ROOT = Path(__file__).resolve().parent.parent

class AppSettings(CommonSettings):
    # 必填欄位
    API_KEY: str
    
    # 2. 強制指定使用絕對路徑讀取該專案下的 .env
    model_config = SettingsConfigDict(
        env_file=APP_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = AppSettings()