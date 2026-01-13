from datetime import datetime
from analyzer.models import LogEvent
from analyzer.filters import filter_by_severity, filter_by_system


def sample_events():
    return [
        LogEvent(datetime(2026, 1, 1, 8, 0), "PLC_1", "INFO", "Started"),
        LogEvent(datetime(2026, 1, 1, 8, 5), "PLC_1", "WARN", "Temp High"),
        LogEvent(datetime(2026, 1, 1, 8, 10), "PLC_2", "ERROR", "Sensor Failed"),
    ]

def test_filter_by_severity():
    events = sample_events()
    errors = filter_by_severity(events, "ERROR")
    
    assert len(errors) == 1
    assert errors[0].severity == "ERROR"
    

def test_filter_by_system():
    events = sample_events()
    plc1_events = filter_by_system(events, "PLC_1")
    
    assert len(plc1_events) == 2
    assert all(e.system == "PLC_1" for e in plc1_events)
    