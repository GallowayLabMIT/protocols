mapping = {
   **{f"{x}5": "sciP2.{1-8}" for x in 'ABCDEFGH'},
   **{f"{x}6": "sciP2.{9-16}" for x in 'ABCDEFGH'},
   **{f"{x}7": "sciP2.{17-24}" for x in 'ABCDEFGH'},
}
mapping = {**mapping, **{(k[0] + '0' + k[1]): v for k,v in mapping.items() if len(k) == 2}}
fig = plt.figure()
rd.plot.plot_mapping(mapping, style='category', fig=fig)
ax = fig.get_axes()[0]
sns.move_legend(ax, 'lower center', bbox_to_anchor=(0.5,-0.42))
ax.set_title("sciP2 PCR primer plate", fontsize=15)
fig.clip_box = ax.get_tightbbox()