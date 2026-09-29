classrecord = {
    "Roxxy": {
        "StudID": "S001",
        "Grade": [90, 85, 86, 82, 83, 90, 92]
    },
    "Sylphy": {
        "StudID": "S002",
        "Grade": [98, 89, 94, 97, 98, 97, 98]
    },
     "Eris": {
        "StudID": "S003",
        "Grade": [95, 93, 91, 96, 89, 94, 97]
    },

    }

search = input("Enter student name or ID: ")

found = False

for name, classrecord in classrecord.items():

    if search.lower() == name.lower() or search.lower() == classrecord["StudID"].lower():

        found = True

        print("\nStudent Found!")
        print("ID:", classrecord["StudID"])
        print("Name:", name)
        print("Grades:", classrecord["Grade"])

        average = sum(classrecord["Grade"]) / len(classrecord["Grade"])
        print("Average:", round(average, 2))

        for grade in classrecord["Grade"]:
            if grade < 60:
                print("Candidate for Intervention.")
                break

        print("Highest Grade:", max(classrecord["Grade"]))
        print("Lowest Grade:", min(classrecord["Grade"]))

        break

if found == False:
    print("Student not found.")