def switch_case(case):
    switcher = {
        1: "Case 1",
        2: "Case 2",
        3: "Case 3"
    }
    return switcher.get(case, "Invalid case")

print(switch_case(2))
