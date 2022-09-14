"""API for calling premier league stats and possibly for more leagues"""
from .client import APIClient
from .meta_competitions import create_competitions_file
from .errors import EmptyResponse
from .competitions import *

__version__ = "2.0.0"

__all__ = ["APIClient", "__version__", "EmptyResponse", "create_competitions_file"]
