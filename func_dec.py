admin_password = "14092022"
enter_password = input("Enter your password--> ")

def admin_check(func):
    def wrapper_decorator():
        if enter_password != admin_password:
            return 'Access denied'
        else:
            return func()
    return wrapper_decorator

@admin_check
def account_balance ():
    return "Your accaunt balance is 1.000.000 $"

test1 = account_balance()
print(test1) 