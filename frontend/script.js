// Initialize Icons
lucide.createIcons();

// Elements
const vehicleStat = document.getElementById('stat-vehicles');
const emergencyStat = document.getElementById('stat-emergency');
const southCount = document.getElementById('count-south');
const eastCount = document.getElementById('count-east');
const recText = document.getElementById('recommendation-text');
const emergencyLog = document.getElementById('emergency-log');
const demoBtn = document.getElementById('demo-btn');

// 1. Simulate Live Counting
setInterval(() => {
    // Random vehicle fluctuations
    let currentV = parseInt(vehicleStat.innerText);
    vehicleStat.innerText = currentV + (Math.floor(Math.random() * 3) - 1);
    
    let s = parseInt(southCount.innerText);
    southCount.innerText = s + (Math.floor(Math.random() * 3) - 1);
}, 3000);

// 2. Emergency Demo Trigger
demoBtn.addEventListener('click', () => {
    // Change UI to Alert Mode
    emergencyStat.innerText = "1";
    recText.innerText = "AMBULANCE DETECTED - OPENING SOUTH";
    emergencyLog.classList.add('emergency-active');
    
    // Alert Notification in Console
    console.log("Priority Override: Emergency Vehicle in Sector 4");

    // Reset after 6 seconds
    setTimeout(() => {
        emergencyStat.innerText = "0";
        recText.innerText = "Maintain Current Flow";
        emergencyLog.classList.remove('emergency-active');
    }, 6000);
});

// 3. Dynamic Wave Chart Animation
const wavePath = document.getElementById('wave-path');
let phase = 0;

function animateWave() {
    phase += 0.05;
    const d = `M0,80 Q40,${20 + Math.sin(phase)*10} 80,${70 + Math.cos(phase)*5} T160,50 T240,${90 + Math.sin(phase)*10} T320,30 T400,60`;
    wavePath.setAttribute('d', d);
    requestAnimationFrame(animateWave);
}

animateWave();