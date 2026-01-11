from analyzer.parser import parse_log_file
from analyzer.filters import(
    filter_by_severity,
    filter_last_n_minutes,
    sort_by_timestamp,
    filter_by_system
)



def main():
    events = parse_log_file("sample_logs/events.csv")
    
    error_events = filter_by_severity(events, "ERROR")
    print(f"ERROR events: {len(error_events)}")
    
    
    recent_events = filter_last_n_minutes(events, minutes=60)
    print(f"Events in last 60 minutes: {len(recent_events)}")
    
    plc1_events = filter_by_system(events, "PLC_1")
    print(f"PLC1_events: {len(plc1_events)}")
    print("\nPLC1_Events:")
    for event in plc1_events:
        print(event)
    
    print("\nAll events:")
    sorted_events = sort_by_timestamp(events)
    for event in sorted_events:
        print(event)



if __name__ == "__main__":
    main()