def tao_Tuple_tu_list(lst):
    return tuple(lst)


# Nhập danh sách số từ người dùng và xử lý chuỗi
input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_Tuple_tu_list(numbers)
print("List: ", numbers)
print("Tuple từ List: ", my_tuple)