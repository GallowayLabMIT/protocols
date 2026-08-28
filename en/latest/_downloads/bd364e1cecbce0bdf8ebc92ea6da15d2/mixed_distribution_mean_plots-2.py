# Categorize if mGL+
mGL_cat = list()
for mGL_val in data['mGL-H']:
    if mGL_val > mGL_H_thresh:
        mGL_cat.append('mGL+')
    else:
        mGL_cat.append('mGL-')
data['mGL_cat'] = mGL_cat

# Get total counts and percent of mGL+ and mGL-
well_group = ['cond', 'replicate', 'sampleNum'] # specifies we're splitting by cond >> bio rep >> tech rep >> etc...
count_df = data.groupby([*well_group, 'mGL_cat'])['mGL-H'   # Doesn't have to be mGL-H, any column would work
    ].count().unstack(fill_value=0).stack().rename('count') # unstack()/stack() puts 0 if no mGL-H+ rather than dropping row
percent_df = (count_df*100/count_df.groupby(well_group).transform('sum')
    ).reset_index(name='percent')

# Extract just the mGL+ cells
data_mGL = data.loc[data['mGL_cat'] == 'mGL+']
percent_df_mGL = percent_df.loc[(percent_df['mGL_cat'] == 'mGL+')]

# Calculate geom mean of mGL+ cells
well_mGL_gmean_df = data_mGL.groupby(well_group)[
    'mGL-H'].apply(scipy.stats.gmean).reset_index(name='mGL-H (gmean)')

# Plotting parameters
x = 'cond'
y = 'mGL-H'
order = ['mGL', 'mGL-WPRE']
pairs = [('mGL', 'mGL-WPRE')]
colormap = {'mGL': 'lightgrey',
            'mGL-WPRE': 'limegreen'}

# Plot
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
sns.boxplot(
    ax=ax, data=data_mGL,
    x=x, y=y, order=order,
    boxprops={'facecolor': 'None'}, showfliers=False) # Gets rid of boxplot colors and outliers
sns.stripplot(
    ax=ax, data=well_mGL_gmean_df,
    x=x, y=y+' (gmean)', order=order,
    dodge=True, palette=colormap, size=5)

# Add in stats
annot = Annotator(ax=ax, data=well_mGL_gmean_df, x=x, y=y+' (gmean)', pairs=pairs, order=order)
annot.configure(test='t-test_ind', text_format='star', loc='inside', verbose=2)
annot.apply_and_annotate()

# Adjust labels
plt.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
plt.ylabel(y)
plt.title('4 dpi, HG')
fig.tight_layout()  # Helps improve white spacing
plt.show()