import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://opensource-demo.orangehrmlive.com/web/index.php")
    USERNAME = os.getenv("ORANGE_USERNAME", "Admin")
    PASSWORD = os.getenv("ORANGE_PASSWORD", "admin123")
    TIMEOUT = 20000  # 20 seconds default timeout

settings = Settings()
