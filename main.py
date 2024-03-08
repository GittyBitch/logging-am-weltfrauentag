import os
import sys
import logging

from fastapi import FastAPI
import uvicorn

appId = "Weltfrauentag.Logger"
defaultMsg = "What's up ?"

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def log_message(level, message):
    logger = logging.getLogger(appId)
    if (os.environ.get("LOG_LEVEL") ==  logging.getLevelName(level)):
        logger.log(level, message)

app = FastAPI()

@app.get("/info")
def read_info():
    log_message(logging.INFO, defaultMsg)
    sys.exit(0)
    return {"app": appId, "type": "info"}

@app.get("/debug")
def read_debug():
    log_message(logging.DEBUG, defaultMsg)
    sys.exit(0)
    return {"app": appId, "type": "debug", "debug_mode": "on"}

@app.get("/error")
def read_error():
    log_message(logging.ERROR, defaultMsg)
    sys.exit(0)
    return {"app": appId, "type": "error", "error_mode": "on"}

@app.get("/fatal")
def read_fatal():
    log_message(logging.FATAL, defaultMsg)
    sys.exit(0)
    return {"app": appId, "type": "fatal", "fatal_mode": "on"}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

