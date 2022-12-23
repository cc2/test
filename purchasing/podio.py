import logging

logger = logging.getLogger(__name__)


class PodioOrderItem:
    def __init__(self):
        raise TypeError(f"must be instantiated from a classmethod")

    @classmethod
    def fromPodioItemJson(cls, item_json: str):
        """>>> I WANT TO HAVE ACCESS TO CONFIGS OBJECT INITIATED IN MAIN"""
        logger.info("from PodioOrderItem")
        logger.info(configs.podio_client_id)
        ob = cls.__new__(cls)
        return ob
