import keyboard
from decimal import *

lengths = [
1.2, 0.3, 0.9, 0.1, 1.1, 0.2, 0.2, 0.1, 3.5, 0.7, 0.9, 0.4, 0.6, 1.7, 0.2, 0.5,
0.2, 2.5, 0.5, 0.2, 2.5, 0.5, 0.2, 0.8, 1.0, 0.3, 0.9, 0.3, 1.0, 0.7, 0.2, 1.3,
0.5, 0.3, 0.3, 0.2, 0.2, 0.1, 0.5, 0.1, 1.7, 0.1, 0.6, 0.1, 0.1, 0.1, 0.1, 0.5,
0.4, 0.1, 0.1, 0.2, 0.1, 2.3]
lengths1labels = ["Old raised beach", "Alluvium", "UD", "TCA", "UD", "TCA", "UD", "TCA", "UD", "River Terrace Deposits",
"UD", "River T.D.", "F", "UD", "F", "TCD1", "F", "BD", "Om", "TCD1", "BD", "Semipilite Schistose", "Om", "Semipilite",
"BD", "Semipilite", "Water", "BD", "Alluvium", "Water", "Alluvium", "DD", "F", "DD", "F", "DD", "F", "DD", "F","DD",
"F", "DD", "UD", "F", "TCD1", "UD", "F", "Alluvium", "UD", "Water"]

lengths2 = [0.2, 0.1, 1.0, 1.2, 0.2, 0.4, 1.1, 0.1, 5.0, 0.1, 0.2, 0.1, 0.6, 0.05,
0.1, 0.05, 4.1, 0.1, 0.2, 0.6, 0.1, 0.2, 1.0, 0.2, 0.6, 0.3, 1.6, 0.6, 0.9, 0.1,
0.05, 0.1, 0.6, 0.1, 0.2, 0.1, 0.15, 0.1, 0.05, 0.05, 0.05, 0.03, 0.1, 0.05, 0.3,
0.3, 0.5, 0.1, 1.1, 0.9, 1.0, 0.2, 1.6, 0.1, 1.1, 0.3, 1.6, 0.1, 0.4, 0.1, 0.2,
1.2, 0.1, 0.4, 3.0, 0.2, 0.1, 1.0]

lengths2labels = ["TCA - Old raised beach","B - Basaltic dyke", "TCA", "TCA - Old raised beach",
"Blown sand", "TCA - old raised beach", "TCA - inclined strata, dip in degrees", "UD", "TCA", "UD",
"TCA", "B", "TCA", "L - Metalimestone", "TCA", "L", "TCA", "UD", "River terrace deposits", "UD", "DD",
"UD", "F", "UD", "F", "TCD1", "F", "UD", "TCD1", "Alluvium", "Om", "Alluvium", "Om", "BD", "Om", "S",
"BD", "S", "BD", "S", "BD", "S", "BD", "Q", "BD", "S", "BD", "K1 - Heterogenous unit of chlorite schist",
"S", "BD", "F - with dykes", "BD", "F", "DD", "F", "Water", "F - with dykes", "ß", "F - w dykes", "TCD1",
"UD", "TCD1" , "UD", "TCD1 -raised beach", "water", "F", "UD", "BD"]

lengths3 = [0.15, 0.1, 1.2, 0.1, 3.5, 0.1, 1.2, 0.05, 3.3, 0.3, 0.6, 0.1, 0.05,
0.1, 0.1, 0.3, 0.1, 0.1, 0.1, 0.2, 0.1, 0.1, 0.1, 0.1, 0.5, 0.1, 0.1, 0.2, 0.1,
0.05, 0.1, 0.05, 0.1, 0.1, 3.1, 0.1, 0.05, 0.5, 0.2, 0.6, 0.25, 1.0, 1.1, 0.25, 0.1, 0.05, 0.05, 0.05, 0.05, 0.4, 0.1, 0.75, 0.3, 0.3, 0.35, 1.6, 0.4, 0.05, 0.2, 0.1, 0.2,
0.05, 0.1, 0.7, 0.05, 0.1, 0.2, 1.0, 0.05, 0.6, 0.1, 0.3, 0.05, 0.2, 0.1, 0.05, 0.75, 0.4, 0.05, 0.7, 0.05, 0.8, 0.15, 1.0, 0.1,
0.07, 0.6, 0.05, 0.5, 0.3, 0.1, 0.1, 0.07, 0.07, 0.1, 0.07, 0.1, 0.1, 0.1, 3.2, 1.6, 10.3, 0.025, 0.2, 0.3, 0.1, 0.2, 0.6, 5.5,
0.15, 0.6, 0.1, 0.6, 0.1, 0.8, 0.2, 0.1, 0.1, 0.3, 0.25, 5.2]

