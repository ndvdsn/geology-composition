import keyboard
from decimal import *

lengths = [
1.2, 0.3, 0.9, 0.1, 1.1, 0.2, 0.2, 0.1, 3.5, 0.7, 0.9, 0.4, 0.6, 1.7, 0.2, 0.5,
0.2, 2.5, 0.5, 0.2, 2.5, 0.5, 0.2, 0.8, 1.0, 0.3, 0.9, 0.3, 1.0, 0.7, 0.2, 1.3,
0.5, 0.3, 0.3, 0.2, 0.2, 0.1, 0.5, 0.1, 1.7, 0.1, 0.6, 0.1, 0.1, 0.1, 0.1, 0.5,
0.4, 0.1, 0.1, 0.2, 0.1, 2.3]
labels = ["Older raised beach", "Alluvium", "TACET", "TCA  - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
                  "TCA  - coarse ... very coarse ... pebbly ... often contorted", 
                  "TACET", "TCA  - coarse ... very coarse ... pebbly ... often contorted", "TACET",
"River Terrace Deposits", "TACET", "River Terrace Deposits", "F", "TACET", "F", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "F", "Amphibolite - metamorphosed mafic volcanic", 
"Om", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "Amphibolite - metamorphosed mafic volcanic",
"Semipilite Schistose", "Om", "Semipilite", "Amphibolite - metamorphosed mafic volcanic", "Semipilite", "Water", 
"Amphibolite - metamorphosed mafic volcanic", "Alluvium", "Water",
"Alluvium", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "TACET", "F",
"Alluvium", "TACET", "Water"]

lengths2 = [0.2, 0.1, 1.0, 1.2, 0.2, 0.4, 1.1, 0.1, 5.0, 0.1, 0.2, 0.1, 0.6, 0.05,
0.1, 0.05, 4.1, 0.1, 0.2, 0.6, 0.1, 0.2, 1.0, 0.2, 0.6, 0.3, 1.6, 0.6, 0.9, 0.1,
0.05, 0.1, 0.6, 0.1, 0.2, 0.1, 0.15, 0.1, 0.05, 0.05, 0.05, 0.03, 0.1, 0.05, 0.3,
0.3, 0.5, 0.1, 1.1, 0.9, 1.0, 0.2, 1.6, 0.1, 1.1, 0.3, 1.6, 0.1, 0.4, 0.1, 0.2,
1.2, 0.1, 0.4, 3.0, 0.2, 0.1, 1.0]

lengths2labels = ["TCA  - coarse ... very coarse ... pebbly ... often contorted - Old raised beach","Basaltic dyke", 
                  "TCA  - coarse ... very coarse ... pebbly ... often contorted", 
                  "TCA  - coarse ... very coarse ... pebbly ... often contorted- Old raised beach",
"Blown sand", "TCA  - coarse ... very coarse ... pebbly ... often contorted - old raised beach", 
"TCA  - coarse ... very coarse ... pebbly ... often contorted - inclined strata, dip in degrees", "TACET", 
"TCA  - coarse ... very coarse ... pebbly ... often contorted", "TACET",
"TCA  - coarse ... very coarse ... pebbly ... often contorted", "Basaltic dyke", 
"TCA  - coarse ... very coarse ... pebbly ... often contorted", "L - Metalimestone (marble)", 
"TCA  - coarse ... very coarse ... pebbly ... often contorted", "L - Metalimestone (marble)", "TCA  - coarse ... very coarse ... pebbly ... often contorted", 
"TACET", "River terrace deposits", "TACET", "DD - Amphibolite metamorphosed mafic dykes",
"TACET", "F", "TACET", "F", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "F", "TACET", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "Alluvium", "Om", "Alluvium", "Om", "Amphibolite - metamorphosed mafic volcanic", 
"Om", "S",
"Amphibolite - metamorphosed mafic volcanic", "S", "Amphibolite - metamorphosed mafic volcanic", "S", 
"Amphibolite - metamorphosed mafic volcanic", "S", "Amphibolite - metamorphosed mafic volcanic", "Q", 
"Amphibolite - metamorphosed mafic volcanic", "S", "Amphibolite - metamorphosed mafic volcanic", "K1 - Heterogenous unit of chlorite schist",
"S", "Amphibolite - metamorphosed mafic volcanic", "F - with dykes", "Amphibolite - metamorphosed mafic volcanic", 
"F", "DD - Amphibolite metamorphosed mafic dykes", "F", "Water", "F - with dykes", "ß", "F - w dykes", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles",
"TACET", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles" , "TACET", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles -raised beach", "water", "F", "TACET", "Amphibolite - metamorphosed mafic volcanic"]

