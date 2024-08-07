import unittest
import json
from review_service import app

class ReviewServiceTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_review(self):
        response = self.app.post('/review', 
            data=json.dumps({"restaurant": "Test Restaurant", "review": "Great food!", "rating": 5}),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Review submitted', response.data)

    def test_get_reviews(self):
        self.app.post('/review', 
            data=json.dumps({"restaurant": "Test Restaurant", "review": "Great food!", "rating": 5}),
            content_type='application/json')
        response = self.app.get('/reviews')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Restaurant', response.data)

if __name__ == '__main__':
    unittest.main()
