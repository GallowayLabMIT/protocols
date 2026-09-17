mapping = {
   **{f"{x}1": "sciAD2.1" for x in "ABCDEFGH"},
   **{f"{x}2": "sciAD2.3" for x in "ABCDEFGH"},
   **{f"{x}3": "sciAD2.4" for x in "ABCDEFGH"},
   **{f"{x}4": "sciAD2.6" for x in "ABCDEFGH"},
   **{f"{x}5": "sciAD2.7" for x in "ABCDEFGH"},
   **{f"{x}6": "sciAD2.8" for x in "ABCDEFGH"},
   **{f"{x}7": "sciAD2.11" for x in "ABCDEFGH"},
   **{f"{x}8": "sciAD2.12" for x in "ABCDEFGH"},
   **{f"{x}9": "sciAD2.13" for x in "ABCDEFGH"},
   **{f"{x}10": "sciAD2.14" for x in "ABCDEFGH"},
   **{f"{x}11": "sciAD2.15" for x in "ABCDEFGH"},
   **{f"{x}12": "sciAD2.17" for x in "ABCDEFGH"},
}
mapping = {**mapping, **{(k[0] + '0' + k[1]): v for k,v in mapping.items() if len(k) == 2}}
fig = plt.figure()
rd.plot.plot_mapping(mapping, style='category', fig=fig)
plt.title("Transposition sciAD2 layout", fontsize=15)