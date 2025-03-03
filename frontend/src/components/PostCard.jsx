import React from "react";
import { Link } from "react-router-dom";

const PostCard = ({ post }) => {
  return (
    <div className="border border-gray-600 rounded-lg p-4 shadow-md bg-gray-700 text-white">
      <h2 className="text-lg font-bold mb-2">
        {/* Pass the entire post object as state */}
        <Link to={`/post/${post.id}`} state={post} className="text-blue-400 hover:underline">
          {post.title}
        </Link>
      </h2>
      <p className="text-gray-400">
        👍 {post.score} | 💬 {post.num_comments} comments
      </p>
    </div>
  );
};

export default PostCard;
