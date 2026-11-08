import pandas as pd

# Import ConcreteElement class from Module 1
from material_calculator import ConcreteElement

# Read required material quantities
required = pd.read_csv("Material_Requirements.csv")

# Read purchased material quantities
purchased = pd.read_csv("Purchased_Materials.csv")


# Create an empty list for comparison results
results = []

# Loop through each element
for i in range(len(required)):

    element_id = required.iloc[i]["element_id"]

    # Get required quantities
    cement_required = required.iloc[i]["cement_kg"]
    sand_required = required.iloc[i]["sand_m3"]
    aggregate_required = required.iloc[i]["aggregate_m3"]

    # Get purchased quantities for this element
    element_purchases = purchased[purchased["element_id"] == element_id]

    # Loop through each material
    for material, required_quantity in [
        ("Cement", cement_required),
        ("Sand", sand_required),
        ("Aggregate", aggregate_required)
    ]:

        # Extract purchased quantity
        purchased_quantity = element_purchases[
            element_purchases["material"] == material
        ]["quantity"].sum()

        # Calculate difference
        difference = purchased_quantity - required_quantity

        # Identify shortage or surplus
        if difference > 0:
            status = "Surplus"
        elif difference < 0:
            status = "Shortage"
        else:
            status = "Exact"

        # Store results
        results.append({
            "element_id": element_id,
            "material": material,
            "required_quantity": required_quantity,
            "purchased_quantity": purchased_quantity,
            "difference": difference,
            "status": status
        })


# Convert results into DataFrame
comparison = pd.DataFrame(results)

# Display results
print(comparison)

# Save report
comparison.to_csv("Material_Comparison_Report.csv", index=False)



