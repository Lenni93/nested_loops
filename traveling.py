destination = input()
savedMoney = 0
while destination != "End":
    neededMoney = float(input())
    while savedMoney <= neededMoney:
        # savedMoney is the counter
        money = float(input())
        # savedMoney += money
        if savedMoney >= neededMoney:
            # saveMoney is increased
            print(f"Going to {destination}!")
            break
    savedMoney = 0
    destination = input()