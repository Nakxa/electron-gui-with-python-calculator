# Electron GUI with Python Calculator

This project is a simple calculator application built using Electron for the GUI and Python for the backend calculations. It demonstrates how to integrate Python scripts with an Electron application.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division
- Cross-platform desktop application (Windows, macOS, Linux)
- Python-powered calculations with Electron frontend

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Node.js (v12 or higher)
- Python (v3.6 or higher)
- npm (usually comes with Node.js)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Nakxa/electron-gui-with-python-calculator.git
   cd electron-gui-with-python-calculator
   ```

2. Install the Node.js dependencies:
   ```
   npm install
   ```

3. Install the Python dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application:

1. Start the Electron app:
   ```
   npm start
   ```

2. Use the calculator by entering two numbers and selecting an operator, then click "Calculate".

## Project Structure

- `main.js`: The main Electron process file
- `index.html`: The HTML file for the calculator UI
- `renderer.js`: The renderer process file for handling UI interactions
- `calculator.py`: The Python script for performing calculations
- `package.json`: Node.js project and dependency information
- `requirements.txt`: Python dependency information

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is open source and available under the [MIT License](LICENSE).


## Acknowledgements

- [Electron](https://www.electronjs.org/)
- [Python](https://www.python.org/)
