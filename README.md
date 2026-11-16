## Task 1

For this assignment, I decided to continue using the oat milk preference heatmap from Assignment 2. The visualization compares the percentage of customers who selected oat milk for three drinks: Latte, Matcha Latte, and Chai Latte, across different times of the day. I created two versions of the visualization. A static version using Matplotlib and an interactive version using Plotly. Both versions use the same cleaned Cor Coffee dataset and calculate oat milk percentages in the same way.

**Static Visualization**

The static version displays two heatmaps one that shows oat milk preferences by individual hour and another that groups the hours into broader time periods. Both heatmaps are displayed together so users can compare patterns without needing any interaction.

<img width="2160" height="1440" alt="static_heatmaps" src="https://github.com/user-attachments/assets/aee58f09-eb6d-4962-8c33-c16e720b47cb" />

**Interactive Visualization**

For the interactive version, I implemented a dropdown menu that allows users to switch between individual hours and grouped time periods. This changes the level of time aggregation displayed in the heatmap.

The interactive visualization also allows users to hover over cells to inspect the corresponding values and sample sizes. Both versions display sample sizes and flag groups containing fewer than eight observations to avoid presenting potentially misleading percentages.

The heatmap can be seen in the html file uploaded.

**Purpose of the Interaction**

The main purpose of this interaction is to allow users to see how oat milk preferences changes depending on the time of day. Switching between hourly and grouped views allows users to identify more detailed patterns or observe broader trends. My hypothesis is that that the interactive version makes it easier for users to compare patterns at different levels of time aggregation because they can switch between views without examining two separate charts. 
