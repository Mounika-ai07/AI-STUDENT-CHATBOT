async function sendMessage() {

    let input = document.getElementById("user-input");

    let message = input.value;

    if(message === "") return;

    let chatBox = document.getElementById("chat-box");

    // USER MESSAGE
    let userMessage = document.createElement("p");

    userMessage.innerHTML = "🧑 You: " + message;

    chatBox.appendChild(userMessage);

    // SEND TO FLASK
    let response = await fetch("/get", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            message: message
        })
    });

    let data = await response.json();

    // BOT MESSAGE
    let botMessage = document.createElement("p");

    botMessage.innerHTML = "🤖 Bot: " + data.reply;

    chatBox.appendChild(botMessage);

    input.value = "";
}