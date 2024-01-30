# Read in data
data = pd.read_csv('data/data_mGL_WPRE/data_mGL_WPRE.csv')

# Plot mGL-H
x = 'mGL-H'
hue = 'cond'
cond_list = ['mGL', 'mGL-WPRE']
colormap = {'mGL': 'lightgrey',
            'mGL-WPRE': 'limegreen'}

# Plot
fig, ax = plt.subplots(1, 1, figsize=(6, 4))
sns.kdeplot(ax=ax, data=data, x=x, hue=hue, hue_order=cond_list,
            log_scale=(True, False), common_norm=False,
            shade=True, palette=colormap)

# Plot neg ctrl
sns.kdeplot(ax=ax, data=data.loc[data['cond'] == 'Neg'], x=x,
            log_scale=(True, False), common_norm=False,
            shade=False, color='black', alpha=0.5, linestyle='--')
ax.annotate('Neg', (0.08, 0.25),
            xycoords='axes fraction', alpha=0.5, ha='center')

# Add threshold for mGL+ gating
mGL_H_thresh = 2*10**2
ax.axvline(mGL_H_thresh, 0, 1, color='black')

# Title
plt.suptitle('4 dpi')
# Adjust limits
mGL_lim = (10, 10**6)
ax.set_xlim(mGL_lim)

# Misc plotting stuff
fig.tight_layout()  # Helps improve white spacing
plt.show()