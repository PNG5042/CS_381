Restaurant Review Microservice
This project is a simple microservice that provides restaurant reviews in JSON format. The microservice is built with a Python backend and a React frontend. It enables users to send and receive restaurant reviews.

How to Use Backend
You can just navigate to the backend directory.
Create and populate requirements.txt with necessary dependencies.
Install the required Python packages using pip install -r requirements.txt.
Implement the review_service.py script.

How to Use Frontend
Navigate to the review-client directory.
Install the required Node.js packages using npm install.
Starting Backend Service

python review_service.py
Starting Frontend Service

npm start
API Reference
POST /review
Submits a restaurant review.

Request Body:
{
  "restaurant": "Restaurant Name",
  "review": "Your review message",
  "rating": 5
}
Response:
{
  "status": "Review submitted"
}
GET /reviews
Retrieves the list of restaurant reviews.

Response:
[
  {
    "restaurant": "Restaurant Name",
    "review": "Review message",
    "rating": 5
  },
  {
    "restaurant": "Another Restaurant",
    "review": "Another review message",
    "rating": 4
  }
]
Testing
You can utilize the test_review_service.py file as a reference for testing.
