import random


class Shadow:
    __position = None
    __direction = None
    __check = None

    def __init__(self, lab):
        self.position = lab.random_position()
        lab.redact(self.position, 2)
        self.direction = ""
        self.random_direction()
        self.check = True

    def think(self, lab, target):
        self.check = True
        if self.position[0] == target[0]:
            if self.position[1] < target[1]:
                for i in range(self.position[1], target[1]):
                    if lab[target[0]][i] == 1:
                        self.check = False
                        break
                if self.check:
                    self.direction = "Right"
            else:
                for i in range(target[1], self.position[1]):
                    if lab[target[0]][i] == 1:
                        self.check = False
                        break
                if self.check:
                    self.direction = "Left"
        elif self.position[1] == target[1]:
            if self.position[0] < target[0]:
                for i in range(self.position[0], target[0]):
                    if lab[i][target[1]] == 1:
                        self.check = False
                        break
                if self.check:
                    self.direction = "Down"
            else:
                for i in range(target[0], self.position[0]):
                    if lab[i][target[1]] == 1:
                        self.check = False
                        break
                if self.check:
                    self.direction = "Up"

    def move(self, lab):
        match self.direction:
            case "Up":
                self.specific_move(lab, (self.position[0] - 1, self.position[1]))
            case "Down":
                self.specific_move(lab, (self.position[0] + 1, self.position[1]))
            case "Left":
                self.specific_move(lab, (self.position[0], self.position[1] - 1))
            case "Right":
                self.specific_move(lab, (self.position[0], self.position[1] + 1))

    def specific_move(self, lab, pos):
        match lab.get_config()[pos[0]][pos[1]]:
            case 0:
                lab.redact(self.position, 0)
                self.position = pos
                lab.redact(self.position, 2)
            case 3:
                lab.set_condition(2)
            case 5:
                lab.redact(self.position, 0)
                self.position = lab.random_position()
                lab.redact(self.position, 2)
            case _:
                self.random_direction()

    def random_direction(self):
        while True:
            match random.randint(1, 4):
                case 1:
                    result = "Up"
                case 2:
                    result = "Down"
                case 3:
                    result = "Left"
                case 4:
                    result = "Right"
                case _:
                    result = ""
            if result != self.direction:
                self.direction = result
                break
