#!/usr/bin/env python

from Spot_Robot_description.srv import AddTwoInts #import message types and services from the Spot_Robot_description package. 
from Spot_Robot_description.srv import AddTwoIntsRequest
from Spot_Robot_description.srv import AddTwoIntsResponse

import rospy

#handle_add_two_ints(req) is the callback function that gets called when a client makes a request to the 'add_two_ints' service
#It takes a single argument req, which is an instance of the AddTwoIntsRequest message type
#Inside the function, it prints a message indicating the two integers being added and their sum
#returns an instance of the AddTwoIntsResponse message type, containing the result of the addition
def handle_add_two_ints(req):
    print ("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')#Initialize a ROS node named 'add_two_ints_server'
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    #reates a ROS service named 'add_two_ints' of type AddTwoInts and associates it with the handle_add_two_ints callback function. 
    #This means that when a client requests the 'add_two_ints' service, the handle_add_two_ints function will be called to handle the request.

    
    print ("Ready to add two ints.")
    rospy.spin()#keeps the ROS node running and processing incoming service requests
    
if __name__ == "__main__":
    add_two_ints_server()
