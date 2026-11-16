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

For this evaluation, I wanted to investigate whether adding interaction to the oat milk preference heatmap improves users' ability to compare purchasing patterns across different times of the day. My hypothesis was that participants using the interactive visualization would complete analytical tasks more quickly than those using the static visualization while maintaining similar or better accuracy.

I designed a within-subject experiment where each participant evaluated both versions of the heatmap. Each participant answered four questions, two using the static version and two using the interactive version. The experiment included two analytical task types: comparing changes in oat milk percentages across time periods and comparing individual hourly percentages with grouped-time percentages. Each task had two comparable variants to reduce memorization effects.

### Analytical Questions and Expected Answers

| Task | Variant | Question | Correct Answer |
|---|---|---|---|
| Change | A | Which drink has the largest increase in oat milk percentage from 9–10 AM to 11 AM–12 PM? | Latte |
| Change | B | Which drink has the largest increase in oat milk percentage from 11 AM–12 PM to 1–3 PM? | Matcha Latte |
| Aggregation | A | For Latte, how many percentage points does the 9 AM oat milk percentage differ from the 9–10 AM grouped percentage? | 5 |
| Aggregation | B | For Matcha Latte, how many percentage points does the 10 AM oat milk percentage differ from the 9–10 AM grouped percentage? | 3 |

### Counterbalancing

To reduce potential learning effects, I divided the 10 participants into four groups. Five participants started with the static visualization, while the other five started with the interactive visualization. I also distributed the question variants across both conditions so that the same questions were not always assigned to the same visualization.

| Participants | First Condition | Second Condition |
|---|---|---|
| P001–P003 | Static (A) | Interactive (B) |
| P004–P005 | Static (B) | Interactive (A) |
| P006–P008 | Interactive (A) | Static (B) |
| P009–P010 | Interactive (B) | Static (A) |

Each participant completed one change question and one aggregation question under each condition.

### Evaluation Procedure

Before beginning the experiment, I explained that the heatmaps displayed the percentage of customers selecting oat milk for different drinks across different times of the day. I also explained what the percentages and sample sizes represented and demonstrated how to switch between the hourly and grouped-time views in the interactive visualization. Participants were instructed to answer each question as quickly and accurately as possible. I measured completion time in seconds, starting when the participant was presented with the question and stopping when they provided their final answer. Each question had a maximum time limit of 90 seconds.

I recorded two quantitative measurements which were Accuracy and Completion time. A value of 1 meant a correct response, while 0 meant an incorrect response. Questions that were unanswered after 90 seconds were recorded as incorrect, with a completion time of 90 seconds. I also recorded whether a participant timed out and documented any difficulties they experienced while interpreting the visualization. Before the main study, I conducted a pilot evaluation with two participants to check whether the questions and instructions were understandable. Based on their feedback, I provided more standardized instructions explaining the visualization before the main experiment. All measurements were recorded in a CSV file using anonymous participant identifiers. The pilot participants were excluded from the main analysis.


## Task 3: Conducting the Evaluation

Before conducting the main evaluation, I performed a pilot study with 2 participants to identify any potential issues with the questions and visualization controls. For the main evaluation, I recruited 10 participants who were not members of my project group. Each participant completed four analytical questions, two using the static visualization and two using the interactive visualization. The questions were:

Which drink has the largest increase in oat milk percentage from 9–10 AM to 11 AM–12 PM?

For Latte, how many percentage points do the 9 AM oat milk percentage differ from the 9–10 AM grouped percentage?

Which drink has the largest increase in oat milk percentage from 11 AM–12 PM to 1–3 PM?

For Matcha Latte, how many percentage points does the 10 AM oat milk percentage differ from the 9–10 AM grouped percentage?

The answers were respectively: Latte, 5, Matcha, and 3.

I used a within-subject design and counterbalanced the order of the two conditions to reduce learning effects. The participants were asked to answer each question as quickly and accurately as possible. For each question, I recorded the participant's response, whether the answer was correct, and the time required to complete the task in seconds. The results were organized in a CSV file using anonymous participant identifiers.

## Pilot Evaluation

Before conducting the main study, I performed a pilot evaluation with two participants, P011 and P012, to identify potential issues with the questions and visualization design. Both participants completed four questions, using both static and interactive visualizations. P011 began with the static version, while P012 began with the interactive version. The pilot results showed that the static visualization had an accuracy of 100%, compared to 75% for the interactive version. The average completion time was 9.5 seconds for the static visualization and 24.5 seconds for the interactive visualization. However, I noticed that both participants initially experienced confusion when interpreting the numbers and layout. Their completion times generally decreased after becoming familiar with the visualization, suggesting a possible learning effect. Based on these observations, I decided to provide standardized instructions explaining the percentages, sample sizes, and interaction controls before participants begin the main evaluation. This should reduce confusion caused by unfamiliarity with the visualization. The pilot participants will not be included in the main evaluation dataset or quantitative analysis.



## Task 4

For this task, I analyzed the results collected from the 10 participants in the main study, excluding the two pilot participants. Each participant answered four questions, two using the static heatmap and two using the interactive heatmap, giving a total of 40 observations. I used Python and Pandas to calculate descriptive statistics, including average accuracy, mean completion time, median completion time, and standard deviation. I also created graphs to compare the performance of the two visualizations.

