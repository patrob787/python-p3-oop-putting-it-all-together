#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0, condition=''):
        self.brand = brand
        self.size = size
        self.condition = condition

    def set_size(self):
        return self._size
    
    def get_size(self, size):
        if type(size) != int:
            print("size must be an integer")
        else:
            self._size = size
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    size = property(set_size, get_size)