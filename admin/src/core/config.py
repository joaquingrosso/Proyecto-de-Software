from os import environ

class Config(object):
    """Base configuration."""
    
    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "secret"
    JWT_SECRET_KEY="secret_key"
    JWT_TOKEN_LOCATION=["cookies"]
    JWT_ACCESS_COOKIE_NAME="access_token_cookie"
    WKHTML_CUSTOM_PATH = environ.get("WKHTML_CUSTOM_PATH", "")
    USE_WKHTML_CUSTOM_PATH = bool(environ.get("USE_WKHTML_CUSTOM_PATH", 0))
class ProductionConfig(Config):
    """Production configuration."""
    ENV_NAME = "prod"
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    ) 


class DevelopmentConfig(Config):
    """Development configuration."""
    ENV_NAME = "dev"
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "postgres")
    DB_PASS = environ.get("DB_PASS", "1234")
    DB_NAME = environ.get("DB_NAME", "grupo13")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    ) 
    WKHTML_CUSTOM_PATH = environ.get("WKHTML_CUSTOM_PATH", r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    USE_WKHTML_CUSTOM_PATH = bool(environ.get("USE_WKHTML_CUSTOM_PATH", 1))


class TestingConfig(Config):
    """Testing configuration."""

    TESTING = True
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER", "MY_DB_USER")
    DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
    DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
    ) 

config = dict(
    development=DevelopmentConfig,
     test=TestingConfig,
      production=ProductionConfig
)





























#cosas viejas para el pdf
# from os import environ

# class Config(object):
#     """Base configuration."""
    
#     DB_HOST = "bd_name"
#     DB_USER = "db_user"
#     DB_PASS = "db_pass"
#     DB_NAME = "db_name"
#     SECRET_KEY = "secret"

# class ProductionConfig(Config):
#     """Production configuration."""
#     ENV_NAME = "prod"
#     DB_HOST = environ.get("DB_HOST", "localhost")
#     DB_USER = environ.get("DB_USER", "MY_DB_USER")
#     DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
#     DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
#     ) 


# class DevelopmentConfig(Config):
#     """Development configuration."""
#     ENV_NAME = "dev"
#     DB_HOST = environ.get("DB_HOST", "localhost")
#     DB_USER = environ.get("DB_USER", "postgres")
#     DB_PASS = environ.get("DB_PASS", "1234")
#     DB_NAME = environ.get("DB_NAME", "grupo13")
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
#     ) 

# class TestingConfig(Config):
#     """Testing configuration."""

#     TESTING = True
#     DB_HOST = environ.get("DB_HOST", "localhost")
#     DB_USER = environ.get("DB_USER", "MY_DB_USER")
#     DB_PASS = environ.get("DB_PASS", "MY_DB_PASS")
#     DB_NAME = environ.get("DB_NAME", "MY_DB_NAME")
#     SQLALCHEMY_DATABASE_URI = (
#         f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
#     ) 

# config = dict(
#     development=DevelopmentConfig,
#      test=TestingConfig,
#       production=ProductionConfig
# )
