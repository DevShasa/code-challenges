import math
"""
You’re trying to build an IoT mesh network. Signals can only travel the maximum of 5 units. 
You’re given coordinates for the switch, the light, and the mesh hubs (which capture and forward 
signals). Return true if the switch can successfully toggle the light.
Example:
let network = { switch: [0,1], hub: [[2,1], [2,5]], light: [1,6] }
$ canToggle(network)
$ true
"""
network = {'switch': [0,1], 'hub': [[2,1], [2,5]], 'light': [1,6]}

def getDistance(p1, p2):
    '''
    Finds the distance between two points
    Uses the distance formula
    '''
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) *(p1[1] - p2[1]) )

def canToggle(network):
    
    r = 5
    p1 = network['switch']
    p2 = network['light']

    # Check if the switch can toggle the network 
    if getDistance(p1, p2) <= r:
        # The switch is within range of the network so toggle away
        return True
    else:
        # The switch is not in range of the network, so we check the hubs 
        if len(network['hub']) > 0: # Only perform when there are hubs
            for i in range(len(network['hub'])):
                # Check if hub is withing distance of switch 
                # If so then make the hub the new switch
                p1 = network["switch"]
                p2 = network["hub"][i]
                if getDistance(p1, p2) <= r:
                    # Substitute the switch for hub[i]
                    new_network = {'switch': network["hub"][i], 'hub': network['hub'], 'light': network['light']}
                    new_network["hub"].pop(i) # Remove the hub after rebuilding the network

                    # Check if the new switch can toggle the light
                    return canToggle(new_network)

                # The switch is not within range of the hub
                return False
        else:
            return False

print(canToggle(network))