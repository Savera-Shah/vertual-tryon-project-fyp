function uploadPhoto() {
    const fileInput = document.getElementById('photoInput');
    const formData = new FormData();
    formData.append('photo', fileInput.files[0]);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById('preview').src = data.image_url;
    });
}

function sendMessage() {
    const message = document.getElementById('chatInput').value;

    fetch('/chatbot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        const chatbox = document.getElementById('chatbox');
        chatbox.innerHTML += "<p><b>You:</b> " + message + "</p>";
        chatbox.innerHTML += "<p><b>Bot:</b> " + data.reply + "</p>";
    });
}
