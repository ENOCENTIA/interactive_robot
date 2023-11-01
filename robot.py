

def robot_name():
    """asks the user to name their robot
    """
    toy_name= input("What do you want to name your robot? " )

    print (f"{toy_name}: Hello kiddo!")
    return toy_name


def get_input(toy_name):
    """ask the user what to do next?
    """
    command = input(f"{toy_name}: What must I do next? ")
    return command
    

def command_help():
    """ function gets user input for commands
    """  
    infomation = """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - moves the robot forward
BACK - moves the robot backward
RIGHT - moves the robot to the right
LEFT - moves the robot to the left
SPRINT - moves the robot faster and at a longer distance
    
"""
    return infomation


def command_choice(command, toy_name):
    """function checks if command is valid
    """
    commands_list = ['OFF','HELP','FORWARD','BACK','RIGHT','LEFT','SPRINT']

    if ((command.split()[0]).upper()) not in commands_list:
        print(f"{toy_name}: Sorry, I did not understand '{command }'.")
        valid_command = False
    else:
        valid_command = True
    return valid_command


def forward_direction(toy_name,axis,value, steps):
    """makes the robot move forward
    """
    old_x,old_y = axis
    x,y = direction(old_x,old_y, steps,value)
    analys_x, x = area_limit_x(x,old_x)
    analys_y, y = area_limit_y(y, old_y)
    if (analys_x is True) and (analys_y is True):
        print(f" > {toy_name} moved forward by {steps} steps.")
    else:
        print(f"{toy_name}: Sorry, I cannot go outside my safe zone.")
    axis = (x, y)
    return axis


def backward_direction(toy_name, value, axis,steps):
    """makes the robot move backward
    """
    old_x,old_y = axis
    x, y = direction(old_x,old_y, steps,value)
    analys_x, x = area_limit_x(x,steps)
    analys_y, y = area_limit_y(y, steps)
    if (analys_x is True) and (analys_y is True):
        print(f" > {toy_name} moved back by {steps*(-1)} steps.")
    else:
        print(f"{toy_name}: Sorry, I cannot go outside my safe zone.")
    new_axis = (x,y)
    return new_axis


def turn_right(toy_name, value):
    """makes robot turn right
    """
    print(f" > {toy_name} turned right.")
    value -= 90
    value = value % 360 
    return value


def turn_left(toy_name, value):
    """makes robot turn left
    """
    print(f" > {toy_name} turned left.")
    value += 90
    value = value % 360 
    return value


def direction(x, y, steps, value):
    """direction takes 4 parameters and checks which steps to move its x,y\ 
       axis and values.
    """
    steps = int(steps)
    if value == 90:
        y += steps
    elif value == 180:
        x -= steps
    elif value == 270:
        y -= steps
    elif value == 0:
        x += steps
    return (x, y)

def area_limit_y(y,old_y):
    """area limit for y axis it checks the input if it exceed the limit\
     then return true or false
     """
    if -200 <= y <= 200:
        return True, y
    else:
        return False, (old_y)

def area_limit_x(x,old_x):
    """area limit for x value and it return true or false
    """
    if -100 <= x <= 100:
        return True, x
    else:
        return False ,(old_x)


def sprint_steps(toy_name, value, axis, steps):
    """function makes robot moves faster and further
    """
    if steps == 1:
        return forward_direction(toy_name,axis,value, steps)
    else :
        axis = forward_direction(toy_name,axis,value, steps)
        return sprint_steps(toy_name, value, axis, steps-1)

def instruct(toy_name,command,value, axis):
    """instruct function is where all there is  information for  command_help 
    """
    if command.upper() == "OFF":
        print(f"{toy_name}: Shutting down..")
        return  (True, axis, value)
    
    elif command.upper() == "HELP":
        print(command_help())
        return (False, axis, value)
    
    elif command.split()[0].upper() == "FORWARD":
        steps = int(command.split()[1])
        axis  = forward_direction(toy_name,axis,value,steps)

    elif command.split()[0].upper() == "BACK":
        steps = int(command.split()[1])*-1
        axis= backward_direction(toy_name,value, axis,steps)

    elif command.upper() == "RIGHT":
        value = turn_right(toy_name,value)

    elif command.upper() == "LEFT":
        value = turn_left(toy_name,value)

    elif command.split()[0].upper() == "SPRINT":
        steps = int(command.split()[1])
        axis = sprint_steps(toy_name, value, axis, steps)
    
    x, y = axis
    print(f" > {toy_name} now at position ({x},{y}).") 
    return (False, axis, value)


def robot_start():
    """This is the entry function"""
    
    toy_name = robot_name()
    execute = False
    axis = (0, 0)
    value = 90
    steps = 0
    while execute is False:
        command = get_input(toy_name)
        valid_command =command_choice(command, toy_name)
        if command[0] == "HELP" or valid_command is False:
            continue
        execute, axis, value = instruct(toy_name, command, value, axis)

       
if __name__ == "__main__":
    
    robot_start()
