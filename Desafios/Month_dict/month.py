month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


user_input = int(input())

if 1 <= user_input <= 12:
    enum_value = month_dict[user_input]
    print(enum_value)
else:
    print("Número fora do intervalo válido.")
