import React from 'react';
import { ChevronRight, Search, Map, Calendar, Star, ArrowRight } from 'lucide-react';

const LandingPage = () => {
  return (
    <div className="min-h-screen bg-white">
      {/* Hero Section */}
      <header className="relative h-screen">
        <div className="absolute inset-0 bg-black/40 z-10" />
        <div 
          className="absolute inset-0 bg-cover bg-center"
          style={{
            backgroundImage: "url('/bg.jpg')" }}
        />
        
        <nav className="relative z-20 container mx-auto px-6 py-6 flex items-center justify-between">
          <div className="text-white text-2xl font-bold">Travel Website</div>
          <div className="hidden md:flex space-x-8 text-white">
            <a href="#" className="hover:text-blue-200">Destinations</a>
            <a href="#" className="hover:text-blue-200">Packages</a>
            <a href="#" className="hover:text-blue-200">About Us</a>
            <a href="#" className="hover:text-blue-200">Contact</a>
          </div>
         <a href='/register'><button className="bg-blue-600 text-white px-6 py-2 rounded-full hover:bg-blue-700">
            Register
          </button>
          </a>
        </nav>

        <div className="relative z-20 container mx-auto px-6 h-full flex items-center">
          <div className="max-w-2xl">
            <h1 className="text-5xl md:text-6xl font-bold text-white mb-6">
              Discover Your Next Adventure
            </h1>
            <p className="text-xl text-white/90 mb-8">
              Explore breathtaking destinations and create unforgettable memories with our curated travel experiences.
            </p>
            
            {/* Search Bar */}
<div className="bg-white p-4 rounded-lg shadow-lg flex flex-wrap gap-4 items-center">
  <div className="flex-1 min-w-[200px] flex items-center gap-2 border border-gray-300 rounded-lg px-3 py-2">
    <Search className="text-gray-400" />
    <input 
      type="text" 
      placeholder="Where to?"
      className="w-full outline-none bg-transparent"
    />
  </div>
  <div className="flex-1 min-w-[200px] flex items-center gap-2 border border-gray-300 rounded-lg px-3 py-2">
    <Calendar className="text-gray-400" />
    <input 
      type="date" 
      placeholder="When?"
      className="w-full outline-none bg-transparent"
    />
  </div>
  <button className="bg-blue-600 text-white px-8 py-2 rounded-lg hover:bg-blue-700">
    Search
  </button>
</div>

          </div>
        </div>
      </header>

      {/* Featured Destinations */}
      <section className="py-20 bg-gray-50">
        <div className="container mx-auto px-6">
          <h2 className="text-3xl font-bold mb-12">Popular Destinations</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[1, 2, 3].map((i) => (
              <div key={i} className="bg-white rounded-xl overflow-hidden shadow-lg hover:shadow-xl transition-shadow">
                <div className="h-48 bg-gray-200">
                  <img 
                    src={`/api/placeholder/400/300`}
                    alt="destination"
                    className="w-full h-full object-cover"
                  />
                </div>
                <div className="p-6">
                  <h3 className="text-xl font-semibold mb-2">Destination {i}</h3>
                  <p className="text-gray-600 mb-4">
                    Experience the beauty and culture of this amazing destination.
                  </p>
                  <div className="flex items-center justify-between">
                    <div className="flex items-center gap-1">
                      <Star className="text-yellow-400 w-4 h-4 fill-current" />
                      <span className="text-gray-600">4.8</span>
                    </div>
                    <button className="text-blue-600 flex items-center gap-1 hover:text-blue-700">
                      Learn More <ChevronRight className="w-4 h-4" />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
            {[
              {
                icon: <Map className="w-8 h-8 text-blue-600" />,
                title: "Curated Destinations",
                description: "Hand-picked locations to ensure the best travel experience"
              },
              {
                icon: <Calendar className="w-8 h-8 text-blue-600" />,
                title: "Best Time to Visit",
                description: "Expert recommendations on when to visit each destination"
              },
              {
                icon: <Star className="w-8 h-8 text-blue-600" />,
                title: "Top-Rated Experience",
                description: "Consistently high-rated tours and activities"
              }
            ].map((feature, i) => (
              <div key={i} className="text-center">
                <div className="inline-block p-4 bg-blue-50 rounded-full mb-4">
                  {feature.icon}
                </div>
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="bg-blue-600 py-20">
        <div className="container mx-auto px-6 text-center">
          <h2 className="text-3xl font-bold text-white mb-6">
            Ready to Start Your Journey?
          </h2>
          <p className="text-white/90 mb-8 max-w-2xl mx-auto">
            Join thousands of satisfied travelers who have experienced the world with us.
          </p>
          <button className="bg-white text-blue-600 px-8 py-3 rounded-full font-semibold hover:bg-gray-100 inline-flex items-center gap-2">
            Start Planning <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-6">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <h4 className="text-xl font-bold mb-4">Wanderlust</h4>
              <p className="text-gray-400">
                Making your travel dreams come true since 2024.
              </p>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Quick Links</h4>
              <ul className="space-y-2 text-gray-400">
                <li><a href="#" className="hover:text-white">About Us</a></li>
                <li><a href="#" className="hover:text-white">Destinations</a></li>
                <li><a href="#" className="hover:text-white">Packages</a></li>
                <li><a href="#" className="hover:text-white">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Contact</h4>
              <ul className="space-y-2 text-gray-400">
                <li>Email: info@wanderlust.com</li>
                <li>Phone: +1 234 567 890</li>
                <li>Address: 123 Travel Street</li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold mb-4">Newsletter</h4>
              <p className="text-gray-400 mb-4">
                Subscribe to our newsletter for travel updates and exclusive offers.
              </p>
              <div className="flex gap-2">
                <input 
                  type="email" 
                  placeholder="Your email"
                  className="bg-gray-800 px-4 py-2 rounded flex-1 text-white"
                />
                <button className="bg-blue-600 px-4 py-2 rounded hover:bg-blue-700">
                  Subscribe
                </button>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;