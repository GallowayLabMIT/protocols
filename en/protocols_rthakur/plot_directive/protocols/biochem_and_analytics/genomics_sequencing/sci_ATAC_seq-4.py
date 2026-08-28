mapping = {
   **{f"A{x}": "sciAD1.3" for x in range(1,13)},
   **{f"B{x}": "sciAD1.4" for x in range(1,13)},
   **{f"C{x}": "sciAD1.5" for x in range(1,13)},
   **{f"D{x}": "sciAD1.6" for x in range(1,13)},
   **{f"E{x}": "sciAD1.7" for x in range(1,13)},
   **{f"F{x}": "sciAD1.9" for x in range(1,13)},
   **{f"G{x}": "sciAD1.10" for x in range(1,13)},
   **{f"H{x}": "sciAD1.11" for x in range(1,13)},
}
mapping = {**mapping, **{(k[0] + '0' + k[1]): v for k,v in mapping.items() if len(k) == 2}}
fig = plt.figure()
rd.plot.plot_mapping(mapping, style='category', fig=fig)
plt.title("Transposition sciAD1 layout", fontsize=15)