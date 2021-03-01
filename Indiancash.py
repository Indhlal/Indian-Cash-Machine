# Greedy algorithm for Indian Cashier System developed by Indhlal
def main():


    # Denominations Available in the counter

    twok = 500
    fhundred = 500
    thundred = 500
    hundred  = 500
    fifty = 500
    twenty = 500
    ten = 500
    five = 500
    two = 500
    one = 500
    counter = 0
    while True:
        try:

            #Denominations
            Denominations2k = 0
            Denominations500 = 0
            Denominations200 = 0
            Denominations100 = 0
            Denominations50 = 0
            Denominations20 = 0
            Denominations10 = 0
            Denominations5 = 0
            Denominations2 = 0
            Denominations1 = 0


            price = int(input("Price of product: "))
            cashrvd = int(input("Cash Received: "))
            print("----------------------------------------")
            balance = cashrvd - price
            print(f"Balance: {balance}")
            print("----------------------------------------")
            print("\nDENOMINATIONS\n")
            # print("----------------------------------------")

            # 2000
            while balance >= 2000:
                if twok > 0:
                    balance = balance - 2000
                    counter += 1
                    Denominations2k += 1
                    twok -= 1
                else:
                    print("Alert!!!Rs.2000 Denominations drained out.\n")
                    break


            # 500    
            while balance >= 500:
                if fhundred > 0:
                    balance = balance - 500
                    counter += 1
                    Denominations500 += 1
                    fhundred -= 1
                else:
                    print("Alert!!!Rs.500 Denominations drained out.\n")
                    break

            # 200
            while balance >= 200:
                if thundred > 0:
                    balance = balance - 200
                    counter += 1
                    Denominations200 += 1
                    thundred -= 1
                else:
                    print("Alert!!!Rs.200 Denominations drained out.\n")
                    break

            # 100    
            while balance >= 100:
                if hundred > 0:
                    balance = balance - 100
                    counter += 1
                    Denominations100 += 1
                    hundred -= 1
                else:
                    print("Alert!!!Rs.100 Denominations drained out.\n")
                    break

            # 50    
            while balance >= 50:
                if fifty > 0:
                    balance = balance - 50
                    counter += 1
                    Denominations50 += 1
                    fifty -= 1
                else:
                    print("Alert!!!Rs.50 Denominations drained out.\n")
                    break

            # 20
            while balance >= 20:
                if twenty > 0:
                    balance = balance - 20
                    counter += 1
                    Denominations20 += 1
                    twenty -= 1
                else:
                    print("Alert!!!Rs.20 Denominations drained out.\n")
                    break

            # 10
            while balance >= 10:
                if ten > 0:
                    balance = balance - 10
                    counter += 1
                    Denominations10 += 1
                    ten -= 1
                else:
                    print("Alert!!!Rs.10 Denominations drained out.\n")
                    break

            # 5
            while balance >= 5:
                if five > 0:
                    balance = balance - 5
                    counter += 1
                    Denominations5 += 1
                    five -= 1
                else:
                    print("Alert!!!Rs.5 Denominations drained out.\n")
                    break

            #2
            while balance >= 2:
                if two > 0:
                    balance = balance - 2
                    counter += 1
                    Denominations2 += 1
                    two -= 1
                else:
                    print("Alert!!!Rs.2 Denominations drained out.\n")
                    break


            #1
            while balance >= 1:
                if one > 0:
                    balance = balance - 1
                    counter += 1
                    Denominations1 += 1
                    one -= 1
                else:
                    print("Alert!!!Rs.1 Denominations drained out.\n")
                    break



            # Refill if limit exceeded
            if twok < 100 and twok > 0:
                refill("2000")
            if fhundred < 100 and fhundred > 0:
                refill("500")
            if thundred < 100 and thundred > 0:
                refill("200")
            if hundred < 100 and hundred > 0:
                refill("100")
            if fifty < 100 and fifty > 0:
                refill("50")
            if twenty < 100 and twenty > 0:
                refill("20")
            if ten < 100 and ten > 0:
                refill("10")
            if five < 100 and five > 0:
                refill("5")
            if two < 100 and two > 0:
                refill("2")
            if one < 100 and one > 0:
                refill("1")


            # How much quantity of denominations are needed
            if Denominations2k > 0:
                print(f"Rs.2000 = {Denominations2k}")
            if Denominations500 > 0:
                print(f"Rs.500 = {Denominations500}")
            if Denominations200 > 0:
                print(f"Rs.200 = {Denominations200}")
            if Denominations100 > 0:
                print(f"Rs.100 = {Denominations100}")
            if Denominations50 > 0:
                print(f"Rs.50 = {Denominations50}")
            if Denominations20 > 0:
                print(f"Rs.20 = {Denominations20}")
            if Denominations10 > 0:
                print(f"Rs.10 = {Denominations10}")
            if Denominations5 > 0:
                print(f"Rs.5 = {Denominations5}")
            if Denominations2 > 0:
                print(f"Rs.2 = {Denominations2}")
            if Denominations1 > 0:
                print(f"Rs.1 = {Denominations1}")

            print("\n----------------------------------------")
            print(f"Total Denominations: {counter}")
            print("----------------------------------------")
            print("\n")


            #break  
        except ValueError:
            print("Enter proper values")

# Definition of Refill Function
def refill(x):
    print(f"\tAlert!!!\nRs.{x} is about to come to the limit. Refill Immedietly")
main()