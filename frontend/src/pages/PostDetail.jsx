import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const PostDetail = () => {
  const { id } = useParams();  // gab the id from the url
  const [comments, setComments] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // fetch the comments for this post 
    fetch(`http://127.0.0.1:5000/api/reddit/${id}/comments`)
      .then((res) => res.json())
      .then((data) => {
        setComments(data.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching comments:", error);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return (
      <div className="container mx-auto px-4 py-6 text-white">
        <h1 className="text-2xl font-bold mb-4">Loading Comments...</h1>
      </div>
    );
  }

  return (
    <div className="container mx-auto px-4 py-6 text-white">
      <h1 className="text-2xl font-bold mb-4">Post Comments</h1>
      {comments.length === 0 ? (
        <p>No comments found for this post.</p>
      ) : (
        <ul className="space-y-4">
          {comments.map((comment, index) => (
            <li
              key={index}
              className="border border-gray-600 rounded-lg p-4 bg-gray-700"
            >
              <p className="mb-2">{comment.body}</p>
              <p className="text-gray-400 text-sm">
                Score: {comment.score}
              </p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default PostDetail;
