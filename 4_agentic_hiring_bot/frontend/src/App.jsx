
import React, { useState } from 'react';
import axios from 'axios';
import './index.css';

function App() {
  const [jobInput, setJobInput] = useState({
    title: '',
    description: '',
    requirements: '',
    role: 'Hiring Manager',
  });
  const [jobId, setJobId] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setJobInput({ ...jobInput, [name]: value });
  };

  const handleJobIdChange = (e) => {
    setJobId(e.target.value);
  };

  const runWorkflow = async (payload) => {
    setLoading(true);
    setError('');
    setResponse(null);
    try {
      const res = await axios.post('/run_agent', payload, {
        headers: { 'Content-Type': 'application/json' },
      });
      setResponse(res.data.result);
    } catch (err) {
      setError('Error running workflow: ' + (err.response?.data?.error || err.message));
    } finally {
      setLoading(false);
    }
  };

  const createJob = () => {
    const requirements = jobInput.requirements.split(',').map((req) => req.trim());
    runWorkflow({ ...jobInput, requirements });
  };

  const runExistingJob = () => {
    if (!jobId) {
      setError('Please enter a Job ID');
      return;
    }
    runWorkflow({ job_id: parseInt(jobId) });
  };

  return (
    <div className="container">
      <h1>Agentic Hiring Bot Demo</h1>
      <div className="section">
        <h2>Create New Job</h2>
        <input
          type="text"
          name="title"
          placeholder="Job Title"
          value={jobInput.title}
          onChange={handleInputChange}
        />
        <textarea
          name="description"
          placeholder="Job Description"
          value={jobInput.description}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="requirements"
          placeholder="Requirements (comma-separated)"
          value={jobInput.requirements}
          onChange={handleInputChange}
        />
        <button onClick={createJob} disabled={loading}>
          {loading ? 'Creating...' : 'Create Job'}
        </button>
      </div>
      <div className="section">
        <h2>Run Workflow for Existing Job</h2>
        <input
          type="number"
          placeholder="Job ID"
          value={jobId}
          onChange={handleJobIdChange}
        />
        <button onClick={runExistingJob} disabled={loading}>
          {loading ? 'Running...' : 'Run Workflow'}
        </button>
      </div>
      {error && <div className="error">{error}</div>}
      {response && (
        <div className="response">
          <h2>Workflow Result</h2>
          <pre>{JSON.stringify(response, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
