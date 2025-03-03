import React, { useEffect, useState } from "react";
import { useParams, useLocation } from "react-router-dom";

const PostDetail = () => {
  const { id } = useParams();  // grab the id 
  const location = useLocation();
  const post = location.state || {};

  // extract stock tickers from text based on all-caps words of 3 or 4 letters or $ followed by 1-4 letters
  const extractStockTickers = (text) => {
    if (!text) return [];
    // eegex matches words of exactly 3 or 4 uppercase letters
    const pattern = /\b[A-Z]{3,4}\b/g;
    const candidates = text.match(pattern) || [];
    // common non-ticker words add more if found in output
    const blacklist = ["CEO", "LOL", "OMG", "USA"];
    const filtered = candidates.filter((word) => !blacklist.includes(word));
    // list using a Set
    return Array.from(new Set(filtered));
  };

  // extract tickers from the post title
  const tickers = extractStockTickers(post.title);

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
      <h1 className="text-2xl font-bold mb-4">Post Details</h1>
      
      {/* display the extracted ticker(s) above the comments */}
      {tickers.length > 0 && (
        <div className="mb-4">
          <p className="text-xl">
            {tickers.length === 1 ? "Ticker:" : "Tickers:"} {tickers.join(', ')}
          </p>
        </div>
      )}
      
      <h2 className="text-2xl font-bold mb-4">Post Comments</h2>
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
