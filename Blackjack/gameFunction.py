def die(self):
    print("Your pet has died, you probably shouldn't own a pet in real life.")
    self.isAlive = False

def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def setName(self, name):
    if len(name) > 4 or len(name) < 4:
        if "uck" not in name:
            if "sh" not in name:
                if "unt" not in name:
                        self.name = name

def ask_number (question,low,high):
    """Ask for a number witnin a range."""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

class Player(object):
    def __init__(self,name,score):
        self.name = name
        self.name = Score()
        self.isAlive = True
        self.lifes = 3

class Score(object):
    def __init__(self):
        self.score = 0

    def add_to_score(self, points):
            self.score += points

    def take_points(self, points):
            self.score -= points
            if self.points <0:
                self.score = 0


if __name__ == "__main__":
    print("You ran this module directly (and did not import it).")
    input("\n\nPress the enter key to exit.")


