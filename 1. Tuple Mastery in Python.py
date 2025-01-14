def format_itineraries(itineraries):
    return "\n".join(
        f"Itinerary {i}: {traveler_name} - From {origin} to {destination}"
        for i, (traveler_name, origin, destination) in enumerate(itineraries, 1)
    )

# Example usage:
itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
formatted_output = format_itineraries(itineraries)
print(formatted_output)

