import zmq

def main():
    context = zmq.Context()

    # Create a socket to communicate with the server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send a request
    socket.send_string("Request data")

    # Receive the reply
    message = socket.recv_string()
    print(f"Received reply: {message}")

if __name__ == "__main__":
    main()
