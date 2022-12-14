import string
import random

class Answers:
    def __init__(self, init_dict):
        self.dict = {}
        self.values = tuple(init_dict.values())

        for i in range(1, 18+1):
            self.dict[i] = {
                "а": self.values[i-1][0],
                "б": self.values[i-1][1],
                "в": self.values[i-1][2],
                "г": self.values[i-1][3],
                "д": self.values[i-1][4],
            }

    def is_correct(self):
        s = 0
        for answer in self.values:
            s += sum(answer)

        return s==270

    def sorted(self):
        d = self.dict

        sint = d[1]["а"]  + d[2]["б"]  + d[3]["д"] \
             + d[4]["г"]  + d[5]["в"]  + d[6]["б"] \
             + d[7]["а"]  + d[8]["б"]  + d[9]["д"] \
             + d[10]["г"] + d[11]["в"] + d[12]["б"] \
             + d[13]["а"] + d[14]["б"] + d[15]["д"] \
             + d[16]["г"] + d[17]["в"] + d[18]["б"]

        ideal = d[1]["б"]  + d[2]["а"]  + d[3]["а"] \
              + d[4]["д"]  + d[5]["а"]  + d[6]["в"] \
              + d[7]["б"]  + d[8]["а"]  + d[9]["г"] \
              + d[10]["в"] + d[11]["а"] + d[12]["в"] \
              + d[13]["б"] + d[14]["а"] + d[15]["г"] \
              + d[16]["в"] + d[17]["а"] + d[18]["в"]

        pragm = d[1]["в"]  + d[2]["г"]  + d[3]["а"] \
              + d[4]["д"]  + d[5]["а"]  + d[6]["в"] \
              + d[7]["б"]  + d[8]["а"]  + d[9]["г"] \
              + d[10]["д"] + d[11]["б"] + d[12]["г"] \
              + d[13]["в"] + d[14]["г"] + d[15]["а"] \
              + d[16]["д"] + d[17]["б"] + d[18]["г"]

        anal = d[1]["г"]  + d[2]["в"]  + d[3]["в"] \
             + d[4]["а"]  + d[5]["д"]  + d[6]["д"] \
             + d[7]["г"]  + d[8]["в"]  + d[9]["в"] \
             + d[10]["а"] + d[11]["д"] + d[12]["д"] \
             + d[13]["г"] + d[14]["в"] + d[15]["в"] \
             + d[16]["а"] + d[17]["д"] + d[18]["д"]

        real = d[1]["д"]  + d[2]["д"]  + d[3]["б"] \
             + d[4]["б"]  + d[5]["г"]  + d[6]["а"] \
             + d[7]["д"]  + d[8]["д"]  + d[9]["б"] \
             + d[10]["б"] + d[11]["г"] + d[12]["а"] \
             + d[13]["д"] + d[14]["д"] + d[15]["б"] \
             + d[16]["б"] + d[17]["г"] + d[18]["а"]
        
        return ("Синтетический стиль: " + str(sint) +
                "\nИдеалистический стиль: " + str(ideal) +
                "\nПрагматический стиль: " + str(pragm) +
                "\nАналитичесеий стиль: " + str(anal) +
                "\nРеалистический стиль: " + str(real)
        )

if __name__ == "__main__":
    random.seed(10)
    answers = {}

    for l in string.ascii_uppercase[:18]:
        tops = [1, 2, 3, 4, 5]
        random.shuffle(tops)
        answers[l] = tops

    ans = Answers(answers)
    print(ans.sorted())
