def list_sorter(list_to_sort):
    
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    
    return list_to_sort
    
    
while True:
    
    print("This program will sort list of integers and find greatest difference between adjascent numbers")
    
    try:
        x = input("Enter even amount (at least 4) of integers, separated by space: ")

        if x.lower() == "exit":
            print("Bye, bye")
            break
    
        list_to_sort = [int(i) for i in x.split()]
    
        if len(list_to_sort) % 2 != 0:
            print("\nPlease enter even amount (at least 4) of integers!")
            continue
        
        elif len(list_to_sort) < 4:
            print("\vPlease enter at least 4 integers!")
            continue
        
        else:
            sorted_list = list_sorter(list_to_sort)
            
            diffs = []
            
            for i in range(len(sorted_list) - 1):
                diffs.append(sorted_list[i + 1] - sorted_list[i])
            
            print(f"\nThe greatest difference between adjacent elements is: {max(diffs)}")
            
            break
    
    except ValueError:
        print("\nYou should enter only digits, separted by spaces!")




