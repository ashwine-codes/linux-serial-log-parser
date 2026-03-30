# Linux Serial Log Parser

A lightweight Python utility to parse UART/serial debug logs and convert raw text into structured CSV format for easier analysis.

Designed for embedded systems debugging by converting raw UART logs into structured, analyzable data.

---

## Features

- Reads UART/serial log files
- Extracts:
  - Timestamp
  - Log Level (INFO, WARN, ERROR)
  - Message
- Exports structured CSV output
- Supports CLI-based filtering (e.g., only WARN/ERROR logs)
- No external dependencies (pure Python)

---

## Key Concepts Used

- Command-line interface (CLI) using sys.argv
- Regular expressions (regex) for log parsing
- File handling and text processing
- CSV generation for structured data output

---

## Project Structure

linux-serial-log-parser/
├── README.md
├── requirements.txt
├── sample_logs/
│   └── uart_log.txt
├── src/
│   └── parser.py

---

## Sample Input

[2026-03-29 10:15:23] INFO System boot complete
[2026-03-29 10:15:25] WARN UART buffer nearing capacity
[2026-03-29 10:15:27] ERROR Sensor initialization failed
[2026-03-29 10:15:30] INFO Retrying sensor setup

---

## How It Works

The parser reads each log line and uses regex to extract:

- timestamp
- log level
- message

Example parsed format:

2026-03-29 10:15:23 | INFO | System boot complete

---

## Usage

Run parser (all logs):

python3 src/parser.py sample_logs/uart_log.txt

Run parser with filtering (WARN & ERROR only):

python3 src/parser.py sample_logs/uart_log.txt "WARN, ERROR"

---

## Output

CSV file is generated at:

output/parsed_logs.csv

Example output:

timestamp,level,message
2026-03-29 10:15:25,WARN,UART buffer nearing capacity
2026-03-29 10:15:27,ERROR,Sensor initialization failed

---

## Tech Stack

- Python 3
- Regex (re module)
- CSV module

---

## Use Case

Useful for:

- Embedded systems debugging
- Firmware log analysis
- Filtering critical logs (WARN/ERROR)
- Converting raw logs into structured format

---

## Future Improvements

- Live serial port reading (/dev/ttyUSB0)
- Support for more log formats
- Log statistics (INFO/WARN/ERROR counts)
- Visualization support

---

## Author

Ashwine  
https://github.com/ashwine-codes
