import matplotlib.pyplot as mtp
import csv
with open ("elden_ring_weapon.csv","r",newline ="") as file:
    reader = csv.reader(file)
    weaponclasses = {}
    smithing = 0
    somber = 0
    for line in reader:
        current_class = line[1]
        if current_class not in weaponclasses and line[1] != "Type":
            weaponclasses[current_class] = 1
        elif line[1] != "Type":
            weaponclasses[current_class] += 1
        if line[23] == "Smithing Stones":
            smithing += 1
        elif line[23] == "Somber Smithing Stones":
            somber += 1 
    x = weaponclasses.keys()
    y = weaponclasses.values()
    mtp.style.use('seaborn-v0_8-dark')
    mtp.bar(x, y)
    mtp.title("elden ring weapon types")
    mtp.xlabel("weapon class")
    mtp.ylabel("frequency")
    mtp.xticks(rotation = 90)
    mtp.grid()
    mtp.subplot(1, 2, 1)
    labels = ["Smithing Stones", "Somber Smithing Stones"]
    slices = [smithing, somber]
    mtp.pie(slices, labels=labels)
    mtp.show()
    
