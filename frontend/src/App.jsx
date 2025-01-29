import { useState, useEffect } from "react";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/health")
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error("Error fetching API:", error));
  }, []);

  return (
    <div>
      <h1>Reddit Penny Stock Tracker</h1>
      <p>API Response: {message}</p>
    </div>
  );
}

export default App;
