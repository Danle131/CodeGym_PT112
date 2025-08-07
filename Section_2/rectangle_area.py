width = float(input("Please input rectangle width: "))
length = float(input("Please input rectangle length: "))

#Tính diện tích và in ra giá trị vừa tính
def calc(rec_width,rec_length):
    area = float(rec_width * rec_length)
    print(f'The approximate area of the given rectangle is {area:.5f}')

calc(width,length)

