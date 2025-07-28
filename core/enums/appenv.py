#
# Author: Rohtash Lakra
#
import os

from enum import unique

from core.enums import BaseEnum


@unique
class AppEnv(BaseEnum):
    """Represents an application's env"""

    DEVELOPMENT = "develop"
    PRODUCTION = "production"
    STAGING = "staging"
    TESTING = "test"
    LOCAL = "local"
    QA = "qa"

    @staticmethod
    def is_production(app_env: str) -> bool:
        """Returns true for production env other false"""
        return AppEnv.equals(AppEnv.PRODUCTION, app_env)

    @staticmethod
    def is_development(app_env: str) -> bool:
        """Returns true for development env other false"""
        return AppEnv.equals(AppEnv.DEVELOPMENT, app_env)

    @staticmethod
    def is_testing(app_env: str) -> bool:
        """Returns true for testing env other false"""
        return AppEnv.equals(AppEnv.TESTING, app_env)

    @staticmethod
    def is_staging(app_env: str) -> bool:
        """Returns true for staging env other false"""
        return AppEnv.equals(AppEnv.STAGING, app_env)

    @staticmethod
    def is_local(app_env: str) -> bool:
        """Returns true for local env other false"""
        return AppEnv.equals(AppEnv.LOCAL, app_env)

    @staticmethod
    def is_qa(app_env: str) -> bool:
        """Returns true for qa env other false"""
        return AppEnv.equals(AppEnv.QA, app_env)

    @classmethod
    def get_app_env(cls):
        return os.getenv("APP_ENV")
