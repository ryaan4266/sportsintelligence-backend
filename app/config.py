import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    database_url: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/athena_sports",
    )
    frontend_url: str = os.getenv("FRONTEND_URL", "http://localhost:5173")


settings = Settings()
