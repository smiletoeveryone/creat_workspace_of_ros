#!/usr/bin/env python

import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    rospy.init_node('talker', anonymous=True) #creat and initial a note
    pub = rospy.Publisher('chat', String, queue_size=10) #creat a publisher 
    rate = rospy.Rate(10) #publish rate

    while not rospy.is_shutdown():
        hello = 'hello world! %s' % rospy.get_time() #string and get publish  time
        pub.publish(hello)
        rospy.loginfo(hello) #print in the screen
        rate.sleep() #blink every 1/10s
