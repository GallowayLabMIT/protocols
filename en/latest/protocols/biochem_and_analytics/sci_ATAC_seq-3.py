mapping = {
   "A3": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A4": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A5": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A6": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A7": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A8": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A9": "sciAD1.{3,4,5,6,7,9,10,11}",
   "A10": "sciAD1.{3,4,5,6,7,9,10,11}",
   "B1": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B2": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B3": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B4": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B5": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B6": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B7": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B8": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B9": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B10": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B11": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
   "B12": "sciAD2.{1,3,4,6,7,8,11,12,13,14,15,17}",
}
mapping = {**mapping, **{(k[0] + '0' + k[1]): v for k,v in mapping.items() if len(k) == 2}}
fig = plt.figure()
rd.plot.plot_mapping(mapping, style='category', fig=fig)
sns.move_legend(fig.get_axes()[0], 'lower center', bbox_to_anchor=(0.5,-0.31))
fig.tight_layout()
plt.title("Transposition primer plate", fontsize=15)