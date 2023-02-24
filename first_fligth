# first fligth in Gazebo - rectangle
import rospy
from clover import srv
from std_srvs.srv import Trigger
import math

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

navigate(x=0, y=0, z=1.5, speed=0.5, frame_id='body', auto_arm=True)
land()
