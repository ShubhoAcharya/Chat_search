const chatHistory = document.getElementById('chatHistory');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

function addUserMessage(message) {
    const userMessage = document.createElement('div');
    userMessage.classList.add('chat-message', 'user-message');
    userMessage.textContent = message;
    chatHistory.appendChild(userMessage);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function addBotMessage(message) {
    const botMessage = document.createElement('div');
    botMessage.classList.add('chat-message', 'bot-message');
    botMessage.textContent = message;
    chatHistory.appendChild(botMessage);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function handleUserInput() {
    const message = userInput.value.trim();
    if (message !== '') {
        addUserMessage(message);
        // Replace the following line with your chatbot logic
        // In this example, we're simply displaying a placeholder bot response
        setTimeout(() => addBotMessage('Hi! I am a Chatbot. How can I assist you?'), 1000);
        userInput.value = '';
    }
}

sendBtn.addEventListener('click', handleUserInput);
userInput.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        handleUserInput();
    }
});
