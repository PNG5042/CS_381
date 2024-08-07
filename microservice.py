import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    while True:
        # Wait for next request from client
        message = socket.recv_string()
        print(f"Received request: {message}")

        # Send reply back to client
        socket.send_string("Hello from the microservice!")

if __name__ == "__main__":
    main()
