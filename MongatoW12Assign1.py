Mongatopatients = {
    "Velasquez": (80, 50, 150, 90, 140, 160, 70),
    "Junasa": (130, 140, 135, 90, 140, 150, 180),
    "Jacomille": (90, 100, 95, 90, 140, 80, 140)
}

for Mongatopatient, Mongatoreadings in Mongatopatients.items():
    print("Patient:", Mongatopatient)

    MongatoHighcount = 0
    print("Blood Sugar Summary")

    for Mongatoreading in Mongatoreadings:
        if Mongatoreading >= 120:
            Mongatostatus = "High"
            MongatoHighcount += 1
        else:
            jacomillestatus = "Normal"

    Mongatomax = max(Mongatoreadings)
    Mongatomin = min(Mongatoreadings)
    Mongatoavg = sum(Mongatoreadings) / len(Mongatoreadings)
    Mongatodiff = Mongatomax - Mongatomin

    print("Number of High Readings:", MongatoHighcount)
    print()
    print(f"Maximum Blood Sugar: {Mongatomax:.0f}")
    print(f"Minimum Blood Sugar: {Mongatomin:.0f}")
    print(f"Average Blood Sugar: {Mongatoavg:.0f}")
    print(f"Difference Blood Sugar: {Mongatodiff}")
    print()