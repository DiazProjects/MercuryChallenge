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
from sensor_msgs.msg import Joy
import time
import maestro

servo = maestro.Controller()
servo.setRange(0,0,9000) # Motor Base
servo.setRange(1,0,9000) # Motor Yaw
servo.setRange(2,0,9000) # Joint 3
servo.setRange(3,0,9000) # Joint 2
servo.setRange(4,0,9000) # Gripper
servo.setRange(5,0,9000)
servo.setRange(6,0,9000)
servo.setRange(7,0,9000)
servo.setRange(8,0,9000)
servo.setAccel(0,4)
servo.setAccel(1,4)
 
def callback(data):
    buttons = data.buttons;
    axes = data.axes
    move(buttons, axes)
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data)
def move(buttons, axes):
    print "Moving"
    if buttons[7]==1 and axes[7]==1:  #Start + up
	home()
    elif buttons[7]==1 and axes[7]==-1:  #Start + down
	tunnel()
    elif buttons[6]==1:  #Back
	free()
def home():
    print "home"
    servo.setTarget(0,3000)
    time.sleep(0.5)
    servo.setTarget(0,0)
    servo.setTarget(1,9000)
    time.sleep(0.5)
    servo.setTarget(1,0)
    servo.setTarget(3,3000)
    time.sleep(0.5)
    servo.setTarget(3,0)
    servo.setTarget(2,4500)
    time.sleep(0.5)
    servo.setTarget(2,0)
    servo.setTarget(4,5500)
def tunnel():
    servo.setTarget(0,3000)
    time.sleep(0.5)
    servo.setTarget(0,0)
    servo.setTarget(1,6000)
    #servo.setTarget(3,4000)
    #servo.setTarget(2,4500)
    #servo.setTarget(4,5500)
def free():
    servo.setTarget(0,0)
    servo.setTarget(1,0)
    servo.setTarget(2,0)
    servo.setTarget(3,0)
    servo.setTarget(4,0)
def ARM():
    rospy.init_node('rover_arm', anonymous=True)
    rospy.Subscriber("/joy", Joy, callback)
    rospy.spin()



if __name__ == '__main__':
    try:
        ARM()
    except rospy.ROSInterruptException:
        pass
