import matplotlib.pyplot as plt

# Data for the chart
categories = ['Total Identified', 'Completed Questionnaire']
values = [200, 80]

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(categories, values, color=['#3b5998', '#00aced'])

# Adding values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 5, int(yval), ha='center', va='bottom', fontsize=12, fontweight='bold')

# Title and labels
plt.title('Population Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Number of Participants', fontsize=12)
plt.ylim(0, 250)

# Display the chart
plt.show()
