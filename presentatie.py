def presenteer(**d):
    for key, value in d.items():
        print(f"{key} : {value}")
    print("="*26)
    totaal = sum(d.values())
    print(f"totaal: {totaal}")
