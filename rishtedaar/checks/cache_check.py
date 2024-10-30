import warnings


def check_cache(cache_alias='default', test_key='health_check_key', test_value='health_check_value'):
    from django.core.cache import caches
    from django.core.cache.backends.base import CacheKeyWarning
    try:
        warnings.simplefilter("ignore", CacheKeyWarning)
        cache = caches[cache_alias]
        # Try to perform a simple get operation; no need to set a new key
        cache.get('_health_check')  # A non-intrusive check
        return True, "Cache is healthy"
    except Exception as e:
        return False, f"Cache error: {str(e)}"
