import importlib

from pluginBase import PluginBase


class Bot:
    def __init__(self, plugins: list = []):
        self._plugins = []
        if plugins != []:
            for plugin in plugins:
                pluginToAdd = importlib.import_module(plugin, ".").Plugin()
                if isinstance(pluginToAdd, PluginBase):
                    self._plugins.append(pluginToAdd)
        # if no plugin list is supplied use the default one
        else:
            self._plugins = [importlib.import_module("default", ".").Plugin()]

    def run(self):
        for plugin in self._plugins:
            print(isinstance(plugin, PluginBase))
            plugin.process()