lengths3 = [0.15, 0.1, 1.2, 0.1, 3.5, 0.1, 1.2, 0.05, 3.3, 0.3, 0.6, 0.1, 0.05, 0.1, 0.1, 0.3, 0.1, 0.1,
0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.2, 0.1, 0.05, 0.1, 0.05, 0.1, 0.1, 3.1, 0.1, 0.05, 0.5,
0.2, 0.6, 0.25, 1.0, 1.1, 0.25, 0.1, 0.05, 0.05, 0.05, 0.05, 0.4, 0.1, 0.75, 0.3, 0.3, 0.35, 1.6, 0.4, 0.05,
0.2, 0.1, 0.2, 0.05, 0.1, 0.7, 0.05, 0.1, 0.2, 1.0, 0.05, 0.6, 0.1, 0.3, 0.05, 0.2, 0.1, 0.05, 0.75, 0.4,
0.05, 0.7, 0.05, 0.8, 0.15, 1.0, 0.1, 0.07, 0.6, 0.05, 0.5, 0.3, 0.1, 0.1, 0.07, 0.07, 0.1, 0.07, 0.1, 0.1,
0.1, 3.2, 1.6, 10.3, 0.025, 0.2, 0.3, 0.1, 0.2, 0.6, 5.5, 0.15, 0.6, 0.1, 0.6, 0.1, 0.8, 0.2, 0.1, 0.1, 0.3,
0.25, 5.2]

lengths3labels = ["TCA  - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
                  "TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
                  "TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
                  "TCA - coarse ... very coarse ... pebbly ... often contorted", "L - Metalimestone (marble)", 
                  "TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
                  "TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", "Alluvium",
"TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "F", "TACET", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F", "TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", 
"TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "F - W DYKES", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "River Terrace", "Water", "TCD3", "Water", "μ", "H", "water", "Om",
"Amphibolite - metamorphosed mafic volcanic", "Om", "Amphibolite - metamorphosed mafic volcanic", "Om", 
"Amphibolite - metamorphosed mafic volcanic", "S", "Amphibolite - metamorphosed mafic volcanic", "S", 
"Amphibolite - metamorphosed mafic volcanic", "Raised beach", "Older raised beach", "Amphibolite - metamorphosed mafic volcanic", 
"S", "water",
"S", "TACET", "S", "Amphibolite - metamorphosed mafic volcanic", "TACET", "Amphibolite - metamorphosed mafic volcanic", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles",
 "Amphibolite - metamorphosed mafic volcanic", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F",
"DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "F", "TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F", "TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F",
"DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "F", "water", "TCA", "water", "NRS", "TACET", "raised beach", "Older raised beach", "TACET",
"NRS", "TCAU medium grained ... contorted", "TACET", "TCAU medium grained ... contorted", "TACET", "TCAU medium grained ... contorted", 
"TACET", "TCAU medium grained ... contorted", "TACET", "NRS", "TACET", "Older raised beach", "NRS",
"water"]

lengths4 = [0.7, 0.2, 0.2, 0.4, 0.2, 1.7, 3.1, 0.4, 1.6, 0.1, 4.7, 0.3, 0.05, 0.1, 0.1, 0.1, 0.2, 0.25,
0.5, 0.6, 0.2, 0.1, 0.1, 0.6, 0.4, 0.1, 0.1, 0.1, 0.05, 0.1, 0.07, 0.1, 0.15, 0.1, 0.1, 0.1, 0.05, 0.1,
0.05, 0.1, 0.2, 0.1, 0.25, 0.1, 0.05, 0.1, 0.3, 0.1, 0.1, 0.1, 1.15, 0.8, 1.9, 0.4, 0.1, 0.1, 0.05, 0.05,
0.1, 0.1, 0.4, 0.3, 0.1, 0.075, 0.1, 0.2, 0.3, 0.3, 0.2, 0.4, 0.1, 0.7, 0.1, 0.1, 0.7, 0.7, 1.2, 0.5, 0.2,
0.1, 0.1, 0.12, 0.1, 0.5,0.3, 0.1, 0.15, 0.1, 0.7]

