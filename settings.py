import os
import sys

import tensorflow as tf
from pydantic.v1 import BaseSettings


os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")


class Settings(BaseSettings):
    STATIC_FOLDER = "static"
    UPLOAD_FOLDER = "static/uploads"
    CAT_DOG_MODEL = tf.keras.models.load_model(
        os.path.join(STATIC_FOLDER, "models", "cat_dog.keras")
    )

    class Config:
        case_sensitive = True


settings = Settings()
