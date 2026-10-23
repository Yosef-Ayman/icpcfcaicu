from datetime import datetime

def is_valid_datetime(dt_string, dt_format="%Y-%m-%dT%H:%M:%S"):
    if not dt_string:
        return False
    try:
        datetime.strptime(dt_string, dt_format)
        return True
    except ValueError:
        return False

def validate_event_duration(starts_at_str, ends_at_str):
    dt_format = "%Y-%m-%dT%H:%M:%S"
    
    # Check for missing values
    if not starts_at_str:
        return None, "starts_at is required"
    if not ends_at_str:
        return None, "ends_at is required"
        
    # Validate format and real calendar bounds for starts_at
    try:
        parsed_start = datetime.strptime(starts_at_str, dt_format)
    except ValueError:
        return None, "Invalid starts_at format. Use YYYY-MM-DDTHH:MM:SS"
        
    # Validate format and real calendar bounds for ends_at
    try:
        parsed_end = datetime.strptime(ends_at_str, dt_format)
    except ValueError:
        return None, "Invalid ends_at format. Use YYYY-MM-DDTHH:MM:SS"
        
    # Check logical order
    if parsed_start >= parsed_end:
        return None, "starts_at must be earlier than ends_at"
        
    # Return cleanly parsed datetime objects if everything passes
    return {
        "starts_at": parsed_start,
        "ends_at": parsed_end
    }, None
