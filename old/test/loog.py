import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set the logging level

# Create a logger
logger = logging.getLogger(__name__)

# Log messages
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
