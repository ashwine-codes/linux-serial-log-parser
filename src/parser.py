import sys
import re
import csv


def read_log_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def parse_line(line):
    pattern = r"\[(.*?)\]\s+(INFO|WARN|ERROR)\s+(.*)"
    match = re.match(pattern, line)

    if match:
        timestamp = match.group(1)
        level = match.group(2)
        message = match.group(3)
        return timestamp, level, message

    return None


def write_to_csv(parsed_data, output_file):
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "level", "message"])
        writer.writerows(parsed_data)


def should_include_log(level, selected_levels):
    return level in selected_levels


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/parser.py <log_file_path> [log_levels]")
        print("Example: python3 src/parser.py sample_logs/uart_log.txt WARN,ERROR")
        return

    file_path = sys.argv[1]

    if len(sys.argv) >= 3:
        selected_levels = [level.strip() for level in sys.argv[2].split(",")]
    else:
        selected_levels = ["INFO", "WARN", "ERROR"]

    output_file = "output/parsed_logs.csv"
    lines = read_log_file(file_path)
    parsed_data = []

    for line in lines:
        line = line.strip()
        parsed = parse_line(line)

        if parsed:
            timestamp, level, message = parsed

            if should_include_log(level, selected_levels):
                parsed_data.append((timestamp, level, message))
        else:
            print(f"Skipping invalid line: {line}")

    write_to_csv(parsed_data, output_file)
    print(f"CSV file created: {output_file}")
    print(f"Included log levels: {selected_levels}")


if __name__ == "__main__":
    main()
