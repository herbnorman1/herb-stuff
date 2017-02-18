# Visc_X1.py
# Created by Herbert Norman Sr.  01/12/2017
# Given:  V(X) = Vo exp[k X]
#	 Visc_Solvent, Amt_Solvent, Visc_Solute, Amt_Solute
# Calculate: 
#          X = Amt_Solvent/(Amt_Solvent + Amt_Solute)
#          Vo = Visc_Solute
#          Viscosity Parameters Vo, k, X
#	Viscosity Visc_Exp @ X
#=================================================================
import math

# INPUT Amount & Viscosities of Solvents &Solutes
#=======================================================
Amt_Solvent = float(raw_input("Solvent: Parts = "))
Visc_Solvent = float(raw_input("Solvent: Viscosity (Low) = "))
Amt_Solute = float(raw_input("Solute: Parts = "))
Visc_Solute = float(raw_input("Solute: Viscosity (High) = "))
X = Amt_Solvent/(Amt_Solvent + Amt_Solute)

# Calculate Parameters: k & Vo
#=============================================================
Vo = Visc_Solute
k = math.log(Visc_Solvent/Visc_Solute)
Visc_X = Vo * math.exp(k * X)

print "k = ", k
print "Vo = ", Vo
print "V(X) = ", round(Visc_X, 4)
print "=============================="

# INPUT X_Exp & Calculate Visc_Exp
#===============================================================
X_Exp = float(raw_input("Projected X = "))
Visc_Exp = Vo * math.exp(k * X_Exp)
print "Visc_Exp = ", round(Visc_Exp,4), "Poise"
