======================================================= 
SingleShot RNA isolation and Reverse Transcription
======================================================= 

This protocol for RNA isolation uses the `Bio-Rad SingleShot Cell Lysis Kit
<https://www.bio-rad.com/webroot/web/pdf/lsr/literature/10000112808.pdf>`__ and  
`Maxima H Minus Reverse Transcriptase <https://www.thermofisher.com/document-connect/document-connect.html?url=https://assets.thermofisher.com/TFS-Assets%2FLSG%2Fmanuals%2FMAN0012047_TS_Maxima_H_Minus_Reverse_Transcriptase_2000U_UG.pdf>`__. 


Materials need for RNA isolation
________________________________________________


==============================  ===================================================================================
**Solution**                     **Location**  
==============================  ===================================================================================
SingleShot Cell Lysis Buffer     All reagents located in kit in -20°C freezer (Sven) in original Bio-Rad packaging.            
Proteinase K solution            -20°C freezer (Sven)
DNase Solution                   -20°C freezer (Sven)
==============================  ===================================================================================

Materials needed for cDNA synthesis
_____________________________________________________


===========================================         ==========================  
**Solution**                                          **Location**  
===========================================         ==========================         
Oligo(dT) :subscript:`18`                             -20°C freezer (Anna)             
dNTP mix                                              -20°C freezer (Anna)
DEPC-treated Water                                    inside genomics hood
5x RT Buffer                                          -20°C freezer (Sven)
Maxima H Minus Reverse Transcriptase                  -20°C freezer (Sven)
Thermo Scientific RiboLock RNase Inhibitor            -20°C freezer (Sven)
===========================================         ========================== 

Other materials:
------------------

- RNase-free surface decontaminant
- Filter tips for pipettes
- PBS
- adherent cells in a 96-well plate
- PCR tubes
- Thermocycler


.. important:: 
    Since cells are being lysed, work does not need to be in the BSC. However, once the cells are lysed, extra precaution should be
    taken to prevent RNase contamination. 
    
    Dedicated RNAse-free tubes and tips should be used, and all pipettes and working surfaces should be wiped down 
    with the RNase-free surface decontaminant spray. Only use the genomics hood for these steps.
    
    Use the genomics hood. There are tubes on the shelf to the right of the genomics hood that are RNase-free.


RNA isolation using SingleShot Cell Lysis
__________________________________________
1. Thaw SingleShot Cell Lysis Buffer, Proteinase K, and DNase on ice.
2. Prepare Cell Lysis Master Mix on ice according to the number of wells to be isolated. It is recommended to make enough master mix for your number of wells plus 5%

==============================     ========================    ======================
**Component**                      **volume per well, µL**     **volume 96-well, µL**
==============================     ========================    ======================
SingleShot Cell Lysis Buffer        48                         4608
Proteinase K solution                1                          96
DNase solution                       1                          96
==============================     ========================    ======================

3. Aspirate media from cells, and wash with 125 µL of room temperature PBS.
4. Remove PBS
5. Add 50 µL of prepared SingleShot master mix to each well
6. Incubate without agitation at room temperature for 10 minutes. 


.. important:: 
    Do not incubate for longer than 20 minutes at room temperature 


.. important:: 
    Do not mix the cells with SingleShot master mix by pipetting

7. After 10 minutes, transfer the mastermix solution from the plate to a PCR tube. Multichannel pipettes work well here as PCR tubes have the same spacing as
   a 96-well plate.

8. Immediately transfer to thermocycler. Incubate at 37°C for 5 minutes followed by 75°C for 5 minutes for heat inactivation of cell lysis.


.. note:: 
    Cell lysate can be stored on ice up to 4 hours, at -20°C for 2 months, and -80°C for 12 months.


cDNA synthesis using Maxima H Minus Reverse Transcriptase
-----------------------------------------------------------

.. important:: 
    Continue to work with RNase-free equipment and in an RNase-free area.

9. Thaw on ice the Oligo(dT) :subscript:`18`, dNTP mix, 5x RT Buffer, Maxima H Minus Reverse Transcriptase (RT), and the RiboLock RNase Inhibitor.
10. Prepare **RT master mix 1**. Up to 9 µL of cell lysate from the SingleShot lysis kit can be used per reaction. AMB has used the maximum and obtained satisfactory results.

==============================     ==========================================================================
**Component**                      **volume per reaction, µL**     
==============================     ==========================================================================
Oligo(dT) :subscript:`18`            1                        
dNTP mix                             1                          
DEPC-treated water                   12.5 - (µL of lysate to be used, max of 9 µL lysate)                          
total                                at least 5.5 µL if maximum 9 µL of lysate and 1 µL of RT is to be used 
==============================     ==========================================================================

11. Determine how many reactions you are running. Normally, run one reaction per lysate. Additionally, pick lysates to
    perform no-reverse-transcriptase controls (e.g. one per condition) and add an extra reaction for those.

.. note::

    For example, if you have nine lysates across three conditions, you might want to setup 12 reactions; one for each
    of the nine lysates, and three additional reactions for a lysate from each of the conditions for no-RT.

12. Add :math:`X = 14.5 \mu\text{L} - (\text{$\mu$L of lysate})` of RT master mix 1 to a new PCR tube for each reaction.
13. Add up to 9 µL of a cell lysate to a PCR tube containing RT master mix 1. Mix gently.
14. Incubate lysate + master mix 1 at 65°C for 5 minutes, then cool on ice to melt secondary structures of RNA. 
15. Prepare RT master mix 2. 0.5-2 µL of RT may be used per reaction (50-200 Units). AMB has used 1 µL and obtained satisfactory results.
    If using different amount than 1 µL, you may need to adjust the water amount in step 10. 


===========================================   =======================================
**Component**                                  **volume per reaction, µL**     
===========================================   =======================================
5x RT Buffer                                     4
Maxima H Minus Reverse Transcriptase             1 - can be varieed between 0.5 and 2
Thermo Scientific RiboLock RNase Inhibitor       0.5                     
total                                            5.5 µL  
===========================================   =======================================

15. For each of the no-RT controls, prepare a control master mix that replaces the Reverse Transcriptase with Elga water.
16. Add 5.5 µL of RT master mix 2 to each PCR tube. Mix gently. If doing a no RT control, use the no-RT master mix.
17. Transfer to thermocycler, incubate at 50°C for 30 minutes, followed by 85°C for 5 minutes for heat inactivation.
18. Proceed to qPCR or freeze for future use.

.. note:: 
    cDNA can be stored at -20°C for 1 week and -80°C for longer. Avoid freeze/thaw cycles. 
