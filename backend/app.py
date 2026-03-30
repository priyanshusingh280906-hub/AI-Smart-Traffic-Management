from flask import Flask, render_template, jsonify
import threading
import time
import random

app = Flask(__name__)

# Global dictionary to store the 'live' state of your city
traffic_system = {
    "lanes": {
        "south": 41,
        "east": 28,
        "north": 15,
        "west": 10
    },
    "emergency_active": False,
    "recommendation": "Maintain Current Flow"
}

def calculate_green_time(count):
    return min(10 + (count * 2), 60)

# This function runs in the background and simulates traffic movement
def mock_traffic_engine():
    global traffic_system
    while True:
        if not traffic_system["emergency_active"]:
            # Randomly fluctuate car counts
            traffic_system["lanes"]["south"] += random.randint(-2, 2)
            traffic_system["lanes"]["east"] += random.randint(-2, 2)
            
            # Ensure numbers stay realistic (between 5 and 60)
            for lane in traffic_system["lanes"]:
                traffic_system["lanes"][lane] = max(5, min(60, traffic_system["lanes"][lane]))
            
            # Simple AI logic: Which lane is busiest?
            busiest = max(traffic_system["lanes"], key=traffic_system["lanes"].get)
            traffic_system["recommendation"] = f"Prioritize {busiest.capitalize()} Lane"
        
        time.sleep(3) # Update every 3 seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stats')
def get_stats():
    return jsonify(traffic_system)

@app.route('/trigger_emergency')
def trigger_emergency():
    traffic_system["emergency_active"] = True
    traffic_system["recommendation"] = "EMERGENCY DETECTED: GREEN CORRIDOR ACTIVE"
    
    # Threaded timer to reset after 10 seconds
    def reset_emergency():
        time.sleep(10)
        traffic_system["emergency_active"] = False
        
    threading.Thread(target=reset_emergency).start()
    return jsonify({"status": "Emergency Mode Activated"})

if __name__ == '__main__':
    # Start the mock engine thread before starting Flask
    threading.Thread(target=mock_traffic_engine, daemon=True).start()
    app.run(debug=True, port=5000)