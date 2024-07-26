import atexit
import json
import logging.config
import logging.handlers
import pathlib
from logging.handlers import QueueListener
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class HasQueueListener(Protocol):
    listener: QueueListener


logger = logging.getLogger("my_app")  # __name__ is a common choice


def setup_logging() -> None:
    config_file = pathlib.Path("config/logging/queued-stderr-json-file.json")
    with open(config_file) as f_in:
        config: dict[str, Any] = json.load(f_in)

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None and isinstance(queue_handler, HasQueueListener):
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)


def main() -> None:
    setup_logging()
    logging.basicConfig(level="INFO")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        _ = 1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")
    logger.info("Message after exception that was caught")


if __name__ == "__main__":
    main()
