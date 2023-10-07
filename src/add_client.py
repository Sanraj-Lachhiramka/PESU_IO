#!/usr/bin/env python3

import sys #imports the sys module, which provides access to various system-specific parameters and functions
import rospy
from Spot_Robot_description.srv import AddTwoInts #import specific service type from package
from Spot_Robot_description.srv import AddTwoIntsRequest
from Spot_Robot_description.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints') #rospy.wait_for_service('add_two_ints') waits for the ROS service named 'add_two_ints' to become available before proceeding
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)#Creates a service proxy named add_two_ints for the 'add_two_ints' service using rospy.ServiceProxy. This allows you to call the service as if it were a regular function.
        resp1 = add_two_ints(x, y) #calls the service with the arguments x and y and stores the response in resp1
        return resp1.sum
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3: #checks if there are exactly three command-line arguments when running the script
        x = int(sys.argv[1])#converts first  argument to integer
        y = int(sys.argv[2])##converts second  argument to integer
    
    else:#if there are not exactly three command-line arguments, it prints a usage message indicating how the script should be used (with x and y arguments) and exits with a status code of 1
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting %s+%s"%(x, y))#If there are three command-line arguments, it prints a message indicating that it's requesting the addition of x and y.
    
    s = add_two_ints_client(x, y)##It then calls the add_two_ints_client function with x and y and stores the result in s
    print ("%s + %s = %s"%(x, y, s))
