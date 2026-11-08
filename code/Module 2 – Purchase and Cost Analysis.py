import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read the concrete elements data
elements = pd.read_csv("Element.csv")

# Read the supplier prices data
prices = pd.read_csv("Prices.csv")

# Read the purchase transactions
purchases = pd.read_csv("purchases.csv")


print("Before Cleaning:")
print("Elements:", len(elements))
print("Prices:", len(prices))
print("Purchases:", len(purchases))

# Remove missing values
prices = prices.dropna()
purchases = purchases.dropna()

# Remove identical rows
prices = prices.drop_duplicates()


purchases = purchases.drop_duplicates()

print("After Cleaning:")
print("Elements:", len(elements))
print("Prices:", len(prices))
print("Purchases:", len(purchases))



data = pd.merge(
    purchases,
    prices,
    on=["supplier_id", "material"],
    #Keep only the rows that have matching values in BOTH tables.
    how="inner"
)

print(data)

# Calculate cost for each purchase
data["purchase_cost"] = data["quantity"] * data["unit_price"]

print(data)

data.to_csv(
    "data.csv",
    index=False
)


# Calculate total quantity and cost for each material from each supplier
supplier_cost = data.groupby(["supplier_id", "material"]).agg({
    "quantity": "sum",
    "unit_price": "first",
    "purchase_cost": "sum"
})

print("supplier_cost")
print(supplier_cost)

# Calculate total purchased quantity for each element and material

purchased_materials = purchases.groupby(
    ["element_id", "material"]
)["quantity"].sum().reset_index()

print(purchased_materials)

# Save purchased quantities into CSV
purchased_materials.to_csv(
    "Purchased_Materials.csv",
    index=False
)




print("Use NumPy to compare estimated costs for required quantities before and after increasing the price .")

# Read calculated material requirements from Module 1
required = pd.read_csv("Material_Requirements.csv")

# Read supplier prices
prices = pd.read_csv("Prices.csv")


# Get the lowest available price for each material
lowest_prices = prices.groupby("material")["unit_price"].min()

print("\nLowest Material Prices:")
print(lowest_prices)


# Calculate total required quantities
cement = required["cement_kg"].sum()
sand = required["sand_m3"].sum()
aggregate = required["aggregate_m3"].sum()


# Material names
materials = ["Cement", "Sand", "Aggregate"]

# Required quantities we used numpy to make the multiplay method easier
quantities = np.array([cement, sand, aggregate])

# Lowest unit prices
unit_prices = np.array([
    lowest_prices["Cement"],
    lowest_prices["Sand"],
    lowest_prices["Aggregate"]
])

# Calculate estimated cost for each material
cost_before = quantities * unit_prices

# Calculate total estimated cost
total_before = np.sum(cost_before)

print("\nEstimated Cost Before Increase:", round(total_before, 2))

# Ask user to select a material
selected_material = input(
    "\nSelect material (Cement, Sand, Aggregate): "
).strip().capitalize()


# Ask user for price increase percentage
increase = float(input("Enter price increase percentage: "))



# Copy original prices
new_prices = unit_prices.copy()

# Find selected material position
material_index = materials.index(selected_material)

# Increase the selected material price
new_prices[material_index] = (
    new_prices[material_index] * (1 + increase / 100)
)

# Calculate costs after increase
cost_after = quantities * new_prices

# Calculate new total estimated cost
total_after = np.sum(cost_after)

# Calculate additional cost
additional_cost = total_after - total_before
# Create cost comparison table
comparison = pd.DataFrame({
    "material": materials,
    "required_quantity": quantities,
    "unit_price_before": unit_prices,
    "unit_price_after": new_prices,
    "cost_before": cost_before,
    "cost_after": cost_after
})

# Calculate cost difference for each material
comparison["cost_difference"] = (
    comparison["cost_after"] - comparison["cost_before"]
)

print("\nMaterial Cost Comparison:")
print(comparison)

print("\nTotal Cost Before:", round(total_before, 2))
print("Total Cost After:", round(total_after, 2))
print("Additional Cost:", round(additional_cost, 2))

# Export results
comparison.to_csv("Price_Increase_Analysis.csv", index=False)






# CHART 1: Daily Cost Variation Before and After Price Increase

# Convert date to datetime
data["date"] = pd.to_datetime(data["date"])

# Calculate cost after price increase
data["new_price"] = data["unit_price"]

# Increase the price of the selected material
data.loc[
    data["material"] == selected_material,
    "new_price"
] *= (1 + increase / 100)

# Calculate new purchase cost
data["cost_after"] = data["quantity"] * data["new_price"]


# Calculate daily costs before increase
daily_before = data.groupby("date")["purchase_cost"].sum().sort_index()

# Calculate daily costs after increase
daily_after = data.groupby("date")["cost_after"].sum().sort_index()


# Calculate daily variation
variation_before = daily_before.diff().fillna(0)

variation_after = daily_after.diff().fillna(0)


# Save comparison to CSV
daily_comparison = pd.DataFrame({
    "cost_before": daily_before,
    "cost_after": daily_after,
    "variation_before": variation_before,
    "variation_after": variation_after
})

daily_comparison.to_csv("Daily_Variation_Comparison.csv")

print(daily_comparison)


# Draw comparison line chart
plt.figure(figsize=(12, 5))

plt.plot(
    variation_before.index,
    variation_before.values,
    marker="o",
    label="Before Increase"
)

plt.plot(
    variation_after.index,
    variation_after.values,
    marker="o",
    label="After Increase"
)

plt.axhline(0, color="black", linestyle="--")

plt.title("Daily Purchase Cost Variation Before and After Price Increase")
plt.xlabel("Date")
plt.ylabel("Daily Cost Variation (currency units)")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



# BAR CHART: Daily Variation After Increase

plt.figure(figsize=(12, 5))

plt.bar(
    variation_after.index,
    variation_after.values,
    label="After Increase"
)

plt.title("Daily Cost Variation After Price Increase")
plt.xlabel("Date")
plt.ylabel("Cost Variation (currency units)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()



# CHART 3: Scatter Chart

plt.figure(figsize=(8, 6))

plt.scatter(
    variation_before.values,
    variation_after.values
)

plt.title("Daily Cost Variation Before vs After Price Increase")
plt.xlabel("Variation Before Increase (currency units)")
plt.ylabel("Variation After Increase (currency units)")

plt.show()



# CHART 4: Histogram

plt.figure(figsize=(10, 5))

plt.hist(
    [variation_before.values, variation_after.values],
    bins=8,
    label=["Before Increase", "After Increase"]
)

plt.title("Daily Cost Variation Distribution")
plt.xlabel("Daily Cost Variation (currency units)")
plt.ylabel("Number of Days (count)")

plt.legend()
plt.tight_layout()
plt.show()