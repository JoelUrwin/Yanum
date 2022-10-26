import yaml
from yaml import Loader, Dumper

class Yanum():

    def __init__(self,args):
        self.file = args['f']
        self.yaml = yaml.load(self.file, Loader=Loader)
