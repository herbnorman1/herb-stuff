# Visc_T1.py
# Created by Herbert Norman Sr.  01/10/2017
# Given:  V(T) = Vo exp[k T]
#	 Temp_Low, Visc_Hi, Temp_Hi, Visc_Low, Temp_Exp
# Calculate: 
#          Viscosity Parameters Vo & K(T)
#	Viscosity Visc_Exp @ Temp_Exp
#=================================================================
import math

# INPUT Temp_Low & Visc_Hi
#=======================================================
Temp_Low_C = float(raw_input("Temp_Low: Degrees C = "))
Temp_Low_K = Temp_Low_C + 273.15 
Temp_Low_F = 9.0/5.0 * Temp_Low_C + 32
Visc_Hi = float(raw_input("Viscosity @ Temp_Low: Poise = "))

# INPUT Temp_Hi & Visc_Low
#=======================================================
Temp_Hi_C = float(raw_input("Temp_High: Degrees C = "))
Temp_Hi_K = Temp_Hi_C + 273.15 
Temp_Hi_F = 9.0/5.0 * Temp_Hi_C + 32
Visc_Low = float(raw_input("Viscosity @ Temp_High: Poise = "))

# Calculate Parameters: K(T) & Vo
#=============================================================
KT = (1/(Temp_Hi_K - Temp_Low_K)) * math.log(Visc_Low/Visc_Hi)
Vo = Visc_Hi * math.exp(-KT * Temp_Low_K)


print "K(T) = ", KT
print "Vo = ", Vo
print "=============================="

# INPUT Temp_Exp & Calculate Visc_Exp
#===============================================================
Temp_Exp_C = float(raw_input("Projected Temperature: Degrees C = "))
Temp_Exp_K = Temp_Exp_C + 273.15 
Temp_Exp_F = 9.0/5.0 * Temp_Exp_C + 32
Visc_Exp = Vo * math.exp(KT * Temp_Exp_K)

print "Temp_Exp_F = ", round(Temp_Exp_F)
print "Temp_Exp_K = ", round(Temp_Exp_K)
print "Visc_Exp = ", round(Visc_Exp,4), "Poise @ Deg C = ", Temp_Exp_C
