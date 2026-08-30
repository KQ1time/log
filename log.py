# Logging
# version 0.0.1

from datetime import datetime

def create_log(log_type: str, event: str) -> str:
    now = datetime.now()
    new_time = now.replace(microsecond=0)

    return f"{log_type}: [{new_time}] {event}"

def write_log(log: str):
    with open("events.log", "a") as f:
        f.write(log)
        f.write("\n")

# Examples 
if __name__ == "__main__":
    new_log = create_log("INFO", "Program started")
    write_log(new_log)

    log_2 = create_log("INFO", "Program finished")
    write_log(log_2)