### Overall Accuracy and Completion Time

| Condition | Correct Answers | Accuracy | Average Time (s) | Median Time (s) | Standard Deviation (s) |
|---|---|---|---|---|---|
| Static | 17/20 | 85% | 18.55 | 17.0 | 9.22 |
| Interactive | 18/20 | 90% | 22.00 | 17.5 | 17.31 |

<img width="1260" height="827" alt="task4_completion_time" src="https://github.com/user-attachments/assets/80f61d07-a853-4ab4-9b48-f860af3c1f92" />

<img width="1260" height="827" alt="task4_accuracy" src="https://github.com/user-attachments/assets/3a5d48ca-a4d4-49f0-b06d-8936a4861a72" />


From the results, the interactive visualization had a slightly higher accuracy of 90% compared to 85% for the static visualization. However, the static version had a faster average completion time of 18.55 seconds, compared to 22 seconds for the interactive version. One important observation was that the interactive version had a higher standard deviation, meaning participants' completion times varied more. This was partly due to participant P06 reaching the 90-second time limit on one question. The median completion times were almost identical, with 17 seconds for static and 17.5 seconds for interactive. This suggests that the difference between the averages was influenced by unusually long completion times rather than a consistent difference between the visualizations.

### Comparing Different Analytical Tasks

I also compared the results based on the two types of analytical questions: identifying changes in oat milk preferences across time periods and comparing hourly percentages with grouped percentages.

| Task Type | Static Accuracy | Interactive Accuracy | Static Avg. Time | Interactive Avg. Time |
|---|---|---|---|---|
| Comparing changes | 90% | 100% | 21.9 s | 19.3 s |
| Comparing aggregation | 80% | 80% | 15.2 s | 24.7 s |


<img width="1800" height="810" alt="task4_by_task" src="https://github.com/user-attachments/assets/05583ea7-3920-4346-98e0-99dfa7fe93d0" />

For questions involving changes across time periods, participants performed slightly better with the interactive visualization. They achieved 100% accuracy and completed the questions faster on average. However, for questions involving hourly and grouped percentages, both visualizations had the same accuracy of 80%. Participants took longer using the interactive version, although this result was influenced by the 90-second timeout. This suggests that interaction may be more beneficial for certain analytical tasks than others.

### Differences Between Participants

<img width="1620" height="882" alt="task4_participants" src="https://github.com/user-attachments/assets/4c51c32c-44ec-41bd-952a-ee3569948a2d" />

Looking at individual participants, I noticed that the interactive visualization did not affect everyone in the same way. For example, P04 completed interactive questions in an average of 14.5 seconds compared to 25.5 seconds for static questions. Similarly, P08 completed interactive questions faster, averaging 18 seconds compared to 34.5 seconds for static questions. However, P06 took an average of 60.5 seconds with the interactive visualization compared to 15.5 seconds with the static visualization. This difference was largely caused by the participant reaching the 90-second time limit. I also considered whether the order of the visualizations affected performance. Participants who started with the static visualization had an average interactive completion time of 15.1 seconds, while participants who started with the interactive visualization averaged 28.9 seconds. This may indicate a learning effect, although the small sample size and the timeout make it difficult to draw a definite conclusion.

### Interpretation of Results

My original hypothesis was that the interactive visualization would help participants complete the analytical tasks faster while maintaining similar or better accuracy. The results partially supported this hypothesis. The interactive visualization had slightly better overall accuracy, but its average completion time was longer than the static version. One possible explanation is that the interactive controls introduced additional steps or unfamiliarity for some participants. However, for tasks involving changes between time periods, the interactive version appeared to be useful. Overall, the results suggest that interaction does not automatically improve visualization performance. Its effectiveness depends on the type of analytical task and how comfortable participants are with the interface. There were also limitations to this evaluation. The study only had 10 participants, some participants may have benefited from learning effects, and unusual completion times affected the overall averages. Because of these limitations, I cannot conclude that either visualization is universally better. Instead, the experiment demonstrates that both static and interactive visualizations have different strengths depending on the analytical task.

## Task 5

Through this asssignment, I learned that adding interaction to a visualization does not necessarily make it more effective. Although the interactive heatmap had a slightly higher accuracy of 90% compared to 85% for the static version, participants took longer on average to complete the questions. One strength of the interactive visualization was that users could switch between hourly and grouped-time views, allowing them to explore the data at different levels of detail. However, this also introduced additional steps that may have slowed participants down. During the pilot study, I noticed that some participants initially struggled to understand the numbers and layout, which could mean that familiarity with the visualization affected their performance. Based on these observations, I would improve the interactive heatmap by adding clearer instructions, making the dropdown easier to understand, and allowing users to compare both time groupings side by side instead of switching between them.

One limitation of this evaluation was the small sample size of 10 participants, which makes it hard to generalize the results. Additionally, participants may have experienced learning effects because they used both versions, and one participant's 90-second timeout affected the average completion time. Overall, this assignment demonstrated that interaction can be useful for certain analytical tasks, but it does not automatically improve performance. The effectiveness of a visualization depends on how information is presented and how easily users can interpret it.
