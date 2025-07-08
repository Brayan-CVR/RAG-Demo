import logging


def start_logger() -> None:
    """Initialize the basic configuration for the logging system.
    
    This function sets up the root logger with a basic configuration that includes:
    - Logging level: INFO (captures INFO, WARNING, ERROR and CRITICAL messages)
    
    Note:
        This should be called only once at the beginning of the application setup.
        Subsequent calls won't have any effect unless the logging system is reset.
    """    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name.
    
    Creates or retrieves a logger with the given name. The logger will inherit
    the configuration set by start_logger() if it has been called previously.
    
    Args:
        name (str): Name to identify the logger. Typically you would use __name__
            to automatically create loggers that match the module hierarchy.
            
    Returns:
        logging.Logger: Configured logger instance ready for use.
        
    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("This is an info message")
    """    
    logger = logging.getLogger(name)
    return logger