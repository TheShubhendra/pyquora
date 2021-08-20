import logging

logger = logging.getLogger(__name__)


def cache(func):
    async def _wrapper(user, *args, **kwargs):
        key = f"pyquora_{func.__name__}_{user.username}"
        if user._cache is not None:
            value = user._cache.get(key)
            if value is not None:
                logger.info(f"Using cache from {key}")
                return value
        res = await func(user, *args, **kwargs)
        if user._cache is not None:
            logger.info(f"Storing cache into {key}")
            user._cache.set(key, res)
        return res

    return _wrapper
