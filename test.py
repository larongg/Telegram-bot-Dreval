from answers import Answers
import random
import string


random.seed(10)
answers = {}

for l in string.ascii_uppercase[:18]:
    tops = [1, 2, 3, 4, 5]
    random.shuffle(tops)
    answers[l] = tops

ans = Answers(answers)
print(ans.sorted())


excel_dreval = {
    'Синтетический стиль': [],
    'Идеалистический стиль': [],
    'Прагматический стиль': [],
    'Аналитичесеий стиль': [],
    'Реалистический стиль': []
}

k = 0
lst = [
    "Синтетический стиль",
    "Идеалистический стиль",
    "Прагматический стиль",
    "Аналитичесеий стиль",
    "Реалистический стиль"
]

for res in ans.sorted().split('\n'):
    excel_dreval[lst[k]].append(res.replace(lst[k] + ": ", ''))
    k += 1

print(excel_dreval)