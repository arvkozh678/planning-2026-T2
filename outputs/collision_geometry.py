from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

joints = np.array([[0., 0.], [1., 0.], [1., 1.]])
obs = np.array([1.3, .6])
radius = .35
fig, axes = plt.subplots(1, 2, figsize=(11, 5), constrained_layout=True)
for i, ax in enumerate(axes):
    a, b = joints[i:i+2]
    v = b-a
    raw = np.dot(obs-a, v)/np.dot(v, v)
    t = np.clip(raw, 0, 1)
    closest = a+t*v
    distance = np.linalg.norm(obs-closest)
    ax.plot(joints[:, 0], joints[:, 1], color='#a9b3bf', lw=5, zorder=2)
    ax.plot([a[0], b[0]], [a[1], b[1]], color='#2463ad', lw=6, zorder=3)
    ax.scatter(*joints.T, color='#344054', s=40, zorder=4)
    ax.add_patch(Circle(obs, radius, facecolor='#f0aa52', edgecolor='#ac6817', alpha=.3))
    ax.scatter(*obs, marker='x', color='#8c480b', s=65, zorder=5)
    ax.annotate('obs = (1.3, 0.6)', obs, xytext=(0, 30), textcoords='offset points', ha='center')
    ax.plot([obs[0], closest[0]], [obs[1], closest[1]], '--', color='#ac6817', lw=2)
    ax.scatter(*closest, color='#2463ad', s=85, zorder=6)
    ax.annotate(f'p3 = ({closest[0]:g}, {closest[1]:g})', closest,
                xytext=(-18, -30), textcoords='offset points', ha='right')
    ax.annotate('p1', a, xytext=(-16, 8), textcoords='offset points')
    ax.annotate('p2', b, xytext=(-22, 10), textcoords='offset points')
    if raw > 1:
        foot = a+raw*v
        ax.plot([b[0], foot[0]], [b[1], foot[1]], ':', color='#667085')
        ax.plot([obs[0], foot[0]], [obs[1], foot[1]], ':', color='#667085')
        ax.scatter(*foot, facecolors='none', edgecolors='#667085', s=55)
    ax.set_title(f'Link {i+1}: t = {raw:.1f}' + (' → clipped to 1' if raw > 1 else '') +
                 f'\nDistance = {distance:.3f}; ' + ('COLLISION' if distance <= radius else 'clear'), fontsize=12)
    ax.set(xlim=(-.2, 1.85), ylim=(-.3, 1.25), xlabel='x', ylabel='y', aspect='equal')
    ax.set_xticks([0, .5, 1, 1.5])
    ax.set_yticks([0, .5, 1])
    ax.grid(alpha=.18)
fig.suptitle('Same robot and circular obstacle (radius 0.35): check each link', fontsize=14)
fig.savefig(Path(__file__).with_suffix('.png'), dpi=170)
