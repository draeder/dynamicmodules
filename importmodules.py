import os
import sys
from importlib import __import__


class ImportModules:
    def imp(self, path):
        my_classes = {}
        for folder in os.scandir(path):
            api_adapter = folder.name
            sys.path.insert(0, path + '/' + api_adapter)
            class_name = api_adapter.capitalize()
            module = __import__(api_adapter)
            my_classes[api_adapter] = getattr(module, class_name)
        return my_classes
