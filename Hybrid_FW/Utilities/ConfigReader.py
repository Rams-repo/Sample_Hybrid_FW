from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("Hybrid_FW/Configuration/config.ini")
    return config.get(category, key)
