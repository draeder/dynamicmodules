from importmodules import ImportModules

imports = ImportModules()

my_classes = imports.imp('apiAdapters')
print(my_classes)
print(list(my_classes.values())[0])

list(my_classes.values())[0]()
