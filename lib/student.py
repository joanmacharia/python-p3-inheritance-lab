#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first_name, last_name, knowledge=[]) -> None:
        super().__init__(first_name, last_name)
        self.knowledge = knowledge
    
    def learn(self, new_information):
        return self.knowledge.append(new_information)
        pass