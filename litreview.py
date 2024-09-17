import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace with actual values from the PDF)
apps = ['App 1', 'App 2', 'App 3', 'App 4', 'App 5', 'App 6', 'App 7', 'App 8', 'App 9', 'App 10']
usability_scores = [78, 83, 77, 84, 88, 70, 72, 81, 86, 89]
content_quality_scores = [80, 85, 75, 82, 87, 68, 71, 79, 85, 90]
overall_scores = [79, 84, 76, 83, 87, 69, 71, 80, 86, 89]

# X-axis positions
x = np.arange(len(apps))
width = 0.25  # Width of the bars

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot bars for each category
bars1 = ax.bar(x - width, usability_scores, width, label='Usability', color='skyblue')
bars2 = ax.bar(x, content_quality_scores, width, label='Content Quality', color='lightgreen')
bars3 = ax.bar(x + width, overall_scores, width, label='Overall Score', color='salmon')

# Add labels and title
ax.set_xlabel('Apps', fontsize=12)
ax.set_ylabel('Scores', fontsize=12)
ax.set_title('Detailed Assessment of Popular Pregnancy Apps in Australia', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(apps, rotation=45)
ax.legend()

# Display scores on top of bars
def add_labels(bars):
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=10)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

# Show plot
plt.tight_layout()
plt.show()
