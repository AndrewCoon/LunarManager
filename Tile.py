import random

class Tile:
  pos_states = [ice_high, ice_medium, ice_low, solar, hazard]
  states = []
  def __init__():
    geoconstraints = randint(0, len(pos_states))
    for i in range(geoconstraints):
      loc = randint(0, len(pos_states))
      states.append(pos_states[loc])
      pos_states.pop(loc)
      
            
