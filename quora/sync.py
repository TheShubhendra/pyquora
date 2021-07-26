import asyncio
import inspect
import functools
from .user import User


def _syncify_wrapper(type, method_name):
    method = getattr(type, method_name)

    @functools.wraps(method)
    def _wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        coro = method(*args, **kwargs)
        if loop.is_running():
            return coro
        else:
            return loop.run_until_complete(coro)

    setattr(type, method_name, _wrapper)


def syncify(*types):
    for i in types:
        for m in dir(i):
            if not m.startswith("_") and inspect.iscoroutinefunction(getattr(i, m)):
                _syncify_wrapper(i, m)


syncify(User)

__all__ = [
    "User",
]
