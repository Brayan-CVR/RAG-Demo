import logging


def start_logger() -> None:
    """_summary_
    """    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def get_logger(name: str) -> logging.Logger:
    """_summary_

    Args:
        name (str): _description_

    Returns:
        logging.Logger: _description_
    """    
    logger = logging.getLogger(name)
    return logger