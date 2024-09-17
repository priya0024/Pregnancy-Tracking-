import matplotlib.pyplot as plt

# Sample data for demonstration
# Age distribution
age_groups = ['18-24', '25-30', '31-35', '36-40', '41-45']
age_counts = [10, 30, 25, 10, 5]

# Occupation distribution
occupations = ['Healthcare', 'Teachers', 'IT Professionals', 'Homemakers', 'Students', 'Others']
occupation_counts = [15, 10, 20, 15, 10, 10]

# Education Level
education_levels = ['High School', 'College', 'Bachelor\'s', 'Master\'s', 'Doctorate']
education_counts = [10, 20, 30, 15, 5]

# Plot Age Distribution
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.bar(age_groups, age_counts, color='#3b5998')
plt.title('Age Distribution')
plt.xlabel('Age Groups')
plt.ylabel('Number of Participants')

# Plot Occupation Distribution
plt.subplot(2, 2, 2)
plt.barh(occupations, occupation_counts, color='#00aced')
plt.title('Occupation Distribution')
plt.xlabel('Number of Participants')
plt.ylabel('Occupation')

# Plot Education Level Distribution
plt.subplot(2, 2, 3)
plt.pie(education_counts, labels=education_levels, autopct='%1.1f%%', startangle=140, colors=['#f4b400', '#4285f4', '#ea4335', '#34a853', '#ff6f00'])
plt.title('Education Level Distribution')

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
