"""
submission_consumer.py

This script sets up a ZeroMQ subscriber to receive and process job submission data.

Usage:
1. Run this script using the command: `python submission_consumer.py`
2. Ensure pyzmq is installed (`pip install pyzmq`).
3. This script listens for incoming messages on port 5555.
"""

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://127.0.0.1:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')  # Subscribe to all messages

print("Listening for submissions...")

while True:
    message = socket.recv_json()
    print(f"Received submission: {message}")
    # Here you can process the submission data, e.g., store it in a database
