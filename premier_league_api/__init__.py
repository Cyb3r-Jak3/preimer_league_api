"""API for calling premier league stats and possibly for more leagues"""
from .client import APIClient
from .meta_competitions import create_competitions_file
from .errors import EmptyResponse
from .competitions import *

__version__ = "0.0.1-b"

__all__ = ["APIClient", "__version__", "EmptyResponse", "create_competitions_file"]
