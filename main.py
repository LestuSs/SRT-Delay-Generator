# Made by Raphaël QUETELART
import tkinter as tk
from tkinter import filedialog
from os import path

def pick_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

address = pick_file()

with open(address, 'r') as f:
    lines = f.readlines()

newLines = []

delay = input("Input delay in ms : ")
fileName, fileExtension = path.splitext(path.basename(address))
newAddress = address.replace(fileName, fileName + "_addedDelay_" + delay + "ms")
delay = int(delay)

def addDelay(msDelay, hours, mins, sec, ms):
    ans = [hours, mins, sec, ms]
    if msDelay < 0:
        msDelay = msDelay*(-1)
        secDelay = msDelay // 1000
        msDelay = msDelay % 1000
        ans[3] -= msDelay
        ans[2] -= secDelay
        if ans[3] < 0:
            ans[2] -= 1
            ans[3] = abs(1000 + ans[3])
        if ans[2] < 0:
            ans[1] -= 1
            ans[2] = abs(60 + ans[2])
        if ans[1] < 0:
            if ans[0] > 0:
                ans[0] -= 1
                ans[1] = abs(60 + ans[1])
            else:
                ans = [00, 00, 00, 000]
    else:
        secDelay = msDelay // 1000
        msDelay = msDelay % 1000
        ans[3] += msDelay
        ans[2] += secDelay
        if ans[3] >= 1000:
            ans[2] += (ans[3] // 1000)
            ans[3] = ans[3] % 1000
        if ans[2] >= 60:
            ans[1] += ans[2] % 60
            ans[2] = ans[2] - 60*(ans[2] // 60)
        if ans[1] >= 60:
            ans[0] += 1
            ans[1] -= 60
    toReturn = ""
    ans[0] = str(ans[0])
    ans[1] = str(ans[1])
    ans[2] = str(ans[2])
    ans[3] = str(ans[3])
    for n in range(3):
        if len(ans[n]) < 2:
            ans[n] = "0" + ans[n]
    if len(ans[3]) < 3:
        ans[3] = "0" + ans[3]
        if len(ans[3]) < 3:
            ans[3] = "0" + ans[3]
    return(ans[0] + ":" + ans[1] + ":" + ans[2] + "," + ans[3])

for i in range(len(lines)):
    if ("-->" in lines[i] and lines[i][0].isdigit()):
        hoursBeginning = int(lines[i][0:2])
        minBeginning = int(lines[i][3:5])
        secBeginning = int(lines[i][6:8])
        msBeginning = int(lines[i][9:12])
        hoursEnd = int(lines[i][17:19])
        minEnd = int(lines[i][20:22])
        secEnd = int(lines[i][23:25])
        msEnd = int(lines[i][26:29])
        newLines.append(addDelay(delay, hoursBeginning, minBeginning, secBeginning, msBeginning) + " --> " + addDelay(delay, hoursEnd, minEnd, secEnd, msEnd) + "\n")
    else:
        newLines.append(lines[i])

with open(newAddress, 'w') as f:
    f.writelines(newLines)
