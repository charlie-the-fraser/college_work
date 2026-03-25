import logging

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter("%(levelname)s: %(message)s")

file_handler = logging.FileHandler("logging_it.txt")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s::%(levelname)s::"
                                            "%(name)s::%(funcName)s::"
                                            "%(lineno)d::%(message)s"))

logger.addHandler(console_handler)
logger.addHandler(file_handler)

print(logger.critical("hello"))