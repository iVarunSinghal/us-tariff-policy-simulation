# US Tariff Policy & Trade Diversion Simulator
**An interactive analytics engine modeling supply chain cost impacts and macroeconomic nearshoring trends driven by Section 301 tariffs (2018–2026).**

![Dashboard Preview](images/01_Simulator.png) 
*(Note: Replace with your actual Page 1 screenshot link)*

## 📌 Executive Summary
This project provides a comprehensive quantitative view of US trade policy impacts on the electronics sector (HS Chapters 84 & 85). Built in Power BI, the dashboard enables supply chain leaders and trade compliance teams to simulate landed cost shocks, visualize downstream margin compression, and track the structural shift of import volumes away from China toward alternative manufacturing hubs.

**[View the Static PDF Version Here](link_to_your_exported_pdf.pdf)**

## ⚙️ Core Analytical Features

* **Dynamic Cost-Buildup Simulator:** Utilizes DAX What-If parameters to rebuild FOB-to-Consumer pricing structures under 5 distinct policy scenarios. A conditional waterfall chart dynamically separates standard logistics and importer markups from statutory policy penalties.
* **Margin Sensitivity Heatmap:** A dual-axis matrix measuring the compounding interaction between statutory tariff rates and importer margin behavior, utilizing custom gradient logic to highlight downstream inflation risks.
* **Trade Diversion Analytics:** Evaluates market share displacement from 2017 to 2024. A 100% stacked column chart proves the macroeconomic rewiring of supply chains, highlighting the proportional volume crossover between China, Mexico, and Vietnam.
* **Cumulative Policy Timeline:** A stepped line chart powered by custom DAX time-intelligence filtering, plotting the statutory escalation of Section 301 and IEEPA actions against major bilateral trade events.

## 🛠️ Technical Architecture & Skills Demonstrated

* **Data Modeling:** Star schema architecture bridging transactional tariff event logs with longitudinal trade volume aggregates.
* **Advanced DAX:** Implementation of custom time-intelligence measures (e.g., cumulative statutory rate calculation filtering for active HS chapters and origin countries).
* **UI/UX Design:** Executive "dark mode" terminal aesthetic (`#152235` background) maximizing contrast and readability. Semantic color-coding applied globally (Green = Savings/Baseline, Amber = Status Quo, Red = Inflationary Shock) to reduce cognitive load.
* **Conditional Formatting:** Automated visual cues (color-shifting KPIs, gradient matrices) driven by underlying model rules rather than static assignments.

## 📈 Key Business Insights Generated

1. **The Compounding Margin Effect:** At a 25% statutory tariff rate, standard percentage-based importer margins disproportionately inflate the final consumer price, demonstrating that supply chains amplify, rather than absorb, baseline policy shocks.
2. **Structural Nearshoring:** Between 2017 and 2023, China's combined import share in Chapters 84/85 dropped from ~48% to ~29%. Concurrently, Vietnam's share rose from 4% to 18%, proving that Section 301 rewired physical supply chains rather than merely serving as a consumption tax.

## 🚀 How to Run the Project
1. Download the `Tariff_Simulator_Final.pbix` file from this repository.
2. Open with [Power BI Desktop](https://powerbi.microsoft.com/desktop/).
3. Use the page navigator at the bottom of the canvas to cycle through the interactive models.
