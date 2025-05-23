
function logMessage(message) {
    const log = document.getElementById('log');
    log.textContent += message + '\n';
    log.scrollTop = log.scrollHeight;
}
function startSniping() {
    const webhook = document.getElementById('webhook').value;
    if (!webhook.startsWith('http')) {
        alert("Please enter a valid Webhook URL.");
        return;
    }
    logMessage("🔧 Starting sniping tool...");
    logMessage("✅ Tool by KHALID | UI loaded.");
    logMessage("❗ For full functionality, run backend on Python.");
}
