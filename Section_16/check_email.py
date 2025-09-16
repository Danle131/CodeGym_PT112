email = input("Nhập email của bạn: ").strip()
def check_mail(a):
    if (a.find("@") == -1 or a.find(".") == -1):
        return False
    if (a.find("@") > a.find(".")):
        return False
    if (a.find("@") == 0 or a.find("@") == len(a) - 1):
        return False
    return a.lower()

print(check_mail(email))
