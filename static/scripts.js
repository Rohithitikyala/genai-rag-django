// Send message function
function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (message === "") return;

    // Show user message
    addMessage(message, "user");
    input.value = "";

    fetch("/chat_api/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken")
    },
    body: JSON.stringify({
        message: message,
        sessionId: "default"
    })
})
.then(async (response) => {
    const text = await response.text();

    if (!response.ok) {
        throw new Error("Server error: " + text);
    }

    try {
        return JSON.parse(text);
    } catch (e) {
        throw new Error("Invalid JSON response: " + text);
    }
})
.then(data => {
    if (data.reply) {
        addMessage(data.reply, "bot");
    } else if (data.error) {
        addMessage("Server error: " + data.error, "bot");
    } else {
        addMessage("Unexpected server response.", "bot");
    }
})
.catch(error => {
    console.error("Fetch Error:", error);
    addMessage("Server connection failed.", "bot");
});
}
