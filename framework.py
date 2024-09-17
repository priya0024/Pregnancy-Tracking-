import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.patches import FancyArrowPatch

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Function to draw boxes
def draw_box(ax, text, xy, color):
    ax.add_patch(FancyBboxPatch(xy, 2.5, 1, boxstyle="round,pad=0.3", ec=color, fc=color, lw=1.5))
    ax.text(xy[0] + 1.25, xy[1] + 0.5, text, va='center', ha='center', fontsize=10, color='white', fontweight='bold')

# Draw boxes
draw_box(ax, "Knowledge of Mother", (0, 7), '#3b5998')  # Dark blue
draw_box(ax, "Help from Friends\nand Relatives", (0, 5), '#00aced')  # Light blue
draw_box(ax, "Attitude of Pregnant\nWomen", (0, 3), '#e52d27')  # Red
draw_box(ax, "Online System", (0, 1), '#3b5998')  # Dark blue
draw_box(ax, "Better Health", (5, 4.5), '#f4b400')  # Yellow

# Draw arrows
def draw_arrow(start, end):
    arrow = FancyArrowPatch(start, end, connectionstyle="arc3,rad=0", color="black", lw=2, arrowstyle='-|>')
    ax.add_patch(arrow)

# Connect boxes to "Better Health"
draw_arrow((2.5, 7.5), (5, 5))  # Knowledge of Mother to Better Health
draw_arrow((2.5, 6), (5, 5))  # Help from Friends to Better Health
draw_arrow((2.5, 4), (5, 5))  # Attitude of Pregnant Women to Better Health
draw_arrow((2.5, 2), (5, 5))  # Online System to Better Health

# Set axis limits and hide axes
ax.set_xlim(-1, 8)
ax.set_ylim(0, 9)
ax.axis('off')

# Show plot
plt.show()
