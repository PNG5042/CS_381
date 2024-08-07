# Microservice Communication

## Communication Contract
**Request Data:**
- **Protocol:** ZeroMQ
- **Endpoint:** `tcp://localhost:5555`
- **Message Format:** String
- **Response:** String with a message

### Example Call

import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

socket.send_string("Request data")
message = socket.recv_string()
print(f"Received reply: {message}")
