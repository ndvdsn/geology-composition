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
1.2, 0.1, 0.4, 3.0]

lengths2labels = []

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
        return minutes + "m"

for x in range(len(acc_durations)):
    # print(acc_durations[i] + "-" + acc_durations[i + 1])
    print(acc_durations[x] + " - " + acc_durations[x + 1] + "  " + "(" + iszerominutes(str(int(durations[x]//60))) , str(int(durations[x]%60)) + "s) " + lengths1labels[x])
# print(checkDecimals(int(durations[0] //60)))
# print(checkDecimals(int(durations[0] %60)))


# print(sum)
# print(percentages)
# print(total_seconds)

# print(103 // 60, ":", 103 % 60)



# listen_for_stop()


# print(lengths)
