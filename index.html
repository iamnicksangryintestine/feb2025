<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surgery Updates</title>
    
    <!-- OneSignal Web Push SDK -->
    <script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async></script>
    <script>
        window.OneSignal = window.OneSignal || [];
        OneSignal.push(function() {
            OneSignal.init({
                appId: "${{ secrets.ONESIGNAL_APP_ID }}",  // Using GitHub Secret for OneSignal App ID
                notifyButton: {
                    enable: true  // Adds a notification opt-in button
                },
                allowLocalhostAsSecureOrigin: true
            });

            // Auto-prompt users when they visit the site
            OneSignal.push(function() {
                OneSignal.showNativePrompt();
            });
        });
    </script>

    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }
        .update-container { max-width: 600px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 10px; }
        h1 { color: #333; }
        .timestamp { color: gray; font-size: 0.9em; }
    </style>
</head>
<body>

    <h1>Surgery Updates</h1>
    <div class="update-container">
        <h2 id="status">Loading latest update...</h2>
        <p id="timestamp" class="timestamp"></p>
    </div>

    <script>
        async function fetchUpdate() {
            try {
                let response = await fetch('${{ secrets.WEBPAGE_URL }}');  // Using GitHub Secret for Webpage URL
                let data = await response.json();
                document.getElementById('status').textContent = data.status;
                document.getElementById('timestamp').textContent = "Last updated: " + data.timestamp;
            } catch (error) {
                document.getElementById('status').textContent = "Unable to load updates.";
            }
        }
        fetchUpdate();
        setInterval(fetchUpdate, 60000); // Refresh every minute
    </script>

</body>
</html>
