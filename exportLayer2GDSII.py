################################################################################
# Name: exportLayer2GDSII.py                                                   #
# Purpose: export user-chosen layers to GDSII in L-Edit                        #
#                                                                              #
# Release: 17/March/2023                                                       #
# Author: Khalid Teama @ EDA Solutions Ltd.                                    #
# Contact: Support@eda-solutions.com                                           #
#                                                                              #
# Please use this script at your own discretion and responsbility. Eventhough  #
# This script was tested and passed the QA criteria to meet the intended       #
# specifications and behaviors upon request, the user remains the primary      #
# responsible for the sanity of the results produced by the script.            #
# The user is always advised to check the imported design and make sure the    #
# correct data is present.                                                     #
#                                                                              #
# For further support or questions, please e-mail support@eda-solutions.com    #
#                                                                              #
# Test platform version: L-Edit 2022.2 Update 3 Release build 20925            #
################################################################################
# --------------------------
# Installation:- 
# --------------------------
# Open "exportLayer2GDSII.py.tcl" in a text editor e.g. notepad
# Set the path for this Python script here: (Example: set pyScriptLoc {F:\exportLayer2GDSII.py})
# Execute the script ("exportLayer2GDSII.py.tcl") in L-Edit
# Note: the TCL file must be loaded with every new session, to avoid doing
# so manually, please refer to L-Edit's documentation to decided the
# most suitable way to load the script automatically as there are plenty  
# --------------------------
# Usage:-
# --------------------------
# 1. Have a design and a cell open
# 2. Once the path to the script is set and the TCL is loaded, use the button "Export_layer_2_GDSII" in your toolbar
# --------------------------
# Notes:
# --------------------------
# N/A
################################################################################
#########################################################################
#                                                                       #
#   History:                                                            #
#   Version 0.0 |- Created  script                                      #
#           1.0 | 16/03/2023 - First version of the script              #
#########################################################################
#++++++++++++++++ END OF Comments ++++++++++++++++++++

#++++++++++++++++ Script start ++++++++++++++++++++
import os 

#Function to export GDSII
def exportGDSII(gdsName):
    try: 
        pwdPath = os.getcwd()
        cellName = LCell_GetName(None)
        destFileName = cellName + "_" + str(gdsName) + ".gds"
        destFileName = destFileName.replace(":","_")
        print("Export layer to GDSII: Written: " + pwdPath + "\\" + destFileName)
        pPar = LGDSParamEx()
        pPar.cszDestFileName = destFileName
        pPar.bOverwriteGDSII = LTRUE 
        pPar.bIncludeHierarchy = LTRUE
        pPar.bDoNotExportHiddenObjects = LTRUE
        pPar.ExportScope = gdsExportActiveCell
        pLog = LGDSExportLogParams()
        pLog.bOpenLogInWindow = LFALSE
        pLog.szLogFileName = destFileName + ".log"
        LFile_ExportGDSII(pPar, pLog)
        del pPar
        del destFileName
        del pLog
        return 1
    except Exception as err: 
        print("Export layer to GDSII: An error occurred at GDSII export function:")
        print(err)
        return 5

#Function to hide all layers with the exception of a user input. It will also show all layers if asked 
def hideAllLayersExceptOrShowAll(expLayerNamesStr,hideShow):
    try:
        #Get all layer object handlers and parameters 
        loclayersInFile = LLayer_GetList()
        loclayerParams = [LLayer_GetParametersEx1512(layerObj) for layerObj in loclayersInFile]

        #Get exception layer handlers and parameters 
        expLayerObj = LLayer_Find(expLayerNamesStr) 
        expLayerParams = LLayer_GetParametersEx1512(expLayerObj) 

        #Iterate through all layers and hide or show based on hideShow input
        #If layer is in the exception list, it won't be hidden 
        for idx, m in enumerate(loclayersInFile):
            newParam=loclayerParams[idx]
            newParam.Hidden=LTRUE if hideShow == 0 and m != expLayerObj else LFALSE 
            LLayer_SetParametersEx1512(m,newParam)

        #Clear all variables to avoid contamination with future runs 
        del newParam
        del loclayersInFile
        del loclayerParams
        del expLayerObj
        del expLayerParams
        del m 
        del idx 
        return 1
    except Exception as err: 
            print("Export layer to GDSII: An error occurred at show/hide layers function with layer " + expLayerNamesStr + " :")
            print(err)
            return 5 

#Function to query user for layers to export 
def usrInput():
    all_layersInFile = LLayer_GetList()
    all_layerNames = [LLayer_GetName(layerObj) for layerObj in all_layersInFile]
    selection = LDialog_PickList("Select layer to export", 1, all_layerNames)
    selectedLayerName = all_layerNames[selection]
    if (selection >= 0): 
        del all_layersInFile
        del all_layerNames
        del selection
        return selectedLayerName 
    else:
        return -1 

#Main function
def main(usrInp):
    try: 
        #Get layer's original parameters
        origlayersInFile = LLayer_GetList()
        origlayerParams = [LLayer_GetParametersEx1512(layerObj) for layerObj in origlayersInFile]

        #For each requested layer, hide all except the layer and export GDSII
        if hideAllLayersExceptOrShowAll(usrInp,0) != 5: 
            if exportGDSII(usrInp) == 5: return 5  
        else:
            return 5
        
        #Return all layer parameters to their original state 
        for idx,j in enumerate(origlayersInFile):
            LLayer_SetParametersEx1512(j,origlayerParams[idx]) 

        #Refresh the display
        LDisplay_Refresh

        #Finish with success 
        del origlayersInFile
        del origlayerParams 
        return 1

    except Exception as err: 
        print("Export layer to GDSII: An error occurred at main function:")
        print(err)
        #Finish with failure
        return 5 

#Script top level
usrInp = 1
#Infinite loop until user cancels
while (usrInp != -1): 
    usrInp = usrInput()
    if usrInp != -1:
        if main(usrInp) == 1: print("Export layer to GDSII: Completed successfully.\n")
        else: print("Export layer to GDSII: Failed to complete export operation, make sure \nfile and cell are open or check your inputs.\n")
    else: 
        print("Export layer to GDSII: Exit by user.\n")
