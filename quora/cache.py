import logging

logger = logging.getLogger(__name__)


def cache(cache_exp=None):
    def decorator(func):
        async def _wrapper(user, *args, **kwargs):
            key = f"pyquora_{func.__name__}_{user.username}"
            if user._cache is not None:
                value = user._cache.get(key)
                if value is not None:
                    logger.info(f"Using cache from {key}")
                    return value
            res = await func(user, *args, **kwargs)
            if user._cache is not None:
                time = 0
                if kwargs.get("cache_exp"):
                    time = kwargs.get("cache_exp")
                elif user._cache_exp:
                    time = user._cache_exp
                elif cache_exp:
                    time = cache_exp
                logger.info(f"Storing cache into {key} will expire in {time} seconds")
                user._cache.set(key, res, time=time)
            return res

        return _wrapper

    return decorator
