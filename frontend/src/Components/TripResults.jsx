import React, { useEffect, useState, useMemo } from "react";
import { useSearchParams } from "react-router-dom";
import axios from "axios";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css";

const TripResults = () => {
  const [searchParams] = useSearchParams();
  const [tripData, setTripData] = useState(null);
  const [loading, setLoading] = useState(true);
  const token = useMemo(() => localStorage.getItem("token"), []);

  const places = useMemo(() => searchParams.getAll("place"), [searchParams]);
  const budget = useMemo(() => searchParams.get("budget"), [searchParams]);
  const travel_type = useMemo(() => searchParams.get("travel_type"), [searchParams]);
  const duration = useMemo(() => parseInt(searchParams.get("duration"), 10), [searchParams]);

  useEffect(() => {
    if (!places.length || !budget || !travel_type || !duration || !token) return;

    const fetchTripData = async () => {
      setLoading(true);
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/trip/generate/",
          { places, budget, travel_type, duration },
          { headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" } }
        );
        setTripData(response.data);
      } catch (error) {
        console.error("Error fetching trip data:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchTripData();
  }, [places, budget, travel_type, duration, token]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-r from-blue-400 to-purple-500 flex items-center justify-center">
        <div className="bg-white p-8 rounded-lg shadow-lg text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
          <p className="mt-4 text-lg font-semibold text-gray-700">Planning your dream trip...</p>
        </div>
      </div>
    );
  }
  
  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* Title & Overview */}
      <div className="max-w-4xl mx-auto bg-white p-6 rounded-lg shadow-lg text-center">
        <h1 className="text-4xl font-bold">{tripData.places.join(", ")}</h1>
        <p className="text-gray-600 mt-2">{tripData.about}</p>
        <div className="flex justify-center gap-4 mt-4 text-gray-700">
          <span className="px-3 py-1 bg-gray-200 rounded">Budget: {tripData.budget}</span>
          <span className="px-3 py-1 bg-gray-200 rounded">Type: {tripData.travel_type}</span>
          <span className="px-3 py-1 bg-gray-200 rounded">Duration: {tripData.duration} days</span>
        </div>
      </div>

      {/* Image Carousel */}
      <div className="max-w-4xl mx-auto mt-6 rounded-lg overflow-hidden shadow-lg">
        <Carousel showThumbs={false} infiniteLoop autoPlay>
          {tripData.images.map((img, index) => (
            <div key={index}>
              <img src={img} alt="Place" className="w-full h-80 object-cover" />
            </div>
          ))}
        </Carousel>
      </div>

      {/* Activities & Places */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto mt-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold mb-3">Top Activities</h2>
          <ul className="list-disc pl-5 text-gray-700">
            {tripData.top_activities.map((activity, index) => (
              <li key={index}>{activity}</li>
            ))}
          </ul>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold mb-3">Top Places</h2>
          <ul className="list-disc pl-5 text-gray-700">
            {tripData.top_places.map((place, index) => (
              <li key={index}>{place}</li>
            ))}
          </ul>
        </div>
      </div>

      {/* Itinerary */}
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-4xl mx-auto mt-6">
        <h2 className="text-2xl font-bold mb-4">Itinerary</h2>
        {tripData.itinerary.map((day, index) => (
          <div key={index} className="mt-4 p-4 border rounded-lg">
            <h3 className="font-semibold text-lg">Day {day.day}</h3>
            <p className="text-gray-700">🌅 Morning: {day.morning}</p>
            <p className="text-gray-700">🌞 Afternoon: {day.afternoon}</p>
            <p className="text-gray-700">🌙 Evening: {day.evening}</p>
          </div>
        ))}
      </div>

      {/* Local Cuisine & Packing Checklist */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto mt-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold">Local Cuisine</h2>
          <ul className="list-disc pl-5 text-gray-700">
            {tripData.local_cuisine.map((food, index) => (
              <li key={index}>{food}</li>
            ))}
          </ul>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold">Packing Checklist</h2>
          <ul className="list-disc pl-5 text-gray-700">
            {tripData.packing_checklist.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>
        </div>
      </div>

      {/* Best Time & Nearby Activities */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto mt-6">
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold">Best Time to Visit</h2>
          <p className="text-gray-700">{tripData.best_time_to_visit}</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow-lg">
          <h2 className="text-2xl font-bold">Nearby Activities</h2>
          <ul className="list-disc pl-5 text-gray-700">
            {tripData.nearby_activities.map((activity, index) => (
              <li key={index}>{activity}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default TripResults;
