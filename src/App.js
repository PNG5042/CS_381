import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [submissions, setSubmissions] = useState([]);
  const [newSubmission, setNewSubmission] = useState({
    title: '',
    specialty: '',
    city: '',
    state: '',
    salary: '',
    yearsOfExperience: ''
  });

  useEffect(() => {
    fetchSubmissions();
  }, []);

  const fetchSubmissions = async () => {
    try {
      const response = await axios.get('/submissions');
      setSubmissions(response.data);
    } catch (error) {
      console.error('Error fetching submissions:', error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      await axios.post('/submission', newSubmission);
      fetchSubmissions();
    } catch (error) {
      console.error('Error submitting data:', error);
    }
  };

  const handleChange = (event) => {
    setNewSubmission({ ...newSubmission, [event.target.name]: event.target.value });
  };

  return (
    <div>
      <h1>Submission Form</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="title" placeholder="Title" onChange={handleChange} required />
        <input type="text" name="specialty" placeholder="Specialty" onChange={handleChange} required />
        <input type="text" name="city" placeholder="City" onChange={handleChange} required />
        <input type="text" name="state" placeholder="State" onChange={handleChange} required />
        <input type="number" name="salary" placeholder="Salary" onChange={handleChange} required />
        <input type="number" name="yearsOfExperience" placeholder="Years of Experience" onChange={handleChange} required />
        <button type="submit">Submit</button>
      </form>
      <h2>All Submissions</h2>
      <ul>
        {submissions.map((submission, index) => (
          <li key={index}>
            <strong>{submission.title}</strong>, {submission.specialty}, {submission.city}, {submission.state} - Salary: {submission.salary}, Experience: {submission.yearsOfExperience} years
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

}

export default App;
