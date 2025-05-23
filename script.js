const startBtn = document.getElementById('start-btn');
const webhookInput = document.getElementById('webhook');
const logArea = document.getElementById('log');

startBtn.addEventListener('click', () => {
  const webhook = webhookInput.value.trim();
  if (!webhook) {
    alert('Please enter a valid webhook URL.');
    return;
  }
  logArea.textContent = '[INFO] Starting sniper...\n';
  fetch('/start?webhook=' + encodeURIComponent(webhook))
    .then(res => res.json())
    .then(data => {
      logArea.textContent += '[SUCCESS] ' + data.message + '\n';
    })
    .catch(() => {
      logArea.textContent += '[ERROR] Failed to start sniper backend.\n';
    });
});