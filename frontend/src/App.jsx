import { useState, useEffect } from "react";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/reddit")
      .then(response => response.json())
      .then(data => setPosts(data.data))
      .catch(error => console.error("Error fetching posts:", error));
  }, []);

  return (
    <div>
      <h1>Reddit Penny Stock Tracker</h1>
      <h2>Latest Posts from r/pennystocks</h2>
      <ul>
        {posts.map((post, index) => (
          <li key={index}>
            <a href={post.url} target="_blank" rel="noopener noreferrer">
              {post.title}
            </a> (💬 {post.num_comments} | 👍 {post.score})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
