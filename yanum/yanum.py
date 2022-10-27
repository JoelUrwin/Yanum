import yaml
from yaml import load, Loader

class Yanum():
    def __init__(self, args):
        self.filepath = args['f']
        self.yaml = load(self.filepath, Loader=Loader)
        self.keys = list(self.yaml.keys())
        self.values = list(*self.yaml.values())
        self.dump = yaml.dump(self.yaml)

        self.dumpfile = open("yanum.java","w")

        def parser():
            print(self.values)
            print(self.keys)

        if args['f']:
            self.dumpfile.write(f"enum {self.keys[0]} "+"{")
            parser()






