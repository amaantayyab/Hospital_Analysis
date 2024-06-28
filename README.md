# EDA of Hospital Equipment Data

## Project Overview
This project involves the exploratory data analysis (EDA) of a dataset containing information on hospital equipment. The primary objective is to uncover patterns, insights, and anomalies in the data that could inform better decision-making and operational efficiency in hospital equipment management.

## Dataset
The dataset used in this analysis contains the following columns:
- **Serial No**: Unique identifier for each record.
- **Hospital**: Name of the hospital.
- **State**: State where the hospital is located.
- **Location**: Specific location within the state.
- **Department**: Department within the hospital where the equipment is used.
- **Equipment**: Type of equipment.
- **Quantity**: Number of units ordered.
- **Unit Price (USD)**: Price per unit in USD.
- **Supplier**: Name of the supplier.
- **Supplier Contact**: Contact person at the supplier.
- **Supplier Phone**: Phone number of the supplier contact.
- **Supplier Email**: Email address of the supplier contact.
- **Supplier Country**: Country where the supplier is located.
- **Date Ordered**: Date the equipment was ordered.
- **Date Delivered**: Date the equipment was delivered.
- **Warranty Period (Years)**: Warranty period for the equipment.
- **Maintenance Cost (USD/year)**: Annual maintenance cost.
- **Installation Cost (USD)**: Cost of installation.
- **Equipment Condition**: Condition of the equipment (e.g., new, used, refurbished).

## Analysis Steps
1. **Data Preparation**:
    - Imported necessary libraries.
    - Loaded the dataset.
    - Checked for null values and duplicates.
    - Removed duplicates.
    - Removed unnecessary columns.

2. **Exploratory Data Analysis**:
    - **Top 20 Hospitals by Order Quantity**: Visualized using a bar chart.
    - **Number of Hospitals per Country**: Visualized using a horizontal bar chart.
    - **Unique Elements in Each Department**: Visualized using a bar chart.
    - **Distribution of Hospitals per State**: Visualized using a pie chart.
    - **Top 10 Costly Equipment**: Presented in a table.
    - **Count of Orders Made by Top Suppliers**: Visualized using a dot chart.
    - **Time Taken to Deliver in Each Department**: Visualized using a violin chart.
    - **Average Warranty Period per Department**: Visualized using a line chart.
    - **Maintenance Cost per Year per Department**: Visualized using a line chart.
    - **Installation Cost per Department**: Visualized using a line chart.
    - **Distribution of Equipment Condition**: Visualized using a pie chart.

## Key Insights
- Summary of the most significant findings, such as:
  - The top 20 hospitals by order quantity.
  - Distribution of hospitals across different countries and states.
  - Unique elements and the variety within each department.
  - The most expensive equipment and their details.
  - Supplier performance in terms of order counts.
  - Delivery time patterns across departments.
  - Trends in warranty periods, maintenance costs, and installation costs.
  - Condition of the equipment (new, used, refurbished) across hospitals.

## Conclusion
A brief conclusion summarizing the overall findings and their potential implications for hospital equipment management.



