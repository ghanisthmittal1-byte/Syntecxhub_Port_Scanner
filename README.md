# TCP Port Scanner

## Project Overview

The TCP Port Scanner is a Python-based cybersecurity project developed as part of the **Syntecxhub Cyber Security Internship Program**. It scans a target host to identify TCP ports that accept connections.

The project uses Python socket programming to check port connectivity and `ThreadPoolExecutor` to perform scanning tasks concurrently. It also uses logging to save scan results for future reference.

## Project Objectives

- Identify open TCP ports on a target host.
- Understand TCP/IP networking and port numbers.
- Implement socket programming using Python.
- Use concurrent execution to improve scanning efficiency.
- Record scan results in a log file.
- Handle connection timeouts and socket errors.
- Learn basic network reconnaissance techniques.

## Features

- **TCP Port Scanning:** Checks TCP ports on a specified host.
- **Multithreading:** Uses `ThreadPoolExecutor` to run multiple scanning tasks concurrently.
- **Custom Port Range:** Allows users to specify the starting and ending ports.
- **Configurable Timeout:** Sets the maximum waiting time for connection attempts.
- **Configurable Threads:** Allows users to control the number of concurrent workers.
- **Logging:** Saves scan results in `scan_results.log`.
- **Error Handling:** Handles hostname resolution errors and socket-related exceptions.
- **Command-Line Interface:** Accepts the target hostname or IP address and scanning options.

## Technologies Used

- Python 3
- Socket Programming
- TCP/IP Networking
- ThreadPoolExecutor
- Argparse
- Logging

## Project Structure

```text
Syntecxhub_Port_Scanner/
│
├── Syntecxhub_Port_Scanner__Ghanisth.py
├── README.md
└── scan_results.log
```

**File descriptions:**

- `Syntecxhub_Port_Scanner__Ghanisth.py` — Main Python program.
- `README.md` — Project documentation.
- `scan_results.log` — Log file generated when the scanner runs.

## Requirements

- Python 3.9 or later recommended.
- Visual Studio Code or another Python editor.
- Command Prompt, PowerShell, or a terminal.
- Authorization to scan the target system.

No third-party Python libraries are required.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/ghanisthmittal1-byte/Syntecxhub_Port_Scanner.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Syntecxhub_Port_Scanner
```

### Step 3: Run the Scanner

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1
```

This command scans TCP ports 1–1024 on the local computer.

## Usage

### 1. Scan the Local Computer

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1
```

The IP address `127.0.0.1` refers to the local computer.

### 2. Scan a Specific Port Range

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1 --start 20 --end 100
```

This command scans ports 20 through 100.

### 3. Change the Connection Timeout

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1 --timeout 1
```

This sets the connection timeout to one second.

### 4. Change the Number of Worker Threads

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1 --threads 100
```

This configures up to 100 concurrent worker threads.

### 5. Combine Scanning Options

```bash
python Syntecxhub_Port_Scanner__Ghanisth.py 127.0.0.1 --start 1 --end 100 --timeout 1 --threads 50
```

This scans ports 1–100 with a one-second timeout and 50 worker threads.

## Command-Line Arguments

| Argument | Description | Default |
|---|---|---|
| `host` | Target hostname or IP address | Required |
| `--start` | First port to scan | 1 |
| `--end` | Last port to scan | 1024 |
| `--timeout` | Connection timeout in seconds | 0.5 |
| `--threads` | Maximum number of concurrent workers | 50 |

Valid TCP port numbers range from 1 to 65535.

## Sample Output

```text
Scanning 127.0.0.1 (127.0.0.1)
Port range: 1-1024

Port 135: OPEN
Port 445: OPEN

Scan completed. Results saved to scan_results.log
```

*Note: This is illustrative output. Actual results depend on the services running on the target computer.*

## How It Works

1. The program accepts a hostname or IP address from the command line.
2. The hostname is converted into an IP address using `socket.gethostbyname()`.
3. The program creates TCP sockets to test the specified ports.
4. The `connect_ex()` method attempts to establish a TCP connection.
5. If the method returns `0`, the port is marked as `OPEN`.
6. In the current implementation, other return values are marked as `CLOSED`.
7. `ThreadPoolExecutor` manages concurrent scanning tasks.
8. The `logging` module records the scan results in `scan_results.log`.
9. The program completes after all submitted scanning tasks finish.

## Logging

The program uses Python's built-in `logging` module to record scanning results.

The log file contains timestamps, target addresses, port numbers, and scan statuses.

Example:

```text
2026-10-16 18:30:00 - 127.0.0.1:135 - OPEN
2026-10-16 18:30:01 - 127.0.0.1:136 - CLOSED
```

The entries above are examples, not actual scan results.

## Learning Outcomes

Through this project, I gained practical exposure to:

- TCP/IP networking and port numbers.
- Socket programming in Python.
- Concurrent task execution.
- Command-line argument handling.
- Exception handling.
- Logging and result recording.
- Basic network reconnaissance concepts.

## Limitations

- The scanner supports TCP ports only.
- It does not identify service versions.
- Firewalls and network filtering may affect results.
- Nonzero connection results are currently classified as `CLOSED`, although some failures may have other causes.
- The program does not generate a separate summary of all open, closed, and timed-out ports.

## Future Improvements

- Improve the classification of closed, filtered, and timed-out ports.
- Add a progress indicator and final scan summary.
- Export results to CSV or JSON.
- Identify common services running on open ports.
- Add unit tests and more detailed error handling.
- Improve the reporting interface.

## Ethical Considerations

This project is intended for educational purposes and authorized security testing.

Only scan systems and networks that you own or have explicit permission to test. Unauthorized scanning may violate applicable laws or organizational policies.

## Author

**GitHub Username:** [ghanisthmittal1-byte](https://github.com/ghanisthmittal1-byte)

**Project Repository:** [Syntecxhub_Port_Scanner](https://github.com/ghanisthmittal1-byte/Syntecxhub_Port_Scanner)

**Program:** Syntecxhub Cyber Security Internship Program

## License

This project is intended for educational and learning purposes.
