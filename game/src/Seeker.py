class Seeker:
    __position = None

    def __init__(self, lab):
        self.position = lab.random_position()
        lab.redact(self.position, 3)

    def get_position(self):
        return self.position

    def move(self, lab, direction):
        match direction:
            case "Up":
                match lab.get_config()[self.position[0] - 1][self.position[1]]:
                    case 0:
                        lab.redact(self.position, 0)
                        self.position = [self.position[0] - 1, self.position[1]]
                        lab.redact(self.position, 3)
                    case 2:
                        lab.set_condition(2)
                    case 4:
                        lab.set_condition(3)
                    case 5:
                        lab.redact(self.position, 0)
                        self.position = lab.random_position()
                        lab.redact(self.position, 3)
            case "Down":
                match lab.get_config()[self.position[0] + 1][self.position[1]]:
                    case 0:
                        lab.redact(self.position, 0)
                        self.position = [self.position[0] + 1, self.position[1]]
                        lab.redact(self.position, 3)
                    case 2:
                        lab.set_condition(2)
                    case 4:
                        lab.set_condition(3)
                    case 5:
                        lab.redact(self.position, 0)
                        self.position = lab.random_position()
                        lab.redact(self.position, 3)
            case "Left":
                match lab.get_config()[self.position[0]][self.position[1] - 1]:
                    case 0:
                        lab.redact(self.position, 0)
                        self.position = [self.position[0], self.position[1] - 1]
                        lab.redact(self.position, 3)
                    case 2:
                        lab.set_condition(2)
                    case 4:
                        lab.set_condition(3)
                    case 5:
                        lab.redact(self.position, 0)
                        self.position = lab.random_position()
                        lab.redact(self.position, 3)
            case "Right":
                match lab.get_config()[self.position[0]][self.position[1] + 1]:
                    case 0:
                        lab.redact(self.position, 0)
                        self.position = [self.position[0], self.position[1] + 1]
                        lab.redact(self.position, 3)
                    case 2:
                        lab.set_condition(2)
                    case 4:
                        lab.set_condition(3)
                    case 5:
                        lab.redact(self.position, 0)
                        self.position = lab.random_position()
                        lab.redact(self.position, 3)
