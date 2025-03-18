document.getElementById("checkScam").addEventListener("click", async () => {
    const text = document.getElementById("userText").value;
    const resultElement = document.getElementById("result");

    if (!text.trim()) {
        resultElement.innerText = "Please enter some text!";
        return;
    }

    // Replace this with your hosted API URL
    const apiUrl = "http://127.0.0.1:5000/check-scam";

    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });
        const data = await response.json();

        resultElement.innerText = data.isScam ? "🚨 Scam Detected!" : "✅ Safe Message";
    } catch (error) {
        resultElement.innerText = "Error checking scam.";
    }
});
