function sendEvent(type) {
  fetch('/track', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      user_id: "user_001",
      event_type: type,
      page: window.location.pathname,
      timestamp: new Date().toISOString()
    })
  }).then(response => response.json())
    .then(data => console.log(data));
}
