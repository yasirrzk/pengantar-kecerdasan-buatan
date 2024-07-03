const startButton = document.getElementById('start');
const statusElement = document.getElementById('status');
const resultElement = document.getElementById('result');
const animationElement = document.getElementById('animation');

startButton.addEventListener('click', () => {
    animationElement.classList.remove('hidden');
    statusElement.textContent = 'Listening...';
    resultElement.textContent = '';

    fetch('/voice', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response JSON:', data); 
        statusElement.textContent = data.status;
        resultElement.textContent = data.text;
        animationElement.classList.add('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
        animationElement.classList.add('hidden');
    });
});