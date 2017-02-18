#!/usr/bin/python
# Mixer Model 
# MODEL_A.py
# 
# Herbert Norman Sr. 09/12/2015
#=================================================================
import math
import pandas as pd

# INPUT INDEPENDENT VARIABLES AND CONSTANTS

B = 3000         # Bulk Capacity
E = 0.15         # Allowance
P = 1350.0       # Initial Pigment Charge
V = 1200.0       # Initial Vehicle Charge
np = 240000.0    # Relative Pigment Viscosity 
nv = 100.0       # Relative Vehicle Viscosity
r = 0.20         # Solids of Presscake

Tp = 2.50       # Process Time
Pct_wtr = 0.4    # Sampled % Moisture (1st Mixing Stage)
Mix_pct = 0.95   # Mix to % Completion
nw = 0.01        # Relative Water Viscosity
Wd1 = 1918
y = B*Pct_wtr/Wd1
K_Resid =round(math.log(y)/(-Tp**2),4)

# DEPENDENT VARIABLES

Kw = round(math.log(nw/np),4)         # Viscosity Constant (Water)
Xp = round(P/(P+V),4)                 # Pigment Content (Mix)
Xv = round(1 - Xp,4)                  # Vehicle Content (Mix)
Kv = round(math.log(nv/np),4)         # Viscosity Content (Mix)
n_mix = round(np*math.exp(Kv*Xv),1)   # Viscosity of Mix
N = round(((1-E)*Xp/r + Xv)/Xv,4)     # Exact Nbr of Mix Stages
n = int(N + 0.5)                      # Optimized Nbr of Mis Stages
kvn = round(math.log(nv/n_mix),4)     # Relative Viscosity Constant
i = 0                                 # Stage Counter (1 <= i <= n)
ni = []                               # Viscosity Distribution
xvi = []                              # % Vehicle Distribution
xpi = []                              # % Pigment Distribution
Pi = []                               # Vehicle Distribution
Vi = []                               # Pigment Distribution
Wdi = []                              # Water Displacement
stage = []                            # Stage Nbr
Cum_Pi = []                           # Cummulative Pigment Distribution
Cum_Vi = []                           # Cummulative Vehicle Distribution
Cum_Wdi = []                          # Cummulative Water Displacemrnt
VP_ratio = []                         # V to P Ratio
VPi = []                              # Charge (P + V) per stage
Cum_VPi = []                          # Cullulative Charge Sum(P + V) per stage
Wd_Resid = []                         # Residual (Water remaining after to Mix_pct)
Tai = []                              # Model A Time Est (hr/stage) to mix to Mix_pct
Tbi = []                              # Model B Time Est (hr/stage) to mix to Mix_pct
wi = []                               # Net Water Displaced per Stage (Wd - Residual)

# Dummy Variables Used to Build the LISTS in the DataFrames
sum_p = 0
Pi_x = 0
Vi_x = 0
Cum_Pix = 0
Cum_Vix = 0
Cum_Wdix = 0
VP_ratio_x =0.0
VPi_x = 0
Cum_VPi_x = 0
Wd_Resid_x = 0
Tai_x = 0
Tbi_x = 0
wi_x = 0

# Load the DataFrame Matrix

for i in range(1,n+1,1):
	stage.append(i)
	ni_x = n_mix*(1 - math.exp(kvn*i/n)) + nv
	ni_x = int(ni_x)
	ni.append(ni_x)
	xvi_x = round((math.log(ni_x/np))/Kv,4)
	xvi.append(xvi_x)
	xpi_x = round(1 - xvi_x,4)
	xpi.append(xpi_x)
	sum_p = sum_p + Pi_x
	Pi_x = round((B*xpi_x - sum_p)/(1/r + xvi_x*(1-1/r)),1)
	Pi.append(Pi_x)
	Cum_Pix = Cum_Pix + Pi_x
	Cum_Pi.append(Cum_Pix)
	Wdi_x = int(Pi_x/r*(1 - r))
	Wdi.append(Wdi_x)
	Vi_x = B - Cum_Pix - Cum_Vix - Wdi_x
	Vi.append(Vi_x)
	Cum_Vix = Cum_Vix + Vi_x
	Cum_Vi.append(Cum_Vix)
	VP_ratio_x = round(Cum_Vix/Cum_Pix,2)
	VP_ratio.append(VP_ratio_x)
	VPi_x = round(Pi_x + Vi_x,1)
	VPi.append(VPi_x)
	Cum_VPi_x = Cum_VPi_x + VPi_x
	Cum_VPi.append(Cum_VPi_x)
	wi_x = Wdi_x + Wd_Resid_x
	if i == 1:
		wi_x = wi_x * Mix_pct
	wi_x = round(wi_x,1)
	wi.append(wi_x)
	Wd_Resid_x = round(((1 - Mix_pct)*(Wdi_x + Wd_Resid_x)),2)
	Wd_Resid.append(Wd_Resid_x)
	Tai_x = round(math.sqrt(-1/K_Resid * math.log(1 - wi_x/Wd1)),2)
	Tai.append(Tai_x)
	Tbi_x = round(math.sqrt(-1/(K_Resid*i) * math.log(1 - Mix_pct)),2)
	Tbi.append(Tbi_x)

