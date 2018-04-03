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
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from std_msgs.msg import String
import requests
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

InternetFail = 0
urlTest = urlTest='http://192.168.1.101'
timeoutTest=1
GPIO.setup(26, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
Index = GPIO.PWM(17,500)
Index.start(0)
time.sleep(3)

def talker():
    global InternetFail, urlTest, timeoutTest
    pub = rospy.Publisher('url_test', String, queue_size=10)
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
            if(InternetFail>=2):
                print("-------------------------------")
                print("No internet 2 times. \n")
                print("-------------------------------")
                noConnection()
        rate.sleep()

def noConnection():
    print "PAILA"
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
