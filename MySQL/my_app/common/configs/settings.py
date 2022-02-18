import secrets
from typing import Annotated, Any, Literal

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field,
)
from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    APP_NAME: str = "User App"
    ROOT_PATH: str = "/api"

    PDF_QUESTION_BUCKET: str = "my-portfolio-question-bucket"
    PROJECT_ID: str = "my-app-424608"

    SECRET_ID: str = "gg-secret"
    SECRET_VERSION: str = "2"
    READ_SECRET_FROM_ENV: bool = True  # read from environment variable

    GEMINI_VERSION: str = "gemini-1.5-flash"  # "gemini-pro"
    EMBEDDING_MODEL: str = "models/embedding-001"
    QUESTION_BUCKET: str = "my-portfolio-question-bucket"
    BLOB_BASE_NAME: str = "testy-bytes"

    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    DOMAIN: str = "localhost"
    ENVIRONMENT: Literal["local", "staging", "production"] = (
        "production"  # read from environment variable
    )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def server_host(self) -> str:
        # Use HTTPS for anything other than local development
        if self.ENVIRONMENT == "local":
            return f"http://{self.DOMAIN}"
        return f"https://{self.DOMAIN}"

        # "http://localhost",
        # "http://localhost:5173",
    BACKEND_CORS_ORIGINS: Annotated[list[AnyUrl] | str, BeforeValidator(parse_cors)] = [
        "https://vyathartha.com",
        "https://vyathartha.com/",
        "https://www.vyathartha.com",
    ]


settings = Settings()  # type: ignore
