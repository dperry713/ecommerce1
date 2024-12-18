import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://data1_bywn_user:TWCeIRfbCBUZcGlOpfT7NvieJCzfYSKM@dpg-ctgh2c52ng1s738ibkvg-a:5432/data1_bywn"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
