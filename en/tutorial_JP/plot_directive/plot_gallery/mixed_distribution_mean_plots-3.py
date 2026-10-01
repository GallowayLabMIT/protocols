# For violin plots, you must first log10 transform data
data_mGL['log({})'.format(y)] = np.log10(data_mGL[y])
well_mGL_gmean_df['log({})'.format(y+' (gmean)')] = np.log10(well_mGL_gmean_df[y+' (gmean)'])

# Plot
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
# Plot all points as violin
sns.violinplot(
    ax=ax, data=data_mGL,
    x=x, y='log({})'.format(y), order=order,
    palette=colormap, inner="quartile")
# Plot log10 transformed -> well geometric means of mGL-A as points
sns.stripplot(
    ax=ax, data=well_mGL_gmean_df,
    x=x, y='log({})'.format(y+' (gmean)'), order=order,
    dodge=True, color='white', size=5)

# Make log axis label:
ax.yaxis.set_major_formatter(
    mticker.StrMethodFormatter("$10^{{{x:.0f}}}$"))
ax.yaxis.set_ticks(
    [np.log10(x) for p in range(1, 7) for x in np.linspace(10**p, 10**(p+1), 10)],
    minor=True);

# Add in stats
annot = Annotator(ax=ax, data=well_mGL_gmean_df, x=x, y=y+' (gmean)', pairs=pairs, order=order)
annot.configure(test='t-test_ind', text_format='star', loc='inside', verbose=2)
annot.apply_test().annotate(line_offset_to_group=0.3) # Offset helps account for height of violin

# Adjust labels
plt.ylabel(y)
plt.title('4 dpi, HG')
fig.tight_layout()  # Helps improve white spacing
plt.show()