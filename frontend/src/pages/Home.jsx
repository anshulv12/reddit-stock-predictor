import React, { useState, useEffect } from "react";
import PostCard from "../components/PostCard";

const Home = () => {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/api/reddit")
      .then((response) => response.json())
      .then((data) => setPosts(data.data))
      .catch((error) => console.error("Error fetching posts:", error));
  }, []);

  return (
    <div className="container mx-auto px-4 py-6">
      <h1 className="text-2xl font-bold mb-4 text-center">
        Latest Posts from r/pennystocks
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {posts.map((post) => (
          <PostCard key={post.id} post={post} />
        ))}
      </div>
    </div>
  );
};

export default Home;
