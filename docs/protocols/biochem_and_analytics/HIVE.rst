==========================
HIVE scRNA-seq
==========================
 
See https://honeycombbio.zendesk.com/hc/en-us

This protocol is from the HIVE protocols page: [HIVE_protocols]_. There are only some added annotated notes.


.. [HIVE_protocols]

    Protocol for single-cell ATAC sequencing using combinatorial indexing
    in mouse lung adenocarcinoma.
    STAR Protocols 2, 100583 (2021).

    https://doi.org/10.1016/j.xpro.2021.100583

.. important::
    The NaN3 is important to include in any single color controls! We observe that presence of EU doesn't change CFSE only control signal but any azide addition (with or without EU) significantly changes FSC/SSC and CFSE signal.
    The following image shows the effects of azide addition on 1 dpi CFSE-labeled MEFs flowed at 4 dpi.

    .. figure:: img/HIVE/Az_effect_on_CFSE.png
        :align: center

