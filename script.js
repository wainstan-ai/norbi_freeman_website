document.getElementById('contact-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    
    const message = document.getElementById('message').value;
    
    const response = await fetch('http://localhost:8000/api/message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    });
    
    const result = await response.json();
    document.getElementById('response').innerText = result.status;
});