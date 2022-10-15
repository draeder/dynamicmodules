from importmodules import ImportModules

imports = ImportModules()

my_classes = imports.imp('apiAdapters')

list(my_classes.values())[0]()  # <-- Executes the first function of the class
