from list_a import _list 

while True:
    try:
        var = eval(input("\n>>> "))  
        print(var)
        if var in _list:
            print(f"{var} это число Асемблера")
        else:
            print(f"{var} это не число Асемблера")
    except Exception as e:
        print(f"Ошибка: {e}")
  
