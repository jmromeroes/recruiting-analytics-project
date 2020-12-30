class RepositoryException(Exception):
    pass

class NotFoundRepositoryException(RepositoryException):
    pass

class DuplicatedRepositoryException(RepositoryException):
    pass