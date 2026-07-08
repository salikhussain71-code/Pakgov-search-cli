class EmptyQueryError(Exception):
    """Raised when user enters empty keyword"""
    pass


class FolderNotFoundError(Exception):
    """Raised when docs folder is missing"""
    pass
