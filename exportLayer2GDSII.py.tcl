################################################################################
# Name: exportLayer2GDSII.py.tcl                                               #
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
# Set the path for the Python script here: (Example: set pyScriptLoc {F:\exportLayer2GDSII.py})
# 
  	
set pyScriptLoc {<PATH HERE>}

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

#Create the button
workspace userbutton set "Export_layer_2_GDSII"

#Procedure to execute python script
proc Export_layer_2_GDSII {} {
    pyscript -name $::pyScriptLoc
}