import os
import requests
from groq import Groq

# Load API keys from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

def generate_trip_data(trip_data):
    """Fetch AI-generated trip details and external data"""
    place = trip_data.place

    #print("Trip Data:", trip_data.__dict__)  # If trip_data is an object

    # Generate AI-based travel details
    ai_response = generate_ai_trip_details(trip_data)

    # Fetch images from Unsplash
    images = fetch_images(place)

    return {
        "place": place,
        "images": images,
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
    """Generate trip details using Groq AI"""
    if not GROQ_API_KEY:
        raise ValueError("Missing GROQ_API_KEY. Set it in environment variables.")

    # Ensure all required fields exist
    required_fields = ["place", "duration", "budget", "travel_type"]
    for field in required_fields:
        if not hasattr(trip_data, field) or getattr(trip_data, field) is None:
            raise ValueError(f"Missing required field: {field}")

    prompt = f"""
Generate a structured travel guide for {trip_data.place} for a {trip_data.duration}-day trip. 
The traveler has a **{trip_data.budget}** budget and is traveling **{trip_data.travel_type}**.

### About
Provide a **single concise paragraph** (max 500 characters) summarizing the destination.
(Do not exceed this limit to avoid database errors.)

### Top Activities ({trip_data.budget} Budget | {trip_data.travel_type} Travel)
Suggest **5 must-do activities** based on the budget and travel type:
- **Budget Considerations**:
  - **Cheap**: Free attractions, local experiences, public transport, outdoor activities.
  - **Moderate**: Mix of budget and premium activities, guided tours, mid-range dining.
  - **Luxury**: VIP access, exclusive tours, private transfers, fine dining, luxury stays.
- **Travel Type Considerations**:
  - **Solo**: Safe & independent experiences, self-guided tours, social hostels.
  - **Duo**: Romantic getaways, couples’ experiences, shared activities.
  - **Family**: Kid-friendly attractions, family accommodations, educational spots.
  - **Friends**: Group-friendly activities, nightlife, adventure sports.
Each on a separate line in this format:
- **Activity Name**: Brief description (max 150 characters per line)

### Top Places ({trip_data.budget} Budget | {trip_data.travel_type} Travel)
List **5 key places** considering the budget and travel type:
- **Budget Considerations**:
  - **Cheap**: Free-to-enter landmarks, public parks, local hotspots.
  - **Moderate**: Paid attractions, guided visits, mid-range experiences.
  - **Luxury**: Exclusive resorts, private experiences, premium sightseeing.
- **Travel Type Considerations**:
  - **Solo**: Safe and easy-to-navigate locations.
  - **Duo**: Romantic destinations with scenic beauty.
  - **Family**: Attractions with activities for all ages.
  - **Friends**: Social hotspots, nightlife, adventure hubs.
Each on a separate line:
- **Place Name**: Brief highlight (max 100 characters per line)

### {trip_data.duration}-Day Itinerary ({trip_data.budget} Budget | {trip_data.travel_type} Travel)
Provide a structured itinerary considering the budget and travel type:
- **Budget Considerations**:
  - **Cheap**: Public transport, street food, free attractions.
  - **Moderate**: Balanced mix of budget and premium experiences.
  - **Luxury**: Private tours, chauffeur services, fine dining.
- **Travel Type Considerations**:
  - **Solo**: Independent sightseeing, self-guided exploration.
  - **Duo**: Romantic dinners, scenic walks, couple-friendly adventures.
  - **Family**: Kid-friendly activities, relaxed schedule.
  - **Friends**: Group adventures, party-friendly spots.
Use this format (each under 200 characters):
Day 1:
- Morning: Activity
- Afternoon: Activity
- Evening: Activity

### Local Cuisine ({trip_data.budget} Budget | {trip_data.travel_type} Travel)
Suggest **5 must-try dishes**:
- **Budget Considerations**:
  - **Cheap**: Street food, affordable local specialties.
  - **Moderate**: Popular restaurants, mid-range dining.
  - **Luxury**: Michelin-starred restaurants, gourmet meals.
- **Travel Type Considerations**:
  - **Solo**: Easy-to-find meals, quick-service options.
  - **Duo**: Romantic dining spots, scenic cafes.
  - **Family**: Kid-friendly meals, allergy-conscious options.
  - **Friends**: Shareable meals, lively food spots.
Each on a separate line:
- **Dish Name**: Description and where to try it (max 150 characters per line)

### Packing Checklist
List **10 essential items**, one per line:
- Item Name (max 50 characters per line)

### Best Time to Visit
Provide a **single** concise paragraph (max 250 characters) about the ideal travel season and reasons.

### Nearby Activities
List **4 nearby attractions**, each on a separate line:
- **Place Name**: Distance and key highlight (max 150 characters per line)

**Formatting Rules:**
- Each list item must be **self-contained** and **parsable as a string in a list**.
- Use **exact** formatting as instructed (no nested bullets, tables, or complex formatting).
- Keep all responses structured and within the **character limits** to prevent database errors.
"""



    # ✅ Now prompt is assigned, preventing UnboundLocalError
    client = Groq(api_key=GROQ_API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    
    response_text = chat_completion.choices[0].message.content.strip()
    
    
    return parse_ai_response(response_text)


import re

def parse_ai_response(response_text):
    """Parse AI response and map the correct data fields."""
    
    parsed_data = {
        "about": "",
        "top_activities": [],
        "top_places": [],
        "itinerary": [],
        "local_cuisine": [],
        "packing_checklist": [],
        "best_time_to_visit": "",
        "nearby_activities": []
    }

    sections = response_text.split("\n\n")  # Split into sections based on spacing

    for section in sections:
        lines = section.strip().split("\n")
        if not lines:
            continue

        first_line = lines[0].lower()

        if "about" in first_line:
            parsed_data["about"] = " ".join(lines[1:]).strip()

        elif "top activities" in first_line:
            parsed_data["top_activities"] = [line.strip("- ").strip() for line in lines[1:] if line.startswith("-")]

        elif "top places" in first_line:
            parsed_data["top_places"] = [line.strip("- ").strip() for line in lines[1:] if line.startswith("-")]

        elif "itinerary" in first_line:
            parsed_data["itinerary"] = [line.strip("- ").strip() for line in lines[1:] if line]

        elif "local cuisine" in first_line:
            parsed_data["local_cuisine"] = [line.strip("- ").strip() for line in lines[1:] if line.startswith("-")]

        elif "packing checklist" in first_line:
            parsed_data["packing_checklist"] = [line.strip("- ").strip() for line in lines[1:] if line.startswith("-")]

        elif "best time to visit" in first_line:
            parsed_data["best_time_to_visit"] = " ".join(lines[1:]).strip()

        elif "nearby activities" in first_line:
            parsed_data["nearby_activities"] = [line.strip("- ").strip() for line in lines[1:] if line.startswith("-")]

    return parsed_data




def fetch_images(place):
    """Fetch images from Unsplash"""
    if not UNSPLASH_ACCESS_KEY:
        raise ValueError("Missing UNSPLASH_ACCESS_KEY. Set it in environment variables.")

    url = f"https://api.unsplash.com/search/photos?query={place}&client_id={UNSPLASH_ACCESS_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [img["urls"]["regular"] for img in data.get("results", [])[:5]]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching images: {e}")
        return []
