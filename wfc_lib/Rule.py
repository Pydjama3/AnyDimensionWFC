from wfc_lib import *


class Rule:
    def __init__(self, applies_to:str, depends_on):
        self.applies_to = applies_to
        self.depends_on = depends_on

    def get_details(self, x, y):
        return self.depends_on(x, y)
