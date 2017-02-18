# Model_LA01.py
# Logistics Model (Series L)
# Created by Herb Norman Sr.  07/27/2016
#
#
#==================================================================================
# INPUT PARAMETERS
# Max Viscosity
import math
L_max = float(raw_input("Max Viscosity: L_max = "))/1000
L_min =  float(raw_input("Min Viscosity: L_min = "))/1000
Alpha = float(raw_input("Alpha % = "))/100
#L_hi = (1-Alpha/2)*L_max*1000
L_hi = (1-Alpha)*L_max*1000
kt_min = round(math.log(L_max/L_min - 1), 4)*(-1)
kt_hi = round(math.log(L_max/L_hi), 4)*(-1)
Delta_kt = kt_hi - kt_min
print "L_hi (@ Alpha) = ", round(L_hi, 2), "Poise"
#print "Alpha = ", round(Alpha,4)
print "kt_min =", kt_min," hrs", "             ", "kt_hi (@ Alpha) = ", kt_hi, " hrs", "                ", "Delta_kt = ", Delta_kt, " hrs"
print 
L_x = float(raw_input("Sample Slurry Viscosity (Poise) : L_x = "))/1000
t_x = float(raw_input("Process Time of Slurry Sample (hrs): t_x = "))
k = 1/t_x * math.log(L_max/L_x - 1)
t_min = round(kt_min/k, 4)
t_hi = round(kt_hi/k, 4)
Delta_t = round(Delta_kt/k, 4)
print "k = ", round(k,4)
print "t_min =", t_min," hrs", "             ", "t_hi (@ Alpha)= ", t_hi, " hrs", "                ", "Delta_t = ", Delta_t, " hrs"
print 
L_tx = round(L_max / (1 + math.exp(-k*(t_x -abs(t_min)))) * 1000, 2)
print "f(t) = L_Max / [1 + Exp(t - |t_min|)]                 Given Domain: 0 <= t <= Delta_t (hrs)"
print "f(", t_x,") = ",L_tx , " Poise"
t = 0
t_values = []
y_values = []
print "t       "," f(t): Viscosity "
print "=====", "=============="
for t in range(0, int(Delta_t+2)):
	Visc_t = round(L_max / (1 + math.exp(-k*(t -abs(t_min)))) * 1000, 2)
	print t, "        ", Visc_t
	t_values.append(t)
	y_values.append(Visc_t)

# GRAPHICS
#========================= 
import matplotlib.pylab as plt
from pylab import plot, show,title,xlabel,ylabel

title("Logistics Function:  Viscosity (Poise) vs Time (hrs)")
xlabel("Time (hrs)")
ylabel("Viscosity (Poise)")
x_numbers = t_values
y_numbers = y_values
plot(x_numbers,y_numbers, marker='*')
show()
