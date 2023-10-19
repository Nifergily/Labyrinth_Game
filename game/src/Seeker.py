import Auxiliary as au


class Seeker:
    def __init__(self, lab):
        self.position = au.random_position(lab)

    def redact_lab(self, lab):
        lab[self.position[0]][self.position[1]] = 3
        return lab

    def move(self, lab, direction):
        match direction:
            case "Up":
                match lab[self.position[0] - 1][self.position[1]]:
                    case 0:
                        lab[self.position[0] - 1][self.position[1]] = 3
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0] - 1, self.position[1]]
                    case 2:
                        lab[0][0] = -1
                    case 4:
                        lab[0][0] = -2
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 3
            case "Down":
                match lab[self.position[0] + 1][self.position[1]]:
                    case 0:
                        lab[self.position[0] + 1][self.position[1]] = 3
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0] + 1, self.position[1]]
                    case 2:
                        lab[0][0] = -1
                    case 4:
                        lab[0][0] = -2
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 3
            case "Left":
                match lab[self.position[0]][self.position[1] - 1]:
                    case 0:
                        lab[self.position[0]][self.position[1] - 1] = 3
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0], self.position[1] - 1]
                    case 2:
                        lab[0][0] = -1
                    case 4:
                        lab[0][0] = -2
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 3
            case "Right":
                match lab[self.position[0]][self.position[1] + 1]:
                    case 0:
                        lab[self.position[0]][self.position[1] + 1] = 3
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = [self.position[0], self.position[1] + 1]
                    case 2:
                        lab[0][0] = -1
                    case 4:
                        lab[0][0] = -2
                    case 5:
                        lab[self.position[0]][self.position[1]] = 0
                        self.position = au.random_position(lab)
                        lab[self.position[0]][self.position[1]] = 3
        return lab

