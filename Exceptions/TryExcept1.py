def func(x):
    try:
        ans = 100/x
        print(ans)

    except ZeroDivisionError:
        print(f'Incorrect value for the denominator. {x} is not accepted.')
    except TypeError:
        print('Wrong data type of input value')
    finally:
        print('Program End.')

func('5')