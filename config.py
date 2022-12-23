import logging

logger = logging.getLogger(__name__)


class Configs:
    def __init__(self, is_prod):
        """False -> Dev , True -> Production"""
        self.__load_variables(is_prod)

    def __load_variables(self, is_prod):
        self.is_prod = is_prod

        self.podio_client_id = 100
        self.podio_client_secret = 200

        logger.error(f"Successfully loaded env variables for {'PROD' if self.is_prod else 'DEV'} environment")
