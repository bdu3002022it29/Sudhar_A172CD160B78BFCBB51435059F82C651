# define base class player
class player (self):
  def play(self):
    print("The player is playing cricket.")

# define derived class batsman
class Batsman(player):
  def play(self):
    print("The batsman is batting.")

# define derived class bowler
class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

# create object of batsman and bowler classes
batsman = Batsman()
bowler = Bowler()

# call play() method
batsman.play()
bowler.play()