from flask import Flask, render_template, jsonify
import threading
import time
import random

app = Flask(__name__)

# --- GLOBAL SYSTEM STATE ---
# This dictionary holds the live data for your "Nexus AI" engine
nexus_state = {
    "lanes": {
        "south": 42,
        "east": 25,
        "north": 18,
        "west": 12
    },
    "stats": {
        "co2_saved": 0.0,
        "fuel_saved": 0.0,
        "efficiency": 0
    },
    "emergency_active": False,
    "recommendation": "OPTIMIZING FLOW"
}

# --- BACKEND LOGIC ---

def traffic_engine():
    """Background thread that simulates real-time traffic changes."""
    global nexus_state
    while True:
        if not nexus_state["emergency_active"]:
            # 1. Simulate vehicle movement (-3 to +3 cars every cycle)
            for lane in nexus_state["lanes"]:
                change = random.randint(-3, 3)
                nexus_state["lanes"][lane] = max(5, min(80, nexus_state["lanes"][lane] + change))

            # 2. Update AI Recommendation based on density
            busiest_lane = max(nexus_state["lanes"], key=nexus_state["lanes"].get)
            nexus_state["recommendation"] = f"PRIORITIZING {busiest_lane.upper()} NODE"

            # 3. Calculate Environmental Impact (Mock logic based on flow optimization)
            total_flow = sum(nexus_state["lanes"].values())
            nexus_state["stats"]["co2_saved"] += (total_flow * 0.0005)
            nexus_state["stats"]["fuel_saved"] += (total_flow * 0.0002)
            nexus_state["stats"]["efficiency"] = min(99, 70 + (total_flow // 10))

        time.sleep(2) # Updates every 2 seconds

# --- FLASK ROUTES ---

@app.route('/')
def index():
    """Serves the main dashboard."""
    return render_template('index.html')

@app.route('/get_stats')
def get_stats():
    """API endpoint for the frontend to fetch data."""
    return jsonify(nexus_state)

@app.route('/trigger_emergency')
def trigger_emergency():
    """Forces the system into Emergency Priority Mode."""
    nexus_state["emergency_active"] = True
    nexus_state["recommendation"] = "EMERGENCY OVERRIDE: GREEN CORRIDOR ACTIVE"
    
    # Auto-reset after 8 seconds of "Priority Green"
    def reset_timer():
        time.sleep(8)
        nexus_state["emergency_active"] = False
    
    threading.Thread(target=reset_timer).start()
    return jsonify({"status": "Priority Mode Engaged"})

if __name__ == '__main__':
    # Start the simulation engine in the background
    engine_thread = threading.Thread(target=traffic_engine, daemon=True)
    engine_thread.start()
    
    # Run the Flask Server
    app.run(debug=True, port=5000)