#lib's 
import rospy
from clover import srv
from std_srvs.srv import Trigger
from clover.srv import SetLEDEffect
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from pyzbar import pyzbar
import math

#node + bridge
rospy.init_node('flight')
bridge = CvBridge()
qr_code = ''


#clover func 
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
land = rospy.ServiceProxy('land', Trigger)
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)  # define proxy to ROS-service


#def's place

# navigate function 
def navigate_wait(x=0, y=0, z=1, speed=0.5, frame_id='aruco_map', auto_arm=False, tolerance=0.2):
    navigate(x=x, y=y, z=z, speed=speed, frame_id=frame_id, auto_arm=auto_arm)

    while not rospy.is_shutdown():
        telem = get_telemetry(frame_id='navigate_target')

        if math.sqrt(telem.x ** 2 + telem.y ** 2 + telem.z ** 2) < tolerance:
            rospy.sleep(3)
            break

        rospy.sleep(0.2)


#led
def led(color):
    if color=='red':
        set_effect(r=255, g=0, b=0)
    elif color == 'yellow':
        set_effect(r=0, g=255, b=255)
    elif color == 'blue':
        set_effect(r=0, g=0, b=255)
    elif color == 'white':
        set_effect(r=255, g=255, b=255)
    elif color == 'nan':
        set_effect(r=0, g=0, b=0)



#QR reading function
def qr_read():
    cv_image = bridge.imgmsg_to_cv2(rospy.wait_for_message('main_camera/image_raw', Image), 'bgr8')
    barcodes = pyzbar.decode(cv_image)
    for barcode in barcodes:
        b_data = barcode.data.decode("utf-8")
        print(b_data)
        led(b_data)



# main function
def main():

    #lifoff
    print("start")
    navigate_wait(z=1, speed=1, frame_id='body', auto_arm=True)

    #point + qr_read
    navigate_wait(x=3)    
    qr_read()
    rospy.sleep(2)

    #landing
    land()

if __name__ == "__main__":
    main()
