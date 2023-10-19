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
                lab.redact(self.position, 3)
            case 2:
                lab.set_condition(2)
            case 4:
                lab.set_condition(3)
            case 5:
                lab.redact(self.position, 0)
                self.position = lab.random_position()
                lab.redact(self.position, 3)
