import os
import requests
from groq import Groq
import json
import re
# Load API keys from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def generate_trip_data(trip_data):
    """Fetch AI-generated trip details and external data."""
    places = trip_data.places

    # Generate AI-based travel details
    ai_response = generate_ai_trip_details(trip_data)

    # Fetch images from Unsplash
    image_dict = fetch_images(places)
    image_list=[]
    for place_image in image_dict.values():
        image_list.extend(place_image)

    return {
        "places": places,
        "images": image_list,
        "about": ai_response.get("about"),
        "top_activities": ai_response.get("top_activities"),
        "top_places": ai_response.get("top_places"),
        "itinerary": ai_response.get("itinerary"),
        "local_cuisine": ai_response.get("local_cuisine"),
        "packing_checklist": ai_response.get("packing_checklist"),
        "best_time_to_visit": ai_response.get("best_time_to_visit"),
        "nearby_activities": ai_response.get("nearby_activities")
    }
def generate_ai_trip_details(trip_data):
    """Generate AI-based travel itinerary and details using Groq."""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Set it in environment variables.")

    # Ensure all required fields exist
    required_fields = ["places", "duration", "budget", "travel_type"]
    for field in required_fields:
        if not hasattr(trip_data, field) or getattr(trip_data, field) is None:
            raise ValueError(f"Missing required field: {field}")

    destinations = ", ".join(trip_data.places) if trip_data.places else "unknown location"

    # AI prompt to generate structured travel plan
    prompt = f"""
You are a structured travel planner. Generate a **valid JSON** response for a {trip_data.duration}-day trip.

### **Instructions:**
- The output **must be valid JSON**.
- No extra text, explanations, or formatting—just JSON.
- Use the structure exactly as shown below.
- For each day in the itinerary, include morning, afternoon, and evening activities.

### **JSON Structure:**
```json
{{
  "places": "{destinations}",
  "budget": "{trip_data.budget}",
  "travel_type": "{trip_data.travel_type}",
  "duration": {trip_data.duration},
  "about": "Brief description of {destinations}.",
  "itinerary": [
    {{
      "day": 1,
      "morning": "Specific morning activity",
      "afternoon": "Specific afternoon activity",
      "evening": "Specific evening activity"
    }}
  ],
  "top_activities": [
    "Activity 1",
    "Activity 2",
    "Activity 3",
    "Activity 4",
    "Activity 5"
  ],
  "top_places": [
    "Place 1",
    "Place 2",
    "Place 3",
    "Place 4",
    "Place 5"
  ],
  "local_cuisine": [
    "Dish 1",
    "Dish 2",
    "Dish 3",
    "Dish 4",
    "Dish 5"
  ],
  "packing_checklist": [
    "Item 1",
    "Item 2",
    "Item 3",
    "Item 4",
    "Item 5"
  ],
  "best_time_to_visit": "Best months to visit {destinations}.",
  "nearby_activities": [
    "Nearby Activity 1",
    "Nearby Activity 2",
    "Nearby Activity 3",
    "Nearby Activity 4"
  ]
}}
"""

    # Connect to Groq API and get AI-generated travel details
    client = Groq(api_key=GROQ_API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    
    response_text = chat_completion.choices[0].message.content.strip()
    
    return parse_ai_response(response_text)

def fetch_images(places):
    """Fetch images from Unsplash API for multiple places."""
    if not UNSPLASH_ACCESS_KEY:
        raise ValueError("Missing UNSPLASH_ACCESS_KEY. Set it in environment variables.")
    
    image_dict = {}
    
    for place in places:
        url = f"https://api.unsplash.com/search/photos?query={place}&client_id={UNSPLASH_ACCESS_KEY}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            image_dict[place] = [img["urls"]["regular"] for img in data.get("results", [])[:5]]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching images for {place}: {e}")
            image_dict[place] = []
    
    return image_dict


def parse_ai_response(response_text):
    """Parse AI response and extract the structured travel data."""
    try:
        # Try to find JSON content between triple backticks if present
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', response_text)
        if json_match:
            json_content = json_match.group(1)
        else:
            json_content = response_text
        
        json_content = json_content.strip()
        
        # Parse the JSON content
        parsed_data = json.loads(json_content)
        
        # Return a dictionary with all the expected fields
        return {
            "places": parsed_data.get("places", ""),
            "budget": parsed_data.get("budget", "N/A"),
            "travel_type": parsed_data.get("travel_type", "N/A"),
            "duration": parsed_data.get("duration", 0),
            "about": parsed_data.get("about", "N/A"),
            "top_activities": parsed_data.get("top_activities", []),
            "top_places": parsed_data.get("top_places", []),
            "itinerary": parsed_data.get("itinerary", []),
            "local_cuisine": parsed_data.get("local_cuisine", []),
            "packing_checklist": parsed_data.get("packing_checklist", []),
            "best_time_to_visit": parsed_data.get("best_time_to_visit", "N/A"),
            "nearby_activities": parsed_data.get("nearby_activities", [])
        }
    except json.JSONDecodeError as e:
        print(f"Error parsing AI response as JSON: {e}")
        print(f"Response received: {response_text[:500]}...")  # Print first 500 chars for debugging
        return {}
    except Exception as e:
        print(f"Unexpected error parsing AI response: {e}")
        return {}