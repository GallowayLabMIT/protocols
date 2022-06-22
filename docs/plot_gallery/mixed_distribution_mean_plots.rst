======================================
Mixed distribution + mean plots
======================================


Violin + mean plot
--------------------

.. plot::
    :context: reset

    import re

    # List of data folder names
    dir_list = ['2022.06.03_HG_mGL-WPRE_test_1',
                '2022.06.05_HG_mGL-WPRE_test_2']

    # Store all data in list of dfs which will be converted to df at end
    data = list()

    # get all csvs for each dir
    for (j, dir_name) in enumerate(dir_list):

        path = r'data/data_mGL_WPRE/{}/export_singlets/'.format(dir_name)
        files = Path(path).glob('*.csv')

        for i, file in enumerate(files):

            # Extract metadata from csv title
            match = re.search(
                'export_(?P<sampleName>.+)-(?P<sampleNum>\d{2})_(?P<subsetName>.+)_(?P<cond>.+).csv', file.name)
            # If csv is a ctrl file it won't match so ignore
            if match is None:
                continue

            cond = match.group('cond')
            sampleNum = match.group('sampleNum')

            # Rename ctrl
            if cond == 'ctrl-neg':
                cond = 'Neg'

            # Load as df and note header is on 0th row
            df = pd.read_csv(file, header=0)

            # Update columns in df with metadata from file name
            df['cond'] = cond
            df['replicate'] = j
            df['sampleNum'] = int(sampleNum)

            data.append(df)

    # Convert list of dfs into single df
    data = pd.concat(data, ignore_index=True)

    # Eliminate any negative fluor
    data = data[(data['mGL-A'] > 0) &
                (data['FSC-A'] > 0) & (data['SSC-A'] > 0)]

    # Threshold for mGL+ gating
    mGL_H_thresh = 2*10**2

    # Randomly sample only 10,000 samples from each condition to make representative flow diagram
    numSamples = 10**4
    small_data = data.groupby(['cond']).sample(n=numSamples, random_state=1)

.. plot::
    :context: close-figs

    # Plot mGL-H
    x = 'mGL-H'
    hue = 'cond'
    cond_list = ['mGL', 'mGL-WPRE']
    colormap = {'mGL': 'lightgrey',
                'mGL-WPRE': 'limegreen'}

    fig, ax = plt.subplots(1, 1, figsize=(6, 4))
    sns.kdeplot(data=small_data, x=x, hue=hue, hue_order=cond_list,
                ax=ax, log_scale=(True, False), shade=True, common_norm=False,
                palette=colormap)

    # Plot neg ctrl
    sns.kdeplot(data=small_data[small_data['cond'] == 'Neg'], x=x, common_norm=False,
            ax=ax, log_scale=(True, False), color='black', shade=False, alpha=0.5, linestyle='--')
    ax.annotate('Neg', (0.08, 0.25),
                    xycoords='axes fraction', alpha=0.5, ha='center')

    # Title
    plt.suptitle('4 dpi')
    # Adjust limits
    mGL_lim = (10, 10**6)
    for sub_ax in plt.gcf().get_axes():
        sub_ax.set_xlim(mGL_lim)
        sub_ax.axvline(mGL_H_thresh, 0, 1, color='black')

    # Misc plotting stuff
    fig.tight_layout()  # Helps improve white spacing
    plt.show()
    # plt.savefig('./figures/2022.06.03.mGL-WPRE_test/mGL_H_dist.pdf')
