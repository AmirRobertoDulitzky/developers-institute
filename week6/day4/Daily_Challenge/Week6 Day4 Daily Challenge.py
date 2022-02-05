
get_age = int(input(f"what is your birthday?\n"
                f"(if 1995 nov 5 type: 19951105"))
age = (20220205 - get_age) * 0.0001
age = int(age)
age = str(age)


candle = "i"
candles = candle*int((age[-1]))
if age[-1] == "0":
    candles = candle*10

print(f"        {candles}         \n"
      f"       |:H:a:p:p:y:|        \n"
      f"     __|___________|__      \n"
      f"    |^^^^^^^^^^^^^^^^^|     \n"
      f"    |:B:i:r:t:h:d:a:y:|     \n"
      f"    |                 |     \n"
      f"    ~~~~~~~~~~~~~~~~~~~       ")

