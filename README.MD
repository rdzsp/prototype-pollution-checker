# Prototype Pollution Checker

Prototype Pollution Checker is a security tool designed to detect potential Prototype Pollution vulnerabilities on target URLs by injecting payloads and verifying responses. This tool uses Selenium to automate browser interactions and concurrently checks multiple URLs for vulnerabilities.

## Features

- **Headless Chrome Testing**: Runs checks in a headless Chrome browser for efficient scanning.
- **Payload Injection**: Utilizes payloads to check for signs of prototype pollution vulnerabilities.
- **Concurrent Scanning**: Supports multithreading for faster scanning using `concurrent.futures`.
- **Simple Input and Output**: Accepts URLs from standard input, making it easy to integrate with other command-line tools.

## Installation

### Prerequisites

- **Python 3.7+**
- **Google Chrome** (Headless mode enabled)
- **ChromeDriver** compatible with your version of Chrome
- **Selenium**: You can install it via pip:

    ```bash
    pip install selenium
    ```

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/Prototype-Pollution-Checker.git
    cd Prototype-Pollution-Checker
    ```

2. Ensure `ChromeDriver` is in your PATH or specify its path in the code.

## Usage

1. **Prepare your URLs**: Save the URLs to check in a text file (e.g., `urls.txt`), each URL on a new line.
2. **Payloads**: Customize `payloads.txt` with payloads used to test for prototype pollution vulnerabilities.

3. **Run the tool**:

    ```bash
    cat urls.txt | python check.py
    ```

### Example

```bash
cat urls.txt | python check.py
