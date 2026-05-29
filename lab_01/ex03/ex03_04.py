def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]  # Truy cập phần tử đầu tiên
    last_element = tuple_data[-1]  # Truy cập phần tử cuối cùng
    return first_element, last_element

#Nhập tuple từ người dùng 
input_tuple = eval(input("Nhập một tuple (ví dụ: (1, 2, 3, 4)): "))
first, last = truy_cap_phan_tu(input_tuple)

#In kết quả
print("Phần tử đầu tiên của tuple là:", first)
print("Phần tử cuối cùng của tuple là:", last)