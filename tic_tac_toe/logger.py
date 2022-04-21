"""Logger"""
import yaml
import logging.config


with open("config.yaml", 'r') as file:
    config = yaml.safe_load(file.read())
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)