lengths4labels = ["TCA - coarse ... very coarse ... pebbly ... often contorted", "TCD3", "Older raised beach", "TCD3", "TACET", "TCD3", 
                  "Water -sea", "Blown sand",
"TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", "TCA - coarse ... very coarse ... pebbly ... often contorted", 
"TACET", "TCD3", "TACET", "Alluvium", "TACET", "TCD3", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "TACET", "TCD3", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "F", "TACET",
"TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F",
"DD - Amphibolite metamorphosed mafic dykes", "F","DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "DD - Amphibolite metamorphosed mafic dykes", "F", "Water - fresh", "F", "TACET", "F", "TACET", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F",
"TACET", "Glaciofluvial", "TACET" "F", "TACET", "Glaciofluvial", "F", "TACET", "F", "Raised beach poolewe",
"Water - Ewe", "Raised beach", "TACET", "Older raised beach", "TAS", "Older raised beach", "TAT", "TACET",
"F", "DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "Alluvium", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "TACET", "F"]

lengths5 = []

lengths5labels = []

lengths6 = []

lengths6labels = []

lengths7 = [0.1, 0.3, 0.6, 1.9, 0.1, 0.15, 0.6, 0.1, 0.1, 1.5, 0.1, 0.1, 0.1, 1.75, 0.1, 0.7, 0.1, 0.3,
0.1, 0.15, 0.1, 0.2, 0.5, 0.6, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1, 0.7, 0.2, 0.1, 0.2, 0.2,]

lengths7labels = ["TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", "Blown sand", "Older raised beach", 
                  "TACET", "Peat", "TCA - coarse ... very coarse ... pebbly ... often contorted", "Peat", "TACET", 
"TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", "TCA - coarse ... very coarse ... pebbly ... often contorted", 
"TACET", "TCA - coarse ... very coarse ... pebbly ... often contorted", "TACET", 
"TCA - coarse ... very coarse ... pebbly ... often contorted", "TCD3", "TACET", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes",
"F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "F", "DD - Amphibolite metamorphosed mafic dykes", "TACET", "F", "TCD1 Gneiss breccia-conglomerate ... containing gneiss pebbles", ]

# lengths = []
array_length = 0


duration = int(input("Enter duration of piece in minutes:"))
total_seconds = duration * 60
seconds_to_percentages = total_seconds / 100

# array_length = int(input("Enter number of values:"))
# print(str(array_length) + " values to enter")


# for x in range(array_length):
#     length = float(input("Enter a length:"))
#     lengths.append(length)


sum = 0
for i in lengths:
    sum = sum + i

percentages = []
# length_to_percentage = sum / 100
#
# print(length_to_percentage)

for i in lengths:
    new_percentage = (i / sum) * 100
    percentages.append(new_percentage)

durations = []

for i in percentages:
    new_duration = seconds_to_percentages * i
    durations.append(new_duration)

for i in durations:
    print(int(i//60),":",int(i%60))

print("-----------")
# Next create the time marker points as accumulative rather than a serie of discrete durations.

def checkDecimals(n):
    if n < 10:
        return ("0"+ str(n))
    else:
        return n
acc_durations = []
c = 0
for i in durations:
    print(int(c//60),":",checkDecimals(int(c%60)))
    acc_durations.append(str(int(c//60)) +":"+ str(checkDecimals(int(c%60))))
    print('-')
    c +=i
    print(int(c//60),":",checkDecimals(int(c%60)))
    # acc_durations.append(str(int(c//60)) +":"+ str(checkDecimals(int(c%60))))
    print('')

def iszerominutes(minutes):
    if minutes == "0":
        return ""
    else:
        return minutes + " m"

for x in range(len(acc_durations)):
    # print(acc_durations[i] + "-" + acc_durations[i + 1])
    print(acc_durations[x] + " - " + acc_durations[x + 1] + "  " + "   (" + iszerominutes(str(int(durations[x]//60))) , str(int(durations[x]%60)) + "s)    " + labels[x])
    print("")
# print(checkDecimals(int(durations[0] //60)))
# print(checkDecimals(int(durations[0] %60)))


# print(sum)
# print(percentages)
# print(total_seconds)

# print(103 // 60, ":", 103 % 60)



# listen_for_stop()


# print(lengths)
