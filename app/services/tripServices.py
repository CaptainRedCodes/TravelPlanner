# import openai
# import requests
# from app.config import OPENAI_API_KEY

# def generate_trip_data(trip_data):
#     """Fetch AI-generated trip details and external data"""
#     place = trip_data.place
#     itinerary = generate_ai_itinerary(trip_data)
#     images = fetch_images(place)

#     return {"itinerary": itinerary, "images": images}

# def generate_ai_itinerary(trip_data):
#     """Generate itinerary using OpenAI"""
#     prompt = f"Create a {trip_data.duration}-day itinerary for {trip_data.place}."
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": prompt}],
#         api_key=OPENAI_API_KEY
#     )
#     return response["choices"][0]["message"]["content"]

# def fetch_images(place):
#     """Fetch images from Unsplash"""
#     url = f"https://api.unsplash.com/search/photos?query={place}&client_id=UNSPLASH_API_KEY"
#     response = requests.get(url).json()
#     return [img["urls"]["regular"] for img in response["results"][:5]]
