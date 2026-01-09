from datetime import datetime


class LogEvent:
    VALID_SEVERITIES = {"INFO", "WARN", "ERROR"}
    
    def __init__(self, timestamp: datetime, system: str, severity: str, message: str):
        if severity not in self.VALID_SEVERITIES    :
            raise ValueError(f"Invalid severity: {severity}")
        
        self.timestamp = timestamp
        self.system = system
        self.severity = severity
        self.message = message
    
    def __repr__(self) -> str:
        return (
            f"LogEvent(timestamp={self.timestamp}, "
            f"system={self.system}, "
            f"severity={self.severity}, "
            f"message={self.message})"
        )
        
        