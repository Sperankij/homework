list = []

while True:
    try:
        var = eval(input(">>>"))  
        print(var)
        if var in list:
            print(f"{var} это число Асемблера")
        else:
            print(f"{var} это не число Асемблера")
    except Exception as e:
        print(f"Ошибка: {e}")
  
