import random

def generate_weather_data(days):
    """Simulate weather data generation."""
    data = []
    for _ in range(days):
        cloudy = random.random() < 0.4  # 40% chance of a cloudy day
        rain_next_day = random.random() < (0.6 if cloudy else 0.2)  # Higher chance of rain after a cloudy day
        data.append((cloudy, rain_next_day))
    return data

def calculate_probability(data):
    """Calculate P(A|B) - probability of rain tomorrow given cloudy today."""
    cloudy_days = sum(1 for day in data if day[0])
    rainy_days_after_cloudy = sum(1 for i in range(len(data)-1) if data[i][0] and data[i+1][1])
    
    p_b = cloudy_days / len(data)  # P(B) - probability of a cloudy day
    p_a_given_b = rainy_days_after_cloudy / cloudy_days  # P(A|B)
    p_a = sum(1 for day in data if day[1]) / len(data)  # P(A) - overall probability of rain
    
    return p_a_given_b, p_b, p_a

# Generate simulated weather data
days = 1000
weather_data = generate_weather_data(days)

# Calculate probabilities
p_rain_given_cloudy, p_cloudy, p_rain = calculate_probability(weather_data)

# Print results
print(f"Based on {days} days of simulated weather data:")
print(f"Probability of a cloudy day: {p_cloudy:.2%}")
print(f"Overall probability of rain: {p_rain:.2%}")
print(f"Probability of rain tomorrow given cloudy today: {p_rain_given_cloudy:.2%}")

# Calculate how much more likely it is to rain after a cloudy day
relative_likelihood = p_rain_given_cloudy / p_rain
print(f"\nIt is {relative_likelihood:.2f} times more likely to rain after a cloudy day compared to the overall probability of rain.")
