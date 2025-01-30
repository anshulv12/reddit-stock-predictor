import React from "react";

const PostCard = ({ post }) => {
  return (
    <div className="border border-gray-600 rounded-lg p-4 shadow-md bg-gray-700 text-white">
      <h2 className="text-lg font-bold mb-2">
        <a
          href={post.url}
          target="_blank"
          rel="noopener noreferrer"
          className="text-blue-400 hover:underline"
        >
          {post.title}
        </a>
      </h2>
      <p className="text-gray-400">👍 {post.score} | 💬 {post.num_comments} comments</p>
    </div>
  );
};

export default PostCard;
