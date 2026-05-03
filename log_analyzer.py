import time
from sklearn.ensemble import IsolationForest

# Store numeric log data
data = []

# AI model
model = IsolationForest(contamination=0.3)

# Track processed lines
last_position = 0


def convert_to_number(line):
    if "ERROR" in line:
        return 3
    elif "WARNING" in line:
        return 2
    else:
        return 1


def print_clean_output(line, is_anomaly=False):
    if is_anomaly:
        print(f"[ANOMALY] {line}")
    elif "ERROR" in line:
        print(f"[ERROR] {line}")
    elif "WARNING" in line:
        print(f"[WARNING] {line}")
    else:
        print(f"[INFO] {line}")


while True:
    with open("app.log", "r") as file:
        lines = file.readlines()

        # Read only new logs
        new_lines = lines[last_position:]
        last_position = len(lines)

        for line in new_lines:
            line = line.strip()
            num = convert_to_number(line)

            data.append([num])

            if len(data) > 5:
                model.fit(data)
                prediction = model.predict([[num]])

                if prediction[0] == -1:
                    print_clean_output(line, True)
                    with open("anomalies.log", "a") as anomaly_file:
                        anomaly_file.write(line + "\n")
                else:
                    print_clean_output(line)
            else:
                print(f"[TRAINING] {line}")
time.sleep(2)