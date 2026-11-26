# Python System Uptime Checker

A lightweight Python application that monitors system uptime in real time and displays basic system information.

## Features

- Display system boot time.
- Monitor system uptime in real time.
- Show operating system information.
- Display CPU core count.
- Display CPU usage percentage.
- Automatically save uptime history to CSV.
- Refresh monitoring every second.

## Requirements

- Python 3.x
- psutil

## Installation

Clone this repository:

```bash
git clone https://github.com/pradipta-web/python-system-uptime-checker.git
```

Navigate to the project directory:

```bash
cd python-system-uptime-checker
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python app.py
```

Press `CTRL+C` to stop monitoring.

## CSV Logging

The application automatically generates:

```text
uptime_history.csv
```

The CSV file stores:
- Timestamp
- System Uptime (Seconds)

## Technologies Used

- Python
- psutil
- CSV

## License

This project is licensed under the MIT License.

## Author

**Kinervaaa**