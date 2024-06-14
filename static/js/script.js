document.getElementById('start').addEventListener('click', () => {
    const statusElement = document.getElementById('status');
    const resultElement = document.getElementById('result');

    statusElement.textContent = 'Mendengarkan...';

    fetch('/voice', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        statusElement.textContent = data.status;
        resultElement.textContent = data.text;
    })
    .catch(error => {
        console.error('Error:', error);
        statusElement.textContent = 'Terjadi kesalahan';
    });
});
