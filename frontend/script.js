lucide.createIcons();

let co2Saved = 0;
let fuelSaved = 0;

async function syncDashboard() {
    try {
        const res = await fetch('/get_stats');
        const data = await res.json();

        document.getElementById('count-south').innerText = data.lanes.south;
        document.getElementById('count-east').innerText = data.lanes.east;
        document.getElementById('recommendation-text').innerText = data.recommendation;
        
        // Update counters
        const avg = Math.round((data.lanes.south + data.lanes.east) / 2);
        document.getElementById('stat-vehicles').innerText = avg;

        co2Saved += (avg * 0.002);
        fuelSaved += (avg * 0.0008);
        
        document.getElementById('stat-co2').innerText = co2Saved.toFixed(2) + " kg";
        document.getElementById('stat-fuel').innerText = fuelSaved.toFixed(2) + " L";
        document.getElementById('stat-wait').innerText = Math.floor(avg / 1.2) + "%";

    } catch (err) { console.log("System offline..."); }
}

document.getElementById('demo-btn').addEventListener('click', () => {
    fetch('/trigger_emergency');
});

setInterval(syncDashboard, 1500);

function updateClock() {
    const now = new Date();
    const timeString = now.getHours().toString().padStart(2, '0') + ":" + 
                       now.getMinutes().toString().padStart(2, '0') + ":" + 
                       now.getSeconds().toString().padStart(2, '0');
    document.getElementById('live-clock').innerText = timeString;
}

// Update clock every second
setInterval(updateClock, 1000);
updateClock(); // Run once immediately