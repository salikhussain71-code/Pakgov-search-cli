# Custom exceptions for our project
# Made by Salik - CS50P Final

class EmptyQueryError(Exception):
    """Raised when user enters nothing"""
    pass

class FolderNotFoundError(Exception):
    """Raised when docs folder is missing"""
    pass