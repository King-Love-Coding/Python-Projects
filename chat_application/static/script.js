const socket = io();

let username = '';
let selectedAvatar = '';
let typingTimeout; // Timeout for typing indicator

// Function to select an avatar
function selectAvatar(url) {
    selectedAvatar = url;
    document.getElementById('avatar').value = ''; // Clear the custom avatar URL if any
}

// Function to start the chat
function startChat() {
    const nameInput = document.getElementById('username').value;
    const avatarInput = document.getElementById('avatar').value;
    document.getElementById('messageInput').focus();

    if (!nameInput.trim()) {
        alert('Please enter your name.');
        return;
    }

    username = nameInput;
    selectedAvatar = avatarInput || selectedAvatar || 'default-avatar.png'; // Fallback avatar

    // Hide user info and show chat room
    document.getElementById('userInfo').style.display = 'none';
    document.getElementById('chatRoom').style.display = 'block';

    // Emit join event
    socket.emit('join_chat', { username, avatar: selectedAvatar });
}

// Listen for incoming messages
socket.on('receive_message', function(data) {
    displayMessage(data);
});

// Function to send a message
function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const messageText = messageInput.value.trim();

    if (messageText) {
        const messageData = {
            message: messageText,
            username: username,
            avatar: selectedAvatar,
            delivered: true // Include delivered status here
        };
        socket.emit('send_message', messageData); // Emit the message to the server
        messageInput.value = ''; // Clear input

        // Stop typing indicator after sending the message
        stopTyping();
    }
}

// Send uploaded media file
function sendMedia(input) {
    const file = input.files[0];
    if (file) {
        // Restrict file size (e.g., 2MB for WebSocket)
        const maxSize = 2 * 1024 * 1024;

        // Check if the file size exceeds the limit
        if (file.size > maxSize) {
            alert('File is too large for direct sharing. Uploading to server...');

            // Create FormData for the HTTP upload
            const formData = new FormData();
            formData.append('file', file);
            formData.append('username', username);
            formData.append('avatar', selectedAvatar);

            // Send via HTTP POST to Flask server
            fetch('/upload_media', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Emit the media link to the chat
                const mediaData = {
                    media: data.url, // URL of the uploaded file
                    filename: file.name,
                    username: username,
                    avatar: selectedAvatar,
                    delivered: true
                };
                socket.emit('send_message', mediaData); // Emit the media link to the server
            })
            .catch(error => console.error('Error uploading file:', error));
        } else {
            // Handle smaller files with base64 encoding
            const reader = new FileReader();
            reader.onload = function(event) {
                const mediaData = {
                    media: event.target.result, // Base64 encoded media data
                    filename: file.name,
                    username: username,
                    avatar: selectedAvatar,
                    delivered: true
                };
                socket.emit('send_message', mediaData); // Emit the media data to the server
            };
            reader.readAsDataURL(file);
        }
    }
}

// Display the received message
function displayMessage(data) {
    const messagesContainer = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    const isSent = data.username === username;

    messageDiv.className = isSent ? 'message user-message' : 'message received-message';

    // Check if the message is media
    let content;
    if (data.media) {
        const isImage = /\.(jpeg|jpg|gif|png)$/i.test(data.media);
        const isAudio = /\.mp3$/i.test(data.media);
        const isVideo = /\.mp4$/i.test(data.media);

        if (isImage) {
            content = `<img src="${data.media}" alt="Image" class="media">`;
        } else if (isAudio) {
            content = `<audio controls src="${data.media}"></audio>`;
        } else if (isVideo) {
            content = `<video controls src="${data.media}"></video>`;
        } else {
            // For non-media files, set the link to download
            content = `<a href="${data.media}" download="${data.filename}">${data.filename}</a>`;
        }
    } else {
        content = `<span>${data.message}</span>`;
    }

    messageDiv.innerHTML = `
        <img src="${data.avatar || 'default-avatar.png'}" class="avatar">
        <div class="message-content">
            <span class="user-message-name">${data.username}</span>
            ${content}
            <span class="timestamp">${data.timestamp || ''}</span>
            <span class="read-status">${data.delivered ? '(Delivered)' : ''}</span>
        </div>
    `;

    messagesContainer.appendChild(messageDiv);
    messagesContainer.scrollTop = messagesContainer.scrollHeight; // Auto-scroll to bottom
}

// Send message on Enter key press
document.getElementById('messageInput').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

const messageInput = document.getElementById('messageInput');
messageInput.addEventListener('input', () => {
    clearTimeout(typingTimeout);

    if (messageInput.value) {
        socket.emit('typing', { username });
    } else {
        socket.emit('stop_typing', { username });
    }

    typingTimeout = setTimeout(() => {
        socket.emit('stop_typing', { username });
    }, 1000);
});

socket.on('display_typing', (data) => {
    document.getElementById('typingIndicator').innerText = `${data.username} is typing...`;
    document.getElementById('typingIndicator').style.display = 'block';
});

socket.on('hide_typing', () => {
    hideTypingIndicator();
});

function hideTypingIndicator() {
    document.getElementById('typingIndicator').style.display = 'none';
}


// Listen for message read updates
socket.on('update_read_status', function(data) {
    const messagesContainer = document.getElementById('messages');
    const messageDivs = messagesContainer.getElementsByClassName('message-container');

    for (let i = 0; i < messageDivs.length; i++) {
        const messageDiv = messageDivs[i];
        const usernameElement = messageDiv.querySelector('.user-message-name');
        if (usernameElement && usernameElement.innerText === data.username) {
            const readStatusElement = messageDiv.querySelector('.read-status');
            readStatusElement.innerText = '(Read)'; // Update the read status
            break;
        }
    }
});
