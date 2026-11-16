## Task 1

For this assignment, I decided to continue using the oat milk preference heatmap from Assignment 2. The visualization compares the percentage of customers who selected oat milk for three drinks: Latte, Matcha Latte, and Chai Latte, across different times of the day. I created two versions of the visualization. A static version using Matplotlib and an interactive version using Plotly. Both versions use the same cleaned Cor Coffee dataset and calculate oat milk percentages in the same way.

**Static Visualization**

The static version displays two heatmaps one that shows oat milk preferences by individual hour and another that groups the hours into broader time periods. Both heatmaps are displayed together so users can compare patterns without needing any interaction.

<img width="2160" height="1440" alt="static_heatmaps" src="https://github.com/user-attachments/assets/aee58f09-eb6d-4962-8c33-c16e720b47cb" />

**Interactive Visualization**

For the interactive version, I implemented a dropdown menu that allows users to switch between individual hours and grouped time periods. This changes the level of time aggregation displayed in the heatmap.

The interactive visualization also allows users to hover over cells to inspect the corresponding values and sample sizes. Both versions display sample sizes and flag groups containing fewer than eight observations to avoid presenting potentially misleading percentages.

The heatmap can be seen in the html file uploaded.




## Task 2

For this evaluation, I wanted to investigate whether adding interaction to the oat milk preference heatmap improves users' ability to compare purchasing patterns across different times of the day. My hypothesis is that participants using the interactive visualization will complete analytical tasks more quickly than those using the static visualization, while maintaining similar accuracy.

I designed a within-subject experiment in which every participant evaluates both versions of the heatmap. Each participant answers four questions, two using the static version and two using the interactive version.

The evaluation includes two analytical task types. The first involves comparing changes in oat milk percentages across different time periods. The second involves comparing individual hourly percentages with their corresponding grouped-time percentages. Each task has two comparable question variants to reduce the possibility of participants remembering answers. To reduce ordering effects, five participants will begin with the static visualization and five with the interactive visualization. The question variants will also be distributed across both conditions.

I will collect two quantitative measurements for each question:

- **Accuracy:** Whether the participant provides the correct answer, recorded as 1 for correct and 0 for incorrect.
- **Completion time:** The number of seconds required to answer the question.

Before conducting the main study, I will test the procedure with one or two pilot participants to identify unclear instructions, unavailable data values, or questions that are too easy or difficult.

All participants will receive the same instructions and use the same testing procedure. They will be asked to answer each question as accurately and quickly as possible, with a maximum of 90 seconds per question. Unanswered or timed-out questions will be counted as incorrect, and their completion time will be recorded as 90 seconds.

The results will be stored in a CSV file using anonymous participant identifiers, along with the visualization condition, question variant, participant response, accuracy, and completion time.

**Purpose of the Interaction**

The main purpose of this interaction is to allow users to see how oat milk preferences changes depending on the time of day. Switching between hourly and grouped views allows users to identify more detailed patterns or observe broader trends. My hypothesis is that that the interactive version makes it easier for users to compare patterns at different levels of time aggregation because they can switch between views without examining two separate charts. 

