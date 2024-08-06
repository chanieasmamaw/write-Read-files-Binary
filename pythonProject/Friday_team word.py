import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Draw the main rectangle of the house
main_house = patches.Rectangle((0.3, 0.3), 0.4, 0.4, edgecolor='black', facecolor='none')
ax.add_patch(main_house)

# Draw the roof as a triangle
roof = patches.Polygon([[0.3, 0.7], [0.7, 0.7], [0.5, 1.0]], closed=True, edgecolor='black', facecolor='none')
ax.add_patch(roof)

# Draw windows
window1 = patches.Rectangle((0.35, 0.55), 0.1, 0.1, edgecolor='black', facecolor='none')
window2 = patches.Rectangle((0.55, 0.55), 0.1, 0.1, edgecolor='black', facecolor='none')
ax.add_patch(window1)
ax.add_patch(window2)

# Draw the door
door = patches.Rectangle((0.45, 0.3), 0.1, 0.2, edgecolor='black', facecolor='none')
ax.add_patch(door)

# Draw the doorknob
doorknob = patches.Circle((0.53, 0.4), 0.01, edgecolor='black', facecolor='black')
ax.add_patch(doorknob)

# Draw the chimney
chimney = patches.Rectangle((0.6, 0.8), 0.05, 0.15, edgecolor='black', facecolor='none')
ax.add_patch(chimney)

# Set the limits and hide the axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

# Display the drawing
plt.show()
