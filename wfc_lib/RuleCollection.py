from wfc_lib import *


class RuleCollection:
    def __init__(self, rule_list: list[Rule] = []):
        self.collection = {rule.applies_to:rule for rule in rule_list}

        self.members: list[str] = []

        self.__update()

    def add_rule(self, rule):
        self.collection[rule.applies_to] = rule
        self.__update()

    def remove_rule(self, key: str):
        self.collection.pop(key)

    def get(self, key):
        return self.collection.get(key)

    def __update(self):
        self.members = list(self.collection.keys())
