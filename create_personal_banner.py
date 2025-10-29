"""
Create a professional GitHub profile banner for Shanteria Johnson.
This banner features confetti and personal branding.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon
import numpy as np
from PIL import Image

# Set up the figure with a professional aspect ratio for GitHub banners
# Recommended size: 1280x640 pixels (2:1 ratio)
fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Create a gradient background with vibrant colors for celebratory feel
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))

# Create multiple gradient layers for depth - using a celebratory color scheme
extent = [0, 100, 0, 50]
colors1 = plt.cm.twilight_shifted(gradient)
ax.imshow(colors1, aspect='auto', extent=extent, alpha=0.6, zorder=0)

# Add confetti pieces (colorful rectangles and shapes scattered around)
np.random.seed(42)  # For consistent confetti placement

confetti_colors = ['#FF6B9D', '#C44569', '#FFC312', '#12CBC4', '#A3CB38', 
                   '#FDA7DF', '#ED4C67', '#F79F1F', '#EE5A6F', '#C4E538',
                   '#4834DF', '#30336B', '#6F1E51', '#B33771', '#FD7272']

# Add various confetti shapes
for i in range(80):
    x = np.random.uniform(5, 95)
    y = np.random.uniform(5, 48)
    
    shape_type = np.random.choice(['rect', 'circle', 'triangle'])
    color = np.random.choice(confetti_colors)
    rotation = np.random.uniform(0, 360)
    
    if shape_type == 'rect':
        width = np.random.uniform(0.8, 2.5)
        height = np.random.uniform(0.3, 1.2)
        rect = FancyBboxPatch((x, y), width, height,
                             boxstyle="round,pad=0.05",
                             facecolor=color, edgecolor='none',
                             alpha=0.7, zorder=1)
        # Apply rotation
        t = plt.matplotlib.transforms.Affine2D().rotate_deg_around(x + width/2, y + height/2, rotation) + ax.transData
        rect.set_transform(t)
        ax.add_patch(rect)
    elif shape_type == 'circle':
        radius = np.random.uniform(0.3, 1.2)
        circle = Circle((x, y), radius, color=color, alpha=0.7, zorder=1)
        ax.add_patch(circle)
    else:  # triangle
        size = np.random.uniform(1, 2.5)
        triangle = Polygon([(x, y), (x + size, y), (x + size/2, y + size)],
                          facecolor=color, edgecolor='none', alpha=0.7, zorder=1)
        t = plt.matplotlib.transforms.Affine2D().rotate_deg_around(x + size/2, y + size/2, rotation) + ax.transData
        triangle.set_transform(t)
        ax.add_patch(triangle)

# Add main name with shadow effect for depth
name_shadow = ax.text(50, 32, 'Shanteria Johnson', 
                      fontsize=58, weight='bold', ha='center', va='center',
                      color='#1a1a1a', alpha=0.4, zorder=2,
                      family='sans-serif')

name = ax.text(50, 32.5, 'Shanteria Johnson', 
               fontsize=58, weight='bold', ha='center', va='center',
               color='white', zorder=3,
               family='sans-serif')

# Add title/subtitle
subtitle = ax.text(50, 23, 'Aspiring Business Intelligence Analyst', 
                  fontsize=28, ha='center', va='center',
                  color='#FFE4E1', zorder=3, weight='normal',
                  family='sans-serif', style='italic')

# Add decorative line
line_y = 18
ax.plot([20, 80], [line_y, line_y], color='white', linewidth=2.5, alpha=0.8, zorder=3)

# Add some sparkle/star effects
star_positions = [(15, 42), (85, 43), (25, 12), (75, 10), (92, 28), (8, 20)]
for sx, sy in star_positions:
    # Create a star effect with lines
    star_size = 1.5
    ax.plot([sx - star_size, sx + star_size], [sy, sy], color='white', linewidth=2, alpha=0.8, zorder=3)
    ax.plot([sx, sx], [sy - star_size, sy + star_size], color='white', linewidth=2, alpha=0.8, zorder=3)
    ax.plot([sx - star_size*0.7, sx + star_size*0.7], [sy - star_size*0.7, sy + star_size*0.7], 
            color='white', linewidth=1.5, alpha=0.8, zorder=3)
    ax.plot([sx - star_size*0.7, sx + star_size*0.7], [sy + star_size*0.7, sy - star_size*0.7], 
            color='white', linewidth=1.5, alpha=0.8, zorder=3)

# Add bottom tagline
tagline = ax.text(50, 8, 'Data-Driven | Insights | Analytics | Success', 
                 fontsize=18, ha='center', va='center',
                 color='#FFE4E1', alpha=0.95, zorder=3,
                 family='sans-serif', style='italic')

# Save the banner
plt.tight_layout(pad=0)
plt.savefig('images/github_banner.png', dpi=80, bbox_inches='tight', 
           facecolor='none', edgecolor='none', transparent=False)
print("✅ GitHub banner created successfully: images/github_banner.png")
print("📐 Dimensions: 1280x640 pixels")
print("🎉 Featuring: Shanteria Johnson | Aspiring Business Intelligence Analyst | Confetti")

plt.close()
