from my_app.common.configs.settings import settings


def get_blob_key(email: str) -> str:
    return f'{settings.BLOB_BASE_NAME}-{email}'