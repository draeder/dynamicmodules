import os
import sys
from importlib import __import__


class ImportModules:
    def imp(self, path):
        api_adapters = {}
        for folder in os.scandir(path):
            api_adapter = folder.name
            sys.path.insert(0, path + '/' + api_adapter)
            class_name = api_adapter.capitalize()

            api_adapters[api_adapter] = next(os.walk(path + '/' + folder.name), (None, None, []))[2]  # [] if no file

            if len(api_adapters[api_adapter]) > 0:
                module = __import__(api_adapter)
                my_classes = {api_adapter: getattr(module, class_name)}
                return my_classes
            else:
                print(api_adapter + ' Does not have any files or importable classes')
