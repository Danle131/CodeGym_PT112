check_conversion = int(input(
    "What type of conversion you want to perform?\n" \
    "Press 1 to convert Fahrenheit to Celsius\n" \
    "Press 2 to convert Celsius to Fahrenheit\n" \
    "Type here: "
))

#Chương trình chuyển đổi nhiệt độ
class degree_convert:
    def FtoC(degree_F):
        degree_C = float((degree_F - 32)*5/9)
        print(f'{degree_F}°F is approximately {degree_C:.5f}°C')
    def CtoF(degree_C):
        degree_F = float((degree_C)*9/5 + 32)
        print(f'{degree_C}°C is approximately {degree_F:.5f}°F')

if check_conversion == 1:
    print("You chose \"Fahrenheit to Celsius\"")
    input_F = float(input("Please input Fahrenheit degree: "))
    degree_convert.FtoC(input_F)
elif check_conversion == 2:
    print("You chose \"Celsius to Fahrenheit\"")
    input_C = float(input("Please input Celsius degree: "))
    degree_convert.CtoF(input_C)
else:
    print("I told you to just type 1 or 2. Terminate the program and rerun it to try again.")