def calculate_green_time(vehicle_count):
    """
    Logic: 
    - Base time: 10 seconds
    - Each vehicle adds 2 seconds
    - Max time: 60 seconds
    """
    base_time = 10
    additional_time = vehicle_count * 2
    total_time = min(base_time + additional_time, 60)
    return total_time

# Example Usage:
# If Lane A has 20 cars, it gets: 10 + (20*2) = 50 seconds.
# If Lane B has 2 cars, it gets: 10 + (2*2) = 14 seconds.