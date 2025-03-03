import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import PostDetail from "./pages/PostDetail";
import Navbar from "./components/Navbar";

function App() {
  return (
    <Router>
      <div className="bg-gray-800 min-h-screen text-white">
        <Navbar />
        <Routes>
          {/* public home */}
          <Route path="/" element={<Home />} />

          {/* based on id post details page */}
          <Route path="/post/:id" element={<PostDetail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
