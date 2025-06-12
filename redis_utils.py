import redis

r = redis.Redis(
    host='localhost',  # Connects to local Redis server
    port=6379,
    db=0,
    decode_responses=True
)

# Test connection
try:
    r.ping()
    print("Successfully connected to Redis!")
except redis.ConnectionError:
    print("Failed to connect to Redis.")

CACHE_HIT = 0
CACHE_MISS = 0

RATE_LIMIT = 3  # 3 per minute

def is_rate_limited(user_id):
    key = f"rate:{user_id}"
    current = r.incr(key)
    if current == 1:
        r.expire(key, 60)
    return current > RATE_LIMIT

def get_cached_response(query):
    global CACHE_HIT, CACHE_MISS
    if r.exists(query):
        CACHE_HIT += 1
        return r.get(query)
    CACHE_MISS += 1
    return None

def cache_response(query, answer):
    r.set(query, answer, ex=3600)

def clear_cache():
    r.flushdb()

def cache_stats():
    return CACHE_HIT, CACHE_MISS