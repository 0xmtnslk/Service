class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.requests = {}
        self.max_requests = max_requests
        self.time_window = time_window
    
    def is_allowed(self, user_id):
        # Implementation for rate limiting
