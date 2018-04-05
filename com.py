#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
import rospy
from std_msgs.msg import String
import requests
import time, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

InternetFail = 0
urlTest='http://www.google.com'
#urlTest=http://25.21.73.120
#utlTest='http://'+os.environ(ROS_PILOT)
timeoutTest=2
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
time.sleep(3)

def talker():
    global InternetFail, urlTest, timeoutTest
    pub = rospy.Publisher('url_Test', String, queue_size=10)
    rospy.init_node('communications', anonymous=True)
    rospy.loginfo("Testing URL")
    rate = rospy.Rate(5) # 10hz
    while not rospy.is_shutdown():
        try:
            r = requests.get(urlTest, timeout=timeoutTest)
            Internet_test = "Internet Ok %s" % rospy.get_time()
            rospy.loginfo(Internet_test)
            pub.publish(Internet_test)
            InternetFail=0
            OK()
        except requests.ConnectionError:
            Internet_test = "Internet FAIL"
            rospy.loginfo(Internet_test)
            pub.publish(Internet_test)
            InternetFail=InternetFail+1
            if(InternetFail>=1):
                print("-------------------------------")
                print("No internet 2 times. \n")
                print("-------------------------------")
                noConnection()
        rate.sleep()

def noConnection():
    print "NO NONNECTION"
    GPIO.output(21, 1)  # turn on
    GPIO.output(20, 0)  # turn off
    time.sleep(0.5)
    GPIO.output(20, 1)  # turn on
    GPIO.output(21, 0)  # turn off
    time.sleep(0.5)
    GPIO.output(21, 1)  # turn on
    GPIO.output(20, 0)  # turn on

def OK():
    print "bien"

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
