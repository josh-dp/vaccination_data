# SARS-CoV-2 Vaccination Data from Cantons of Switzerland and Liechtenstein
The repository contains the scripts and data scraped from the 26 cantons of Switzerland and the principality of Liechtenstein.

# Overview of Information
The following data regarding vaccinations was used to build visualizations:
* First Doses and First Doses per 100
* Second Doses and Second Doses per 100
* Total Vaccinations and Total Vaccinations per 100
* Doses Delivered
* Doses Used (measured in percentages)
Booster shots are not included in this project

The diagrams built from this project include a table listing all cantons and Liechtenstein with their respective vaccination data and separate graphs for each region.

Statistics and how often vaccination data is updated vary widely across each location. Make sure to take a close look at the scales of the y-axis (vaccines/doses delivered) and x-axis (date/time) to ensure a complete understanding of each region's vaccine information. Some graphs do not contain the date-by-date or total doses delivered (orange line).
Hover over each bar of the graph to see how many vaccinations were completed on that date and the total vaccinations up to that date.

# Building Visualizations
All cvs's and tables for each individual municipality are built from different scrapers, in which the information found in the url for each region's health administration website is parsed for the necessary data. The overview table showcasing each region's information uses the latest data found from each cvs.

Plotly was used to generate the graphs for each municipality.

An overview is available [here](https://maekke.github.io/visualize_vaccinations_overview.html).

A visualization is available [here](https://maekke.github.io/visualize_vaccinations.html).

# License
(Enter choice of license here)
