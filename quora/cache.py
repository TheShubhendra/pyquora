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
                time = user._cache_exp
                if time is None:
                    time = cache_exp
                cache_exp = kwargs.get("cache_exp")
                if cache_exp is not None:
                    time = cache_exp
                logger.info(f"Storing cache into {key} will expire in {time} seconds")
                user._cache.set(key, res, time=time)
            return res

        return _wrapper

    return decorator
