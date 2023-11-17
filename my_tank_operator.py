from tank_operator import OperatorActions
from tank_operator import GameState
from tank_operator import TankOperator
from src.vec import Vec

class MyTankOperator(TankOperator):
    def __init__(self):
        self.name = "Team 4.2"
    
    def get_operator_name(self):
        return self.name
    
    def get_tank_action(self: TankOperator, gamestate: GameState):
                
        # A little help:
        # Your input is a gamestate object
        # The gamestate object tells you the position and direction of: you, the other tanks, and all shots fired.. 
        # (Check out the tank_operator.py file to see how the gamestate class is defined)
        # You return an OperatorActions object:
        # actions.turn          # [-1.0 to 1.0] left to right respectively.
        # actionsturn_turret    # [-1.0 to 1.0] left to right respectively. Quicker than turning the whole tank.
        # actions.engine        # [-1.0 to 1.0] reverse to full ahead.
        # actions.shoot         # Set to True to fire cannon! Beware that cannon has to reload between shots.
        
        actions = OperatorActions()
        actions.turn_turret = 1

        turret_direction = gamestate.tank.turret_direction.get_orientation_angle()
        looking_right_down = turret_direction > 0 and turret_direction < 90
        if looking_right_down:
            actions.shoot = False
        else:
            actions.shoot = True


        x = gamestate.tank.position.x 
        y = gamestate.tank.position.y

        top_right = x > 700 and y < 250
        top_left = x < 400 and y < 250
        bottom_right = x > 700 and y > 650
        bottom_left = x < 400 and y > 650

        tank_direction = gamestate.tank.direction.get_orientation_angle()

        if x > 1000 or x < 400:
            actions.engine = -1
        else:
            if y > 400 or y < 150:
                actions.engine = -1
            else:
                actions.engine = 1



        # if round(gamestate.tank.direction.get_orientation_angle(), 0) :
        #     actions.turn = 0
        #     actions.shoot = True
        # else:
        #     actions.engine = -1
        #     actions.shoot = False

        ## Figure out what to do!

        return actions

