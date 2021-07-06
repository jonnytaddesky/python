from dataclasses import dataclass


class Question:

    def __init__(self, text, is_true, explanation):
        self.explanation = explanation
        self.is_true = is_true
        self.text = text


@dataclass
class Question:
    text: str
    is_true: bool
    explanation: str


q = Question('test', True, 'because')
print(q.text)

q = Question('test', True)