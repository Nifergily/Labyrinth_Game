import Auxiliary as au


class Shadow:
    def __init__(self, lab):
        self.position = au.random_position(lab)
        self.direction = au.random_direction("")
        self.check = True

    def redact_lab(self, lab):
        lab[self.position[0]][self.position[1]] = 2
        return lab

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
                match lab[self.position[0] - 1][self.position[1]]:
                    case 0:
                        lab[self.position[0] - 1][self.position[1]] = 2
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0] - 1, self.position[1]]
                    case 3:
                        lab[0][0] = -1
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 2
                    case _:
                        self.direction = au.random_direction(self.direction)
            case "Down":
                match lab[self.position[0] + 1][self.position[1]]:
                    case 0:
                        lab[self.position[0] + 1][self.position[1]] = 2
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0] + 1, self.position[1]]
                    case 3:
                        lab[0][0] = -1
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 2
                    case _:
                        self.direction = au.random_direction(self.direction)
            case "Left":
                match lab[self.position[0]][self.position[1] - 1]:
                    case 0:
                        lab[self.position[0]][self.position[1] - 1] = 2
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0], self.position[1] - 1]
                    case 3:
                        lab[0][0] = -1
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 2
                    case _:
                        self.direction = au.random_direction(self.direction)
            case "Right":
                match lab[self.position[0]][self.position[1] + 1]:
                    case 0:
                        lab[self.position[0]][self.position[1] + 1] = 2
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0], self.position[1] + 1]
                    case 3:
                        lab[0][0] = -1
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 2
                    case _:
                        self.direction = au.random_direction(self.direction)
        return lab
