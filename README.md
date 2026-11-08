# Construction Materials Cost Planner

A Python project that calculates concrete material requirements, analyzes construction purchases, and evaluates the effect of material price increases.

## Project Overview

The project includes two connected modules:

- **Module 1 – Material Quantity Calculator:** Calculates concrete volume and required cement, sand, and aggregate for each concrete element, including a fixed **5% waste allowance**.
- **Module 2 – Purchase and Cost Analysis:** Cleans purchase records, calculates quantities and costs by element and supplier, compares required and purchased materials, and uses NumPy to estimate the effect of a selected material's price increase.

## Sample Dataset

| Item | Dataset coverage |
| --- | --- |
| Concrete elements | 8 |
| Construction sites | 2 (Site A and Site B) |
| Materials | Cement, Sand, Aggregate |
| Suppliers | 2 suppliers for each material |
| Purchase records | 40 original records; 35 retained after cleaning |
| Purchase period | August–September 2026 |

## Tools and Libraries

- Python
- Pandas — data cleaning, merging, and analysis
- NumPy — material cost and price-increase calculations
- Matplotlib — charts and visualizations
- Jupyter Notebook — explanation and testing

Install the libraries with:

```bash
pip install pandas numpy matplotlib notebook
```

## How to Run

1. Download or clone this repository.
2. Keep the input CSV files in the same directory as the Python scripts, unless you update the paths in the code.
3. Run **Module 1** first to generate `Material_Requirements.csv`.
4. Run **Module 2** to analyze purchases, select a material, and enter a price-increase percentage.
5. Open `Construction_Materials_Analysis_and_Tests.ipynb` to review the analysis, charts, and test cases.

## Input and Output Files

**Input datasets:** `Element.csv`, `Prices.csv`, `purchases.csv`.

**Generated reports (as available):** `Material_Requirements.csv`, `Purchased_Materials.csv`, `Price_Increase_Analysis.csv`, `Daily_Variation_Comparison.csv`, and `Test_Results.csv`.

**Charts:** `Line_Chart.png`, `Bar_Chart.png`, `Scatter_Chart.png`, and `Histogram_Chart.png`.

**Notebook:** `Construction_Materials_Analysis_and_Tests.ipynb`.

> The notebook package includes an `Element_Summary.csv` for its summary and tests. Include the original `Element.csv` and both Python module scripts in the repository as well.

## Data Analysis and Visualization

- **Line chart:** Daily purchase cost variation before and after a selected material's price increase.
- **Bar chart:** Total purchase cost by supplier.
- **Scatter chart:** Relationship between daily cost variations before and after the increase.
- **Histogram:** Distribution of daily cost variations before and after the increase.

For the price sensitivity analysis, the program uses the **lowest available unit price for each material** as the baseline for estimated required-material costs. The historical purchase-cost comparison uses the recorded supplier prices.

## Testing

The notebook records **3 valid cases and 3 invalid cases** with expected results, actual results, and pass/fail status. The included sample test report records **6 passing tests**.

## Notes

- The sample data and prices are intended for educational analysis.
- The purchase-cost variation chart compares **consecutive recorded purchasing days**, not necessarily consecutive calendar days.
- An increase in total daily purchase cost does not necessarily mean the unit price itself changed; quantities can also affect total cost.

## Author

Mostafa Khaled
