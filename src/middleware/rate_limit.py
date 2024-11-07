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
def _is_rate_limited(self, client_ip: str, timestamp: float) -> bool:
        # Clean up old requests
        self._cleanup_old_requests(timestamp)
        
        # Get or initialize client's request history
        client_requests = self.requests.get(client_ip, [])
        
        # Add current request timestamp
        client_requests.append(timestamp)
        self.requests[client_ip] = client_requests
        
        # Check if request count exceeds limit
        return len(client_requests) > self.limit
    
    def _cleanup_old_requests(self, current_timestamp: float) -> None:
        # Remove requests older than 1 minute
        cutoff = current_timestamp - 60
        
        for ip in list(self.requests.keys()):
            self.requests[ip] = [
                ts for ts in self.requests[ip] 
                if ts > cutoff
            ]
            
            # Remove empty entries
            if not self.requests[ip]:
                del self.requests[ip]
