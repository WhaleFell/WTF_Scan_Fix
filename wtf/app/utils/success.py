from flask import jsonify
from loguru import logger


@logger.catch()
def success(data):
    # print(data)
    logger.info(data)
    return jsonify({"data": data, "status": True})
