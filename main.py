from analyzer.parser import parse_log_file
from analyzer.filters import(
    filter_by_severity,
    filter_last_n_minutes,
    sort_by_timestamp,
    filter_by_system
)
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description = "Analyze system log events")
    
    parser.add_argument(
        "--severity",
        type = str,
        help = "Filter events by severity (INFO, WARN, ERROR)"
    )
    
    parser.add_argument(
        "--system",
        type = str,
        help = "Filter events by system name (e.g., PLC_1, PLC_2)"
    )
    
    return parser.parse_args()
    
    

def main():
    args = parse_args()
    events = parse_log_file("sample_logs/events.csv")
     
#Adding the CLI tool below this
    if args.severity or args.system:
        if args.severity:
            events = filter_by_severity(events, args.severity)
    
    if args.system:
        if args.system:
            events = filter_by_system(events, args.system)
    
        print(f"\nEvents found: {len(events)}")
        for event in events:
            print(event)
        return
        
#Code before CLI Tool above was added          
    error_events = filter_by_severity(events, "ERROR")
    print(f"\nERROR events found: {len(error_events)}")
    for event in error_events:
        print(event)

    recent_events = filter_last_n_minutes(events, minutes=60)
    print(f"\nEvents in last 60 minutes: {len(recent_events)}")
    
    plc1_events = filter_by_system(events, "PLC_1")
    print(f"\nPLC1_events: {len(plc1_events)}")
    print("PLC1_Events:")
    for event in plc1_events:
        print(event)
    
    plc2_events = filter_by_system(events, "PLC_2")
    print(f"\nPLC2_events found: {len(plc2_events)}")
    for event in plc2_events:
        print(event)
    
    print("\nAll events:")
    sorted_events = sort_by_timestamp(events)
    for event in sorted_events:
        print(event)



if __name__ == "__main__":
    main()