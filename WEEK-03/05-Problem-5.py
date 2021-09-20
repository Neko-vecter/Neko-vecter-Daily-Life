l = [10, 4, 1, 0, 1, 8, 12]
rotate_num = int(input("input how much num you want to rotate?: "))

def NumSift(lists, num):
    output_list = []

    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
       
    for item in range(0, len(lists) - num): 
        output_list.append(lists[item])
          
    return output_list
  
print(NumSift(l, rotate_num))