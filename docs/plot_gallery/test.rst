Testing matplotlib directives
-----------------------------

.. plot::

    x = np.random.randn(1000)
    df = pd.DataFrame({'x':x})
    sns.histplot(data=df, x='x')
    sns.despine()
    plt.show()
