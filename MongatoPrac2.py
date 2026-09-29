studentsL={"Ana": [90,85,82],
           "Kirk": [72,73,78]}

studentsT = {"Ana": (90,85,82),
            "Kirk": (72,73,78)}

for name,grade in studentsL.items():
    print(name,*grade)


