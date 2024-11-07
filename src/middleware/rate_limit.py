from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

class RateLimiter:
    def __init__(self, requests_per_minute: int = 60):
        self.requests = {}
        self.limit = requests_per_minute

    async def __call__(self, request: Request, call_next):
        timestamp = time.time()
        client_ip = request.client.host
        
        if self._is_rate_limited(client_ip, timestamp):
            return JSONResponse(
                status_code=429,
                content={"error": "Rate limit exceeded"}
            )
        
        return await call_next(request)
