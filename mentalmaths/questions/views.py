from django.views import generic

import random
import math


class Question:

    def __init__(self):
        self.value1 = 1
        self.value2 = 2
        self.operator = ""

        self.randomise()

    def randomise(self):

        OPERATORS = ["x", "÷", "+", "-"]
        self.value1 = random.randint(1, 100)
        self.value2 = random.randint(1, 100)
        self.operator = random.choice(OPERATORS)

        if self.operator == "÷":
            while not (self.value1 / self.value2).is_integer():
                self.value1 = random.randint(1, 100)
                self.value2 = random.randint(1, int(math.sqrt(self.value1)))

    def has_integer_answer_for_division(self):
        return (self.value1 / self.value2).is_integer()

    def __str__(self):
        return f"{self.value1} {self.operator} {self.value2} = _______"


# Create your views here.
class QuestionsView(generic.ListView):
    template_name = 'questions/questions.html'
    context_object_name = 'questions_list'

    def get_queryset(self):
        return [Question() for i in range(10)]