lengths3labels = ["TCA", "UD", "TCA", "UD", "TCA", "UD", "TCA", "L", "TCA", "UD", "TCA", "UD", "Alluvium", "UD", "DD", "F", "DD", "UD",
"F", "DD", "F", "UD", "F", "UD", "F", "DD", "UD", "F", "UD", "DD", "F", "UD", "DD", "F", "UD", "F - W DYKES",
"TCD1", "River Terrace", "Water", "TCD3", "Water", "μ", "H", "water", "Om", "BD", "Om", "BD", "Om", "BD", "S", "BD", "S", "BD", "Raised beach",
"Older raised beach", "BD", "S", "water", "S", "UD", "S",
"BD", "UD", "BD", "TCD1", "BD", "TCD1", "F", "DD", "F", "DD", "F", "DD", "F", "DD", "F", "DD", "F", "DD", "F",
"DD", "F", "UD", "F", "UD", "DD", "F", "DD", "UD", "F", "UD", "DD", "F", "DD", "F", "DD", "F", "UD", "F",
"water", "TCA", "water", "NRS", "UD", "raised beach", "Older raised beach", "UD", "NRS", "TCAU", 
"UD", "TCAU", "UD", "TCAU", "UD", "TCAU", "UD", "NRS", "UD", "Older raised beach", "NRS", "water"]

lengths4 = [0.7, 0.2, 0.2, 0.4, 0.2, 1.7, 3.1, 0.4, 1.6, 0.1, 4.7, 0.3, 0.05, 0.1, 0.1, 0.1, 0.2, 0.25, 0.5, 0.6, 0.2, 0.1, 0.1, 0.6, 0.4, 0.1, 0.1, 0.1, 0.05, 0.1, 0.07, 0.1, 0.15, 0.1,
0.1, 0.1, 0.05, 0.1, 0.05, 0.1, 0.2, 0.1, 0.25, 0.1, 0.05, 0.1, 0.3, 0.1, 0.1, 0.1, 1.15, 0.8, 1.9, 0.4, 0.1, 0.1, 0.05, 0.05, 0.1, 0.1, 0.4, 0.3, 0.1,
0.075, 0.1, 0.2, 0.3, 0.3, 0.2, 0.4, 0.1, 0.7, 0.1, 0.1, 0.7, 0.7, 1.2, 0.5, 0.2, 0.1, 0.1, 0.12, 0.1, 0.5, 0.3, 0.1, 0.15, 0.1, 0.7]

lengths4labels = ["TCA", "TCD3", "Older raised beach", "TCD3", "UD", "TCD3", "Water -sea", "Blown sand", "TCA", "UD", "TCA", "UD", "TCD3", "UD", "Alluvium", "UD", "TCD3", "TCD1", "UD", "TCD3", "TCD1", "F", "UD", "TCD1", "F", "DD", "F", "DD", "F","DD", "F","DD", "F","DD",
"F","DD", "F","DD", "F","DD", "F","DD", "F","DD", "F","DD", "F", "DD", "UD", "DD", "F", "Water - fresh", "F", "UD", "F", "UD", "F", "DD", "UD", "F", "UD", "Glaciofluvial", "UD"
"F", "UD", "Glaciofluvial", "F", "UD", "F", "Raised beach poolewe", "Water - Ewe", "Raised beach", "UD", "Older raised beach", "TAS", "Older raised beach", "TAT", "UD", "F", "DD", "F", "UD", "Alluvium", "DD", "F", "DD", "F", "UD", "F"]

lengths5 = []

lengths5labels = []

lengths6 = []

lengths6labels = []

lengths7 = [0.1, 0.3, 0.6, 1.9, 0.1, 0.15, 0.6, 0.1, 0.1, 1.5, 0.1, 0.1, 0.1, 1.75, 0.1, 0.7, 0.1, 0.3, 0.1, 0.15, 0.1, 0.2, 0.5, 0.6, 0.1, 0.1, 0.05, 0.05,
0.05, 0.05, 0.05, 0.1, 0.7, 0.2, 0.1, 0.2, 0.2,]

lengths7labels = ["TCA", "UD", "Blown sand", "Older raised beach", "UD", "Peat", "TCA", "Peat", "UD", "TCA", "UD", "TCA", "UD", "TCA", "UD", "TCA", "TCD3", "UD", "F", "DD", "F", "DD", "F", "DD", "F", "DD", "F", "DD",
"F", "DD", "F", "DD", "F", "DD", "UD", "F", "TCD1", ]

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
    print(acc_durations[x] + " - " + acc_durations[x + 1] + "  " + "   (" + iszerominutes(str(int(durations[x]//60))) , str(int(durations[x]%60)) + "s)    " + lengths1labels[x])
    print("")
# print(checkDecimals(int(durations[0] //60)))
# print(checkDecimals(int(durations[0] %60)))


# print(sum)
# print(percentages)
# print(total_seconds)

# print(103 // 60, ":", 103 % 60)



# listen_for_stop()


# print(lengths)
