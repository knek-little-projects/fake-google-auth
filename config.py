import logging
import yaml
import pymongo
import os


config = yaml.safe_load(open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.yaml")).read())
logging.basicConfig(
    level=getattr(logging, config["logging"]["level"]),
    format=config["logging"]["format"],
    datefmt=config["logging"]["datefmt"])
db = pymongo.MongoClient(config["mongo"]["address"])[config["mongo"]["database"]][config["mongo"]["prefix"]]
