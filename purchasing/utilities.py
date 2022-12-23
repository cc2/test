import logging

logger = logging.getLogger(__name__)


class Utilities:
    def a():
        logger.info("from Utilities")
        logger.info(configs.is_prod)
        logger.info(configs.podio_client_id)
