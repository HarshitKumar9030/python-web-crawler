import time
import logging


def handle_error(exception, url):
    logging.error(f"Error occurred while fetching {url}: {exception}")


def apply_rate_limit(rate_limit):
    time.sleep(60 / rate_limit['requests_per_minute'])


def load_config(file_path):
    import yaml
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
