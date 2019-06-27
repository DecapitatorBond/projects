actions=["+","-","*","/"]


class CalcException(Exception):
    pass

def check(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        arg1, arg2, action = result
        try:
            if"." in arg1:
                arg1 = float(arg1)
            else:
                arg1 = int(arg1)
        except ValueError:
            raise CalcException("Error arg1")

        try:
            if"." in arg2:
                arg2 = float(arg2)
            else:
                arg2 = int(arg2)
        except ValueError:
            raise CalcException("Error arg2")

        if action not in ["+", "-", "/", "*"]:
            raise CalcException("Error action")

        return arg1, arg2, action


def input_data():
    arg1 = input("Введите первое число >> ")
    arg2 = input("Введите второе число >> ")
    action = input("Введите действие >> ")
    return arg1, arg2, action
#
#
#def check_data(arg1, arg2, action):
#    try:
#        if"." in arg1:
#            arg1 = float(arg1)
#        else:
#            arg1 = int(arg1)
#    except ValueError:
#        raise CalcException("Error arg1")
#
#    try:
#        if"." in arg2:
#            arg2 = float(arg2)
#        else:
#            arg2 = int(arg2)
#    except ValueError:
###
    #if action not in ["+", "-", "/", "*"]:
    #    raise CalcException("Error action")
#
    #return arg1, arg2, action


def output_data(arg1, arg2, action):
    if action == "+":
        print(arg1 + arg2)
    elif action == "-":
        print(arg1 - arg2)
    elif action == "*":
        print(arg1 * arg2)
    elif action == "/":
        print(arg1 / arg2)




if __name__ == '__main__':
    try:
        m_arg1, m_arg2, m_action = inpData
    except CalcException as e:
        print(e)
        exit(1)
    outputdata(m_arg1, m_arg2, m_action)
