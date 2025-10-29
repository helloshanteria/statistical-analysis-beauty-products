"""
Create a professional GitHub profile banner for the Customer Sales Insights project.
This banner showcases the data analytics project with a modern, visually appealing design.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np
from PIL import Image

# Set up the figure with a professional aspect ratio for GitHub banners
# Recommended size: 1280x640 pixels (2:1 ratio)
fig, ax = plt.subplots(figsize=(16, 8), dpi=80)
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)
ax.axis('off')

# Create a gradient background (beauty/cosmetics inspired colors)
# Using a sophisticated gradient from deep purple to pink
gradient = np.linspace(0, 1, 256).reshape(1, -1)
gradient = np.vstack((gradient, gradient))

# Create multiple gradient layers for depth
extent = [0, 100, 0, 50]
colors1 = plt.cm.twilight(gradient)
ax.imshow(colors1, aspect='auto', extent=extent, alpha=0.7, zorder=0)

# Add decorative circles (representing data points/bubbles)
circle_colors = ['#FF69B4', '#FFB6C1', '#DDA0DD', '#E6E6FA', '#FFC0CB']
circle_positions = [
    (15, 40, 4), (85, 45, 3.5), (20, 10, 3), (90, 12, 4.5),
    (75, 35, 2.5), (10, 25, 2), (95, 25, 2.8), (30, 45, 2.2)
]

for x, y, r in circle_positions:
    circle = Circle((x, y), r, color=np.random.choice(circle_colors), 
                   alpha=0.3, zorder=1)
    ax.add_patch(circle)

# Add main title with shadow effect for depth
title_shadow = ax.text(50, 35, 'Customer Sales Insights', 
                      fontsize=52, weight='bold', ha='center', va='center',
                      color='#1a1a1a', alpha=0.3, zorder=2,
                      family='sans-serif', style='italic')

title = ax.text(50, 35.5, 'Customer Sales Insights', 
               fontsize=52, weight='bold', ha='center', va='center',
               color='white', zorder=3,
               family='sans-serif', style='italic')

# Add subtitle with project focus
subtitle = ax.text(50, 27, 'Beauty Trends Analytics in Atlanta, GA', 
                  fontsize=24, ha='center', va='center',
                  color='#FFE4E1', zorder=3, weight='normal',
                  family='sans-serif')

# Add decorative line
line_y = 22
ax.plot([25, 75], [line_y, line_y], color='white', linewidth=2, alpha=0.7, zorder=3)

# Add tech stack badges/icons
tech_stack = ['Python', 'Pandas', 'Matplotlib', 'Jupyter', 'Beauty Data']
tech_y = 16
spacing = 15
start_x = 10

for i, tech in enumerate(tech_stack):
    x_pos = start_x + (i * spacing)
    # Create rounded rectangle backgrounds for tech badges
    badge = FancyBboxPatch((x_pos - 1.5, tech_y - 1.5), 13, 3.5, 
                          boxstyle="round,pad=0.1", 
                          facecolor='white', edgecolor='none', 
                          alpha=0.25, zorder=2)
    ax.add_patch(badge)
    
    ax.text(x_pos + 5.5, tech_y, tech, 
           fontsize=11, ha='center', va='center',
           color='white', weight='bold', zorder=3,
           family='monospace')

# Add bottom tagline
tagline = ax.text(50, 6, 'Data Analytics | Insights | Visualization | Storytelling', 
                 fontsize=16, ha='center', va='center',
                 color='#FFE4E1', alpha=0.9, zorder=3,
                 family='sans-serif', style='italic')

# Add decorative data visualization elements (mini bar chart)
bar_x = [7, 9, 11, 13, 15]
bar_heights = [3, 5, 4, 6, 4.5]
bar_colors = ['#FF69B4', '#FFB6C1', '#DDA0DD', '#FF1493', '#FFC0CB']

for x, h, c in zip(bar_x, bar_heights, bar_colors):
    bar = FancyBboxPatch((x - 0.4, 2), 0.8, h, 
                         boxstyle="round,pad=0.05", 
                         facecolor=c, edgecolor='white', 
                         linewidth=1, alpha=0.6, zorder=2)
    ax.add_patch(bar)

# Add decorative data visualization elements (mini line chart on right)
line_x = np.array([88, 90, 92, 94, 96])
line_y_base = 3
line_y_vals = np.array([1, 2.5, 2, 4, 3.5]) + line_y_base

ax.plot(line_x, line_y_vals, color='white', linewidth=2.5, alpha=0.6, 
       marker='o', markersize=6, markerfacecolor='#FF69B4', 
       markeredgecolor='white', markeredgewidth=1.5, zorder=2)

# Save the banner
plt.tight_layout(pad=0)
plt.savefig('images/github_banner.png', dpi=80, bbox_inches='tight', 
           facecolor='none', edgecolor='none', transparent=False)
print("✅ GitHub banner created successfully: images/github_banner.png")
print("📐 Dimensions: 1280x640 pixels")
print("💡 Add this banner to your GitHub profile README!")

plt.close()
