def printvar(target_func):
    def enhanced_func(target_arg):
        res = target_func(target_arg)
        print(res)
    return enhanced_func

@printvar
def doublevar(target_var):
    return target_var * 2

doublevar(2)