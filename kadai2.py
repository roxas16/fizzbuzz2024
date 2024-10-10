def fizz_buzz():

    uwaki_count = int(input("いくつまで数えますか？: "))
    
  
    for danger_level in range(1, uwaki_count + 1):
        if danger_level % 15 == 0:
            print("Fizz Buzz")
        elif danger_level % 3 == 0:
            print("Fizz")
        elif danger_level % 5 == 0:
            print("Buzz")
        else:
            print(danger_level)

fizz_buzz()