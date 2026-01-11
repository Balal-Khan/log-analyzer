from datetime import datetime, timedelta
from analyzer.models import LogEvent


def filter_by_severity(
    events: list[LogEvent], severity: str) -> list[LogEvent]:
        return [event for event in events if event.severity == severity]


def filter_last_n_minutes(
    events: list[LogEvent], minutes: int) -> list[LogEvent]:
        cutoff = datetime.now() - timedelta(minutes=minutes)
        return [event for event in events if event.timestamp >= cutoff]


def sort_by_timestamp(
    events: list[LogEvent], descending: bool = False) -> list[LogEvent]:
        return sorted(events, key=lambda e: e.timestamp, reverse=descending)
        
        
def filter_by_system(
    events: list[LogEvent], system: str) -> list[LogEvent]:
        return[event for event in events if event.system == system]
        