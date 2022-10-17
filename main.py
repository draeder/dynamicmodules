from importmodules import ImportModules

imports = ImportModules()

my_classes = imports.imp('apiAdapters')

print(my_classes)

for c in my_classes.items():
    print(c)
    list(c)[1]()
