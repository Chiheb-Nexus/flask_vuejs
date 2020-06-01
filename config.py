#
# Base Config for Project
#


class BaseConfig:
    DEBUG = True


class DevConfig(BaseConfig):
    pass


class ProdConfig(BaseConfig):
    DEBUG = False


CURRENT_CONFIG = DevConfig
