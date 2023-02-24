# first fligth in Gazebo - rectangle
import rospy
from clover import srv
from std_srvs.srv import Trigger
import math

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)

def navigate_wait(x=0, y=0, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')
        telem_auto = get_telemetry()

        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:      # теорема пифагора для пространства 
            rospy.sleep(3)
            print("получено | X = {} | Y = {}".format(telem_auto.x, telem_auto.y))
            break

        rospy.sleep(0.2)

def main():
    print("взлёт")
    navigate_wait(z=1.5, speed=1, frame_id='body', auto_arm=True)
    navigate_wait(y=2, z=1.5, frame_id='aruco_map')
    navigate_wait(x=2, y=2, z=1.5, frame_id='aruco_map')
    navigate_wait(x=2, z=1.5, frame_id='aruco_map')
    navigate_wait(x=0,y=0, z=1.5, frame_id='aruco_map')
    land()

if __name__ == "__main__":
    main()
