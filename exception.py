# List of countries with their information
countries = [["Spain", "Madrid", "EUR"],
             ["United States", "Washington", "USD"],
             ["Canada", "Ottawa", "CAD"]
            ]

# Iterate over each country's information
for country in countries:
    # Unpack the country's details
    name, capital_city = country[:2]  # Extract only the first two elements
    # Print the name and capital city
    print(f"Country: {name}, Capital City: {capital_city}")