# Build Dictionaries {data1} & {data2}
# KEYS are the Headings for the Model Distributions ("1_Stage", "2_Pgmt", "3_Veh", ... ect)
# Refer to the column headings of the report
# The KEYS are pointing to the LISTS that are linked to column heading (stage, Pi, Vi, ... ect)   

	
data1 ={"1_Stage":stage , "9_Visc":ni , "4_Pgmt%":xpi , "5_Veh%":xvi , "2_Pgmt":Pi , "8_Wtr":Wdi , "3_Veh":Vi ,"6_Cum_P":Cum_Pi , "7_Cum_V":Cum_Vi}
frame1 = pd.DataFrame(data1)
frame1.to_csv("MDLA-Sum_01.csv")
print "Pgmt Charge......P =",P,"     ","Veh Charge........V =",V,"   ","Wtr Displaced....Wd =",P/r*(1-r)
print "Pgmt Viscosity..np =",np,"   ","Veh Viscosity....nv =",nv ,"    ","Wtr Viscosity....nw = ",nw
print "% Solids Pgmt....r =",r,"        ","Veh Visc Const...Kv =",Kv ,"  ","Wtr Visc Const...Kw =",Kw 
print "Mix Visc.....n_mix =", n_mix,"     ","Rel Visc Const..kvn =", kvn, "  ","Wtr Resid Const ..k =",K_Resid
print "Stage-Calc.......N = ", N,"     ","Stage-Optimized...n =",n
print "Optmzd Pgmt Charge =",sum(Pi),"     ","Optmzd Veh Charge ..=",sum(Vi),"   ","Optmzd Wtr Disp.....=",sum(wi)
print
print frame1

print
data2 ={"1_Stage":stage , "2_P+V":VPi , "3_Cum P+V":Cum_VPi , "4_V/P":VP_ratio , "5_Resid":Wd_Resid , "6_Ta-Est":Tai , "7_Tb-Est":Tbi , "8_Wtr Disp":wi}
frame2 = pd.DataFrame(data2)
frame2.to_csv("MDLA-Sum_02.csv")
print frame2
# 
# Print to OUTPUT FILE 
outfile = open("Model_A1.txt" , "w")
lines = ["MODEL A1" + "\n"]
outfile.writelines(lines)
lines = ["========================================================================================="+"\n"]
outfile.writelines(lines)
lines =[ "Pgmt Charge......P =" + str(P) + "     " + "Veh Charge........V =" + str(V) + "   " + "Wtr Displaced....Wd =" + str(P/r*(1-r)) +"\n"]
outfile.writelines(lines)
lines = ["Pgmt Viscosity..np = " + str(np) + "   " + "Veh Viscosity....nv = " + str(nv) +"    " + "Wtr Viscosity....nw = " + str(nw) + "\n"]
outfile.writelines(lines)
lines = ["% Solids Pgmt....r = " + str(r) + "        " + "Veh Visc Const...Kv = " + str(Kv) + "  " + "Wtr Visc Const...Kw = " + str(Kw) + "\n"]
outfile.writelines(lines)
lines = ["Mix Visc.....n_mix = " + str(n_mix) + "     " + "Rel Visc Const..kvn = " + str(kvn) + "  " + "Wtr Resid Const ..k = " + str(K_Resid) + "\n"]
outfile.writelines(lines)
lines = ["Stage-Calc.......N = " + str(N) + "     " + "Stage-Optimized...n = " + str(n) + "\n"]
outfile.writelines(lines)
lines = ["Optmzd Pgmt Charge = " + str(sum(Pi)) + "     " + "Optmzd Veh Charge ..= " + str(sum(Vi)) + "   " + "Optmzd Wtr Disp.....= " + str(sum(wi)) + "\n"]
outfile.writelines(lines)
lines = ["\n"]
outfile.close()

# GRAPHICS
#========================= 
import matplotlib.pylab as plt
from pylab import plot, show,title,xlabel,ylabel

title("Pigment & Vehicle Charge")
xlabel("Mix Stage")
ylabel("Pounds")
x_numbers = stage

y_numbers = Pi
plot(x_numbers,y_numbers, marker='*')

y_numbers = Vi
plot(x_numbers,y_numbers, marker='o')
show()

# ======================================================
# EXCEL WRITER
# =======================================================
import xlsxwriter

# Create a Pandas dataframe from some data.
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_chart.xlsx', engine='xlsxwriter') 
writer = pd.ExcelWriter('Data_02.xlsx', engine='xlsxwriter') 
# Convert the dataframe to an XlsxWriter Excel object.
df1.to_excel(writer, sheet_name='Data1')
df2.to_excel(writer, sheet_name='Data2')
# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Data1']
worksheet = writer.sheets['Data2']
writer.save()

#==============================================

