"""Exception module for library."""


class PyQuoraException(Exception):
    """Base class for exceptions."""


class ProfileNotFoundError(PyQuoraException):
    """Specified Quora profile not found."""
