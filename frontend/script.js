function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showRisk);
  } else {
    alert("Geolocation not supported");
  }
}

function showRisk(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;

  fetch(`http://127.0.0.1:5000/risk?lat=${lat}&lon=${lon}`)
    .then(res => res.json())
    .then(data => {
      document.getElementById("output").innerHTML = `
        <p><strong>Risk Score:</strong> ${data.risk_score}</p>
        <p><strong>Risk Level:</strong> ${data.risk_level}</p>
        <p>Routes will be adjusted accordingly.</p>
      `;
    });
}
