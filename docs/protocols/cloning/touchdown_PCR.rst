======================================
Touchdown PCR
======================================

This protocol describes one `method <https://www.nature.com/articles/nprot.2008.133>`_ to PCR a difficult product. The idea is to start at a high
annealing temperature (Ta) and "touchdown" so you start at the most specific product and amplify
at progressively less specific Ta's.

Touchdown PCR
---------------------------------

=============================== ===========================
Cycle #                          Ta
=============================== ===========================
1                                72°C
2                                71°C
3                                70°C
4                                69°C
...                              ...
n                                Predicted Ta
Repeat last cycle (30-n) times   Predicted Ta
=============================== ===========================

.. note:: 
    You could go even lower than the predicted Ta (we've gone down to 57°C as a robust protocol)

