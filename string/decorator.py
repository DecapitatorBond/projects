from datetime import datetime


func_wrap = []
func_clock = []


def wrap(func):
    print("Wrap", func)
    func.append(func)
        result = func(*args, **kwargs)
        print("decorator wrapper", result)
        return result

    return action


def clock(func):
    print("clock", func)
    func_clock.append(func)
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        message = "Start: {0}\nEnd: {1}\n{2}"
        print(message.format(start, end, end-start))
        return result

    return action
@wrap

@clock
def func():
    for i in range(0, 10):
        print(i)


if __name__ == '__main__':
    func()
