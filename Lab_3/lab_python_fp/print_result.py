def print_result(fn):
    def fn_name(*args, **kwargs):
        print(fn.__name__)
        result = fn(*args, **kwargs)
        if isinstance(result, dict):
            for key, val in result.items():
                print (key, '=', val)
        elif isinstance(result, list):
            for val in result:
                print (val)
        else:
            print (result)
        return result
    return fn_name

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()