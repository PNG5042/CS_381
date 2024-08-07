import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState({ restaurant: '', review: '', rating: '' });

  useEffect(() => {
    fetchReviews();
  }, []);

  const fetchReviews = async () => {
    try {
      const response = await axios.get('/reviews');
      setReviews(response.data);
    } catch (error) {
      console.error('Error fetching reviews:', error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('/review', newReview);
      fetchReviews();
    } catch (error) {
      console.error('Error submitting review:', error);
    }
  };

  const handleChange = (event) => {
    setNewReview({ ...newReview, [event.target.name]: event.target.value });
  };

  return (
    <div>
      <h1>Restaurant Reviews</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="restaurant" placeholder="Restaurant Name" onChange={handleChange} required />
        <textarea name="review" placeholder="Review" onChange={handleChange} required></textarea>
        <input type="number" name="rating" placeholder="Rating" onChange={handleChange} required />
        <button type="submit">Submit Review</button>
      </form>
      <h2>All Reviews</h2>
      <ul>
        {reviews.map((review, index) => (
          <li key={index}>
            <strong>{review.restaurant}</strong>: {review.review} (Rating: {review.rating})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
