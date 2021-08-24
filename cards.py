# cards template
class Card:
    def __init__(self, name):
        self.name = name

class Action:
    def __init__(self, type):
        self.type = type

class Item:
    def __init__(self, ability, swag):
        self.ability = ability
        self.swag = swag        

class Danger: 
    def __init__(self, rollranges):
        self.rollranges = rollranges

class Player:
    def __init__(self, ability, swag, specialability, crazy, tag):
        self.ability = ability
        self.swag = swag
        self.specialability = specialability
        self.crazy = crazy
        self.tag = tag