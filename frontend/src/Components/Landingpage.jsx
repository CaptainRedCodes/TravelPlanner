import React, { useState, useEffect } from "react";
import { useNavigate, Link } from "react-router-dom";
import AnimatedSearchBox from "./AnimatedSearchBox";

const LandingPage = () => {
  const navigate = useNavigate();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState("");

  // Check if user is logged in on component mount
  useEffect(() => {
    const token = localStorage.getItem("token");
    const storedUsername = localStorage.getItem("username");
    if (token && storedUsername) {
      setIsLoggedIn(true);
      setUsername(storedUsername);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("username");
    setIsLoggedIn(false);
    setUsername("");
    navigate("/");
  };

  const handleSearch = (searchParams) => {
    const { places, travelType, budget, duration } = searchParams;

    if (places.every((place) => !place.trim())) return; // Ensure at least one place

    // Convert data into a query string
    const queryParams = new URLSearchParams({
      budget,
      travel_type: travelType,
      duration: duration.toString(),
    });

    // Add multiple places to query params
    places.forEach((place) => queryParams.append("place", place));

    // Navigate to TripResults with the correct params
    navigate(`/trip-results?${queryParams.toString()}`);
  };

  return (
    <div className="flex flex-col min-h-screen">
      {/* Navigation Bar */}
      <nav className="bg-gradient-to-r from-blue-800 to-indigo-900 text-white p-4 shadow-lg">
        <div className="container mx-auto flex justify-between items-center">
          <Link to="/" className="text-2xl font-bold flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clipRule="evenodd" />
            </svg>
            TravelAI
          </Link>
          
          <div className="flex items-center space-x-4">
            {isLoggedIn ? (
              <>
                <span className="hidden md:inline">Welcome, {username}!</span>
                <button 
                  onClick={handleLogout}
                  className="bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-lg transition duration-300 flex items-center"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M3 3a1 1 0 00-1 1v12a1 1 0 001 1h12a1 1 0 001-1V7.414l-5-5H3zm7 5a1 1 0 10-2 0v4.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L12 12.586V8a1 1 0 00-1-1z" clipRule="evenodd" />
                  </svg>
                  Logout
                </button>
              </>
            ) : (
              <>
                <Link 
                  to="/login" 
                  className="bg-transparent border border-white hover:bg-white hover:text-blue-800 text-white py-2 px-4 rounded-lg transition duration-300"
                >
                  Login
                </Link>
                <Link 
                  to="/register" 
                  className="bg-white text-blue-800 hover:bg-blue-100 py-2 px-4 rounded-lg transition duration-300"
                >
                  Register
                </Link>
              </>
            )}
          </div>
        </div>
      </nav>

      {/* Main Hero Section */}
      <div
        className="relative flex-grow flex flex-col items-center justify-center bg-cover bg-center"
        style={{ backgroundImage: "url('/bg.jpg')" }}
      >
        <div className="absolute inset-0 bg-black/50 backdrop-blur-sm"></div>
        
        <div className="relative z-10 text-center px-6 max-w-4xl mx-auto">
          <h1 className="text-4xl md:text-6xl font-bold text-white drop-shadow-lg animate-fade-in">
            Discover Your Next Adventure
          </h1>
          
          <p className="text-lg md:text-xl text-white/90 mt-4 mb-8 max-w-2xl mx-auto">
            Explore breathtaking destinations with AI-generated travel plans 
            customized just for you.
          </p>
          
          {/* Animated Search Box */}
          <div className="mt-6 w-full max-w-lg mx-auto">
            <AnimatedSearchBox 
              onSearch={handleSearch} 
              isDisabled={!isLoggedIn}
              loginPrompt={!isLoggedIn ? "Please login to plan your trip" : ""}
            />
          </div>
          
          {!isLoggedIn && (
            <div className="mt-4 bg-white/10 backdrop-blur-md p-3 rounded-lg inline-block">
              <p className="text-white flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                </svg>
                <Link to="/login" className="underline font-semibold">Login</Link> or <Link to="/register" className="underline font-semibold">Register</Link> to plan your next adventure!
              </p>
            </div>
          )}
        </div>
        
        {/* Features Section */}
        <div className="w-full mt-12 relative z-10 px-4">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
            <div className="bg-white/10 backdrop-blur-md p-6 rounded-xl text-white">
              <div className="bg-blue-600 p-3 rounded-full w-12 h-12 flex items-center justify-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">AI-Powered Plans</h3>
              <p>Get personalized travel itineraries generated by advanced AI specifically for your preferences.</p>
            </div>
            
            <div className="bg-white/10 backdrop-blur-md p-6 rounded-xl text-white">
              <div className="bg-blue-600 p-3 rounded-full w-12 h-12 flex items-center justify-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Budget Friendly</h3>
              <p>Plan trips that match your budget perfectly, from economical getaways to luxury experiences.</p>
            </div>
            
            <div className="bg-white/10 backdrop-blur-md p-6 rounded-xl text-white">
              <div className="bg-blue-600 p-3 rounded-full w-12 h-12 flex items-center justify-center mb-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3" />
                </svg>
              </div>
              <h3 className="text-xl font-bold mb-2">Custom Experiences</h3>
              <p>Discover hidden gems and local favorites tailored to your travel style and preferences.</p>
            </div>
          </div>
        </div>
      </div>
      
      {/* Footer */}
      <footer className="bg-blue-900 text-white py-6">
        <div className="container mx-auto px-4 text-center">
          <p>&copy; {new Date().getFullYear()} TravelAI. All rights reserved.</p>
          <div className="flex justify-center mt-4 space-x-4">
            <a href="#" className="hover:text-blue-300 transition">About</a>
            <a href="#" className="hover:text-blue-300 transition">Privacy</a>
            <a href="#" className="hover:text-blue-300 transition">Terms</a>
            <a href="#" className="hover:text-blue-300 transition">Contact</a>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;