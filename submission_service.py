"""
submission_service.py

This Flask application provides endpoints for managing submission data.
It allows users to submit and retrieve data related to job submissions.

Endpoints:
- POST /submission: Submits a new job submission with the following fields:
  - title: Job title
  - specialty: Job specialty
  - city: City of the job
  - state: State of the job
  - salary: Salary for the job
  - years_of_experience: Required years of experience

- GET /submissions: Retrieves a list of all job submissions.

Usage:
1. Run this script using the command: `python submission_service.py`
2. Ensure Flask is installed (`pip install Flask`).
3. The server will start and be accessible at `http://127.0.0.1:5000` by default.

Notes:
- The application runs in debug mode for development purposes.
- Ensure all required fields are provided in the POST request.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

submissions = []

@app.route('/submission', methods=['POST'])
def add_submission():
    data = request.get_json()
    required_fields = ['title', 'specialty', 'city', 'state', 'salary', 'years_of_experience']
    
    # Check if all required fields are in the request data
    if not all(field in data for field in required_fields):
        return jsonify({"status": "Missing fields"}), 400
    
    # Add the submission data
    submissions.append(data)
    return jsonify({"status": "Submission successful"}), 201

@app.route('/submissions', methods=['GET'])
def get_submissions():
    return jsonify(submissions), 200

if __name__ == '__main__':
    app.run(debug=True)
