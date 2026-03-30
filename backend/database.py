import sqlite3

def log_traffic_data(lane_id, count, wait_time):
    conn = sqlite3.connect('traffic_stats.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS stats 
                     (timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                      lane_id TEXT, count INTEGER, wait_time INTEGER)''')
    
    cursor.execute("INSERT INTO stats (lane_id, count, wait_time) VALUES (?, ?, ?)", 
                   (lane_id, count, wait_time))
    conn.commit()
    conn.close()