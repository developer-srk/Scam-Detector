async function checkForScam() 
{
    const inputText = document.getElementById('inputText').value;
    const resultDiv = document.getElementById('result');
    
    if (inputText.trim() === "") 
        {
        resultDiv.textContent = "Please enter some text to check.";
        return;
    }

    resultDiv.textContent = "Checking for scam...";

    // Send the input to the backend
    const response = await fetch('/check-scam', 
        {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    });

    const data = await response.json();

    if (data.isScam) 
    {
        resultDiv.textContent = "This text is likely a scam!";
    } else 
    {
        resultDiv.textContent = "This text appears to be safe.";
    }
}
