from flask import Flask, render_template, jsonify
import traci
import threading # Added to run simulation in background

app = Flask(__name__)

# --- YOUR PASTED CODE START ---
def calculate_green_time(count):
    # Basic logic: 10s base + 2s per car (max 60)
    return min(10 + (count * 2), 60)

import time
import random

# Global variable to store "simulated" data
traffic_data = {"lane_1": 0, "status": "Idle"}

def run_mock_simulation():
    global traffic_data
    traffic_data["status"] = "Running"
    
    while True:
        # Generate random vehicle counts to simulate real movement
        traffic_data["lane_1"] = random.randint(5, 45)
        
        # Calculate fake green time based on your logic
        green_time = calculate_green_time(traffic_data["lane_1"])
        
        print(f"Mock Sim: Detected {traffic_data['lane_1']} cars. Setting green for {green_time}s")
        
        time.sleep(2) # Update every 2 seconds

        
# --- YOUR PASTED CODE END ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_sim')
def start_sim():
    # Start the simulation in a background thread so the site doesn't freeze
    sim_thread = threading.Thread(target=run_simulation)
    sim_thread.start()
    return jsonify({"status": "Simulation started in background"})

if __name__ == '__main__':
    app.run(debug=True)