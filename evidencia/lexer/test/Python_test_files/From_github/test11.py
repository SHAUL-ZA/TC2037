import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 4, figsize=(12, 12))

# Draw a circle
circle = plt.Circle((0.5, 0.5), 0.4, color='blue', alpha=0.5)
axs[0, 0].add_patch(circle)
axs[0, 0].set_aspect('equal')
axs[0, 0].set_xlim(0, 1)
axs[0, 0].set_ylim(0, 1)
axs[0, 0].set_title('Circle')

# Draw a rectangle
rectangle = plt.Rectangle((0.2, 0.2), 0.6, 0.4, color='red', alpha=0.5)
axs[0, 1].add_patch(rectangle)
axs[0, 1].set_aspect('equal')
axs[0, 1].set_xlim(0, 1)
axs[0, 1].set_ylim(0, 1)
axs[0, 1].set_title('Rectangle')

# Draw an ellipse
ellipse = plt.Ellipse((0.5, 0.5), 0.6, 0.4, angle=45, color='green', alpha=0.5)
axs[0, 2].add_patch(ellipse)
axs[0, 2].set_aspect('equal')
axs[0, 2].set_xlim(0, 1)
axs[0, 2].set_ylim(0, 1)
axs[0, 2].set_title('Ellipse')

# Draw a triangle
triangle = plt.Polygon([[0.3, 0.7], [0.7, 0.7], [0.5, 0.3]], color='purple', alpha=0.5)
axs[0, 3].add_patch(triangle)
axs[0, 3].set_aspect('equal')
axs[0, 3].set_xlim(0, 1)
axs[0, 3].set_ylim(0, 1)
axs[0, 3].set_title('Triangle')

# Draw a pentagon
pentagon = plt.Polygon([[0.3, 0.8], [0.7, 0.8], [0.8, 0.6], [0.5, 0.2], [0.2, 0.6]], color='orange', alpha=0.5)
axs[1, 0].add_patch(pentagon)
axs[1, 0].set_aspect('equal')
axs[1, 0].set_xlim(0, 1)
axs[1, 0].set_ylim(0, 1)
axs[1, 0].set_title('Pentagon')

# Draw a star
star = plt.Polygon([[0.5, 0.9], [0.63, 0.6], [0.95, 0.6], [0.68, 0.4], [0.8, 0.1],
                    [0.5, 0.3], [0.2, 0.1], [0.32, 0.4], [0.05, 0.6], [0.37, 0.6]],
                   color='brown', alpha=0.5)
axs[1, 1].add_patch(star)
axs[1, 1].set_aspect('equal')
axs[1, 1].set_xlim(0, 1)
axs[1, 1].set_ylim(0, 1)
axs[1, 1].set_title('Star')

# Draw an arrow
arrow = plt.Arrow(0.2, 0.5, 0.6, 0.2, width=0.1, color='magenta')
axs[1, 2].add_patch(arrow)
axs[1, 2].set_aspect('equal')
axs[1, 2].set_xlim(0, 1)
axs[1, 2].set_ylim(0, 1)
axs[1, 2].set_title('Arrow')

# Draw a hexagon
hexagon = plt.Polygon([[0.3, 0.8], [0.7, 0.8], [0.9, 0.5], [0.7, 0.2], [0.3, 0.2], [0.1, 0.5]],
                      color='cyan', alpha=0.5)
axs[1, 3].add_patch(hexagon)
axs[1, 3].set_aspect('equal')
axs[1, 3].set_xlim(0, 1)
axs[1, 3].set_ylim(0, 1)
axs[1, 3].set_title('Hexagon')

# Draw an octagon
octagon = plt.Polygon([[0.3, 0.7], [0.7, 0.7], [0.9, 0.5], [0.9, 0.1], [0.7, 0.3], [0.3, 0.3], [0.1, 0.5], [0.1, 0.9]],
                      color='lime', alpha=0.5)
axs[2, 0].add_patch(octagon)
axs[2, 0].set_aspect('equal')
axs[2, 0].set_xlim(0, 1)
axs[2, 0].set_ylim(0, 1)
axs[2, 0].set_title('Octagon')

# Draw a trapezoid
trapezoid = plt.Polygon([[0.2, 0.8], [0.8, 0.8], [0.7, 0.5], [0.3, 0.5]], color='yellow', alpha=0.5)
axs[2, 1].add_patch(trapezoid)
axs[2, 1].set_aspect('equal')
axs[2, 1].set_xlim(0, 1)
axs[2, 1].set_ylim(0, 1)
axs[2, 1].set_title('Trapezoid')

# Draw a diamond
diamond = plt.Polygon([[0.5, 0.9], [0.75, 0.5], [0.5, 0.1], [0.25, 0.5]], color='pink', alpha=0.5)
axs[2, 2].add_patch(diamond)
axs[2, 2].set_aspect('equal')
axs[2, 2].set_xlim(0, 1)
axs[2, 2].set_ylim(0, 1)
axs[2, 2].set_title('Diamond')

# Draw a cross
cross = plt.Polygon([[0.4, 0.8], [0.6, 0.8], [0.6, 0.6], [0.8, 0.6], [0.8, 0.4], [0.6, 0.4],
                     [0.6, 0.2], [0.4, 0.2], [0.4, 0.4], [0.2, 0.4], [0.2, 0.6], [0.4, 0.6]],
                    color='gray', alpha=0.5)
axs[2, 3].add_patch(cross)
axs[2, 3].set_aspect('equal')
axs[2, 3].set_xlim(0, 1)
axs[2, 3].set_ylim(0, 1)
axs[2, 3].set_title('Cross')

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
