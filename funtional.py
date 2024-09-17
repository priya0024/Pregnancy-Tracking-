import matplotlib.pyplot as plt
import numpy as np

# Data for the chart
categories = [
    'User Registration and Authentication', 
    'Profile Management', 
    'Pregnancy Tracking', 
    'Appointment Scheduling', 
    'Educational Resources', 
    'Community and Support', 
    'Data Visualization', 
    'Notifications and Reminders',
    'Usability', 
    'Performance', 
    'Security', 
    'Compatibility', 
    'Scalability', 
    'Accessibility', 
    'Maintainability', 
    'Data Backup and Recovery'
]

requirement_types = ['Functional', 'Non-Functional']
functional_counts = [1, 1, 1, 1, 1, 1, 1, 1]  # 8 functional requirements
non_functional_counts = [1, 1, 1, 1, 1, 1, 1, 1]  # 8 non-functional requirements

# Create the bar chart
x = np.arange(len(categories))  # the label locations
width = 0.4  # the width of the bars

fig, ax = plt.subplots(figsize=(12, 8))

# Plot bars for functional and non-functional requirements
bars1 = ax.bar(x - width/2, functional_counts + [0]*8, width, label='Functional', color='#007bff')
bars2 = ax.bar(x + width/2, [0]*8 + non_functional_counts, width, label='Non-Functional', color='#ff5722')

# Adding labels to the bars
for bar in bars1:
    yval = bar.get_height()
    if yval != 0:
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=10)

for bar in bars2:
    yval = bar.get_height()
    if yval != 0:
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=10)

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_xlabel('Requirements', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Detailed Breakdown of Functional and Non-Functional Requirements', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right', fontsize=10)
ax.legend()

# Display the chart
plt.tight_layout()
plt.show()
