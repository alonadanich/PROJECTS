import queue
import random
import time

request_queue = queue.Queue()

request_id = 0

def generate_request():
    global request_id
    request_id += 1
    new_request = f"Request-{request_id}"
    request_queue.put(new_request)
    print(f"Generated: {new_request}")

def process_request():
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"Processing: {current_request}")
        time.sleep(random.uniform(0.5, 2))
        print(f"Completed: {current_request}")
    else:
        print("Queue is empty. No requests to process.")

def main():
    try:
        while True:
            if random.random() < 0.7:
                generate_request()
            process_request()
            time.sleep(random.uniform(0.5, 1.5))
    except KeyboardInterrupt: #Ctrl+C
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()