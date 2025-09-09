s_in = input("Nhập string: ")
def reverse_string(s):
    temp = s[0]
    i = 0
    l = len(s)
    if l == 0 or l == 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
    
print(f"String moi = {reverse_string(s_in)}")
