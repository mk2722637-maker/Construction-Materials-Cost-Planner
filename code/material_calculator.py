import pandas as pd
import numpy as np



class ConcreteElement:

    def __init__(self, element_id, name, site,
                 length, width, height):

        self.element_id = element_id
        self.name = name
        self.site = site
        self.length = length
        self.width = width
        self.height = height

    # Calculate net concrete volume
    def calculate_volume(self):
        return self.length * self.width * self.height

    # Calculate volume including 5% waste
    def calculate_waste_volume(self):

        volume = self.calculate_volume()

        return volume * 1.05

    # Calculate required materials
    def calculate_materials(self):

        volume = self.calculate_waste_volume()

        cement = volume * 300
        sand = volume * 0.5
        aggregate = volume * 0.8

        return {
            "cement_kg": cement,
            "sand_m3": sand,
            "aggregate_m3": aggregate
        }
# Read the element schedule from CSV
elements_data = pd.read_csv("Element.csv")

# Display the schedule
print(elements_data)

# Create an empty list to store elements
elements = []

# Loop through each row in the schedule
for i in range(len(elements_data)):

    # Create a ConcreteElement object using iloc to access row values
    element = ConcreteElement(
        elements_data.iloc[i]["element_id"],
        elements_data.iloc[i]["element_name"],
        elements_data.iloc[i]["site"],
        elements_data.iloc[i]["length_m"],
        elements_data.iloc[i]["width_m"],
        elements_data.iloc[i]["height_m"]
    )

    # Add the object to the elements list
    elements.append(element)

    # Create an empty list to store results
    results = []

    # Loop through all elements
    for element in elements:
        # Calculate volumes
        net_volume = element.calculate_volume()
        total_volume = element.calculate_waste_volume()

        # Calculate materials
        materials = element.calculate_materials()

        # Store results
        results.append({
            "element_id": element.element_id,
            "element_name": element.name,
            "site": element.site,
            "net_volume_m3": net_volume,
            "volume_with_waste_m3": total_volume,
            "cement_kg": materials["cement_kg"],
            "sand_m3": materials["sand_m3"],
            "aggregate_m3": materials["aggregate_m3"]
        })

    # Convert results into DataFrame
    results_data = pd.DataFrame(results)

    # Save results
    results_data.to_csv("Material_Requirements.csv", index=False)

    print("\nMaterial Requirements:")
    print(results_data)

    print("\nCSV file saved successfully!")