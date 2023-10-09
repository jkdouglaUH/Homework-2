def exact_change(total):
  doll = total // 100
  total %= 100
  qtr = total // 25
  total %= 25
  dime = total // 10
  total %= 10
  nick = total // 5
  total %= 5
  penn = total
  return doll, qtr, dime, nick, penn
leftchange = int(input("How much change is left "))
doll, qtr, dime, nick, penn = exact_change(leftchange)
if leftchange <= 0:
  print("No change")
else:
  if doll > 0:
    if doll == 1:
        print(doll, "dollar")
    else:
        print(doll, "dollars")
  if qtr > 0:
    if qtr == 1:
        print(qtr, "quarter")
    else:
        print(qtr, "quarters")
  if dime > 0:
    if dime == 1:
        print(dime, "dime")
    else:
        print(dime, "dimes")
  if nick > 0:
    if nick == 1:
        print(nick, "nickel")
    else:
        print(nick, "nickels")
  if penn > 0:
    if penn == 1:
        print(penn, "penny")
    else:
        print(penn, "pennies")