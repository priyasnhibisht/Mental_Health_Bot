async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return; // Prevent sending empty messages

    // Display user message in chat box
    appendMessage('You: ' + userInput);
    document.getElementById('user-input').value = ''; // Clear input field

    // Send message to the server
    try {
        const response = await fetch('http://localhost:5000/chat', { // Adjust the URL if needed
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userInput })
        });

        const data = await response.json();
        if (response.ok) {
            appendMessage('Bot: ' + data.bot_response);
        } else {
            appendMessage('Bot: ' + data.error);
        }
    } catch (error) {
        appendMessage('Bot: An error occurred. Please try again later.');
        console.error('Error:', error);
    }
}

function appendMessage(message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.textContent = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom of the chat
}
