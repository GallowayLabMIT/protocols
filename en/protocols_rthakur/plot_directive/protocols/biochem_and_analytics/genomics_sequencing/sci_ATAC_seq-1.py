mapping = {
   **{f"C{i}": "sciP1.{1-12}" for i in range(1,13)},
   **{f"D{i}": "sciP1.{13-24}" for i in range(1,13)},
   **{f"E{i}": "sciP1.{25-36}" for i in range(1,13)},
}
mapping = {**mapping, **{(k[0] + '0' + k[1]): v for k,v in mapping.items() if len(k) == 2}}
fig = plt.figure()
rd.plot.plot_mapping(mapping, style='category', fig=fig)
ax = fig.get_axes()[0]
sns.move_legend(ax, 'lower center', bbox_to_anchor=(0.5,-0.42))
ax.set_title("sciP1 PCR primer plate", fontsize=15)
fig.clip_box = ax.get_tightbbox()