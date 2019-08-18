def add_symbol(func1):
    def prt_func(name):
        return '&&&{0}&&&'.format(func1(name))
    return prt_func

@add_symbol
def print_name(name):
    return 'fuck, ' + name

if __name__ == "__main__":

    print(print_name('world'))