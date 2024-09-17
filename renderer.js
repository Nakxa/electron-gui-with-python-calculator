const { spawn } = require('child_process');

document.getElementById('calculate').addEventListener('click', () => {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operator = document.getElementById('operator').value;

    const pythonProcess = spawn('python', ['calculator.py', num1, operator, num2]);

    pythonProcess.stdout.on('data', (data) => {
        document.getElementById('result').textContent = data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Error: ${data}`);
    });
});