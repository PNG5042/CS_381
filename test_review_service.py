import unittest
import requests

class TestSubmissionService(unittest.TestCase):
    BASE_URL = 'http://localhost:5000'  # I'll adjust this if my backend runs on a different port or URL

    def test_submit_submission(self):
        payload = {
            "title": "Software Engineer",
            "specialty": "Backend Development",
            "city": "San Francisco",
            "state": "CA",
            "salary": 120000,
            "years_of_experience": 5
        }
        response = requests.post(f'{self.BASE_URL}/submission', json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('status'), 'Submission successful')

    def test_get_submissions(self):
        response = requests.get(f'{self.BASE_URL}/submissions')
        self.assertEqual(response.status_code, 200)
        submissions = response.json()
        self.assertIsInstance(submissions, list)
        if submissions:
            self.assertIn('title', submissions[0])
            self.assertIn('specialty', submissions[0])
            self.assertIn('city', submissions[0])
            self.assertIn('state', submissions[0])
            self.assertIn('salary', submissions[0])
            self.assertIn('years_of_experience', submissions[0])

if __name__ == '__main__':
    unittest.main()
