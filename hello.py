def scope_test():
    def scope_local():
        scope = 'local'
    def scope_non_local():
        scope ='nonlocal'
    def scope_global():
        global scope
        scope = "global"
    scope = "test scope"
    print(scope)
    scope_non_local()
scope_test()
print(scope)
