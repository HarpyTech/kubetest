import os
import sys
import redis
import time

host = os.getenv("REDIS_HOST", "redis-service")
port = int(os.getenv("REDIS_PORT", "6379"))
password = os.getenv("REDIS_PASSWORD")

def fail(msg, code=1):
    print(msg)
    sys.exit(code)

if not password:
    fail("Missing REDIS_PASSWORD env var")

# Simple retry loop for startup races
for attempt in range(1, 6):
    try:
        r = redis.Redis(host=host, port=port, password=password, socket_timeout=3)
        r.ping()
        r.set("test-key", "Hello Redis!")
        val = r.get("test-key")
        print(f"Redis connection successful (attempt {attempt}), value: {val.decode()}")
        sys.exit(0)
    except Exception as e:
        print(f"Attempt {attempt} failed: {e}")
        time.sleep(2)

fail("Redis connection failed after 5 attempts")
