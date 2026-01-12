from analyzer.models import LogEvent


def filter_by_severity(events: list[LogEvent], severity: str) -> list[LogEvent]:
        filtered = []
        
        for event in events:
            if event.severity == severity:
                filtered.append(event)
        
        return filtered
        

def filter_by_system(events: list[LogEvent], system: str) -> list[LogEvent]:
        return [event for event in events if event.system == system]