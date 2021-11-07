import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist


def callback(msg):

    rospy.loginfo(rospy.get_caller_id() + "Twist %s", msg)
    power_val = msg.linear.x
    
    if(msg.angular.z==0):
    
        if(power_val >= 10):
            fc.forward(power_val)
        elif(power_val<=-10):
            fc.backward(power_val)
        else:
            fc.stop()
    else:
        if(msg.angular.z==1):
            fc.turn_left(power_val)
        elif(msg.angular.z==-1):
            fc.turn_right(power_val)
            

def picar_controller():
    rospy.init_node("speed_listener")
    rospy.Subscriber("/cmd_vel",Twist,callback)
    rospy.spin()



if __name__ == '__main__':
    try:
        picar_controller()
    except KeyboardInterrupt:
        print("KeyboardInterrupt, motor stop")
        fc.stop()
    except rospy.ROSInterruptException:
	    fc.stop()
	    pass
    finally:
	    fc.stop()






