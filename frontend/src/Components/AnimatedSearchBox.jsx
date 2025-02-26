import React, { useState, useEffect } from "react";

const AnimatedSearchBox = ({ onSearch, isDisabled, loginPrompt }) => {
  const [places, setPlaces] = useState([""]);
  const [travelType, setTravelType] = useState("Solo");
  const [budget, setBudget] = useState("Moderate");
  const [duration, setDuration] = useState(7);
  const [placeholderText, setPlaceholderText] = useState("Paris");
  
  // Sample destinations for placeholder animation
  const destinations = [
    "Paris", "Tokyo", "New York", "Bali", "Rome",
    "Barcelona", "Sydney", "Rio de Janeiro", "Cape Town",
    "Kyoto", "Amsterdam", "Santorini", "Machu Picchu"
  ];
  
  // Animate placeholder text
  useEffect(() => {
    const interval = setInterval(() => {
      const randomIndex = Math.floor(Math.random() * destinations.length);
      setPlaceholderText(destinations[randomIndex]);
    }, 2000);
    
    return () => clearInterval(interval);
  }, []);
  
  const handleAddPlace = () => {
    setPlaces([...places, ""]);
  };
  
  const handleRemovePlace = (index) => {
    if (places.length > 1) {
      const newPlaces = [...places];
      newPlaces.splice(index, 1);
      setPlaces(newPlaces);
    }
  };
  
  const handlePlaceChange = (index, value) => {
    const newPlaces = [...places];
    newPlaces[index] = value;
    setPlaces(newPlaces);
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    if (isDisabled) return;
    
    // Filter out empty places
    const filteredPlaces = places.filter(place => place.trim());
    
    if (filteredPlaces.length > 0) {
      onSearch({
        places: filteredPlaces,
        travelType,
        budget,
        duration
      });
    }
  };
  
  return (
    <div className={`bg-white rounded-lg shadow-xl overflow-hidden transition-all duration-300 ${isDisabled ? 'opacity-95' : 'opacity-100'}`}>
      <form onSubmit={handleSubmit} className="p-6">
        <div className="mb-4">
          <label className="block text-gray-700 text-sm font-bold mb-2">
            Where to?
          </label>
          <div className="space-y-2">
            {places.map((place, index) => (
              <div key={index} className="flex items-center">
                <input
                  type="text"
                  className="flex-grow border border-gray-300 rounded-lg p-2 focus:border-blue-500 focus:ring focus:ring-blue-200 transition"
                  placeholder={`Destination ${index + 1} (e.g., ${placeholderText})`}
                  value={place}
                  onChange={(e) => handlePlaceChange(index, e.target.value)}
                  disabled={isDisabled}
                />
                {places.length > 1 && (
                  <button
                    type="button"
                    className="ml-2 text-red-500 hover:text-red-700"
                    onClick={() => handleRemovePlace(index)}
                    disabled={isDisabled}
                  >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                  </button>
                )}
              </div>
            ))}
          </div>
          <button
            type="button"
            className="mt-2 text-blue-600 hover:text-blue-800 text-sm font-medium inline-flex items-center"
            onClick={handleAddPlace}
            disabled={isDisabled}
          >
            <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-11a1 1 0 10-2 0v2H7a1 1 0 100 2h2v2a1 1 0 102 0v-2h2a1 1 0 100-2h-2V7z" clipRule="evenodd" />
            </svg>
            Add another destination
          </button>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Travel Type
            </label>
            <select
              className="w-full border border-gray-300 rounded-lg p-2 focus:border-blue-500 focus:ring focus:ring-blue-200 transition"
              value={travelType}
              onChange={(e) => setTravelType(e.target.value)}
              disabled={isDisabled}
            >
              <option value="Solo">Solo</option>
              <option value="Duo">Duo</option>
              <option value="Family">Family</option>
              <option value="Friends">Friends</option>
            </select>
          </div>
          
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Budget
            </label>
            <select
              className="w-full border border-gray-300 rounded-lg p-2 focus:border-blue-500 focus:ring focus:ring-blue-200 transition"
              value={budget}
              onChange={(e) => setBudget(e.target.value)}
              disabled={isDisabled}
            >
              <option value="Cheap">Budget</option>
              <option value="Moderate">Moderate</option>
              <option value="Luxury">Luxury</option>
            </select>
          </div>
          
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">
              Duration (days)
            </label>
            <input
              type="number"
              min="1"
              max="30"
              className="w-full border border-gray-300 rounded-lg p-2 focus:border-blue-500 focus:ring focus:ring-blue-200 transition"
              value={duration}
              onChange={(e) => setDuration(parseInt(e.target.value) || 1)}
              disabled={isDisabled}
            />
          </div>
        </div>
        
        {loginPrompt && (
          <div className="mb-4 text-orange-600 text-sm font-medium bg-orange-100 p-2 rounded-lg flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
            </svg>
            {loginPrompt}
          </div>
        )}
        
        <button
          type="submit"
          className={`w-full py-3 rounded-lg text-white font-medium text-lg transition duration-300 ${
            isDisabled 
              ? 'bg-blue-400 cursor-not-allowed' 
              : 'bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50'
          }`}
          disabled={isDisabled}
        >
          {isDisabled ? "Login to Plan Your Trip" : "Plan My Trip"}
        </button>
      </form>
    </div>
  );
};

export default AnimatedSearchBox;