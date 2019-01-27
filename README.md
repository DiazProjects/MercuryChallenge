# Mercury Challenge

**Mercury Challenge** is a repository with the programing elements based on Robotic Operative System ROS and python to control a 4-wheel reover designed to compete in the LatinAmerican [MercuryChallenge](https://mercurylatino.weebly.com/uploads/4/9/3/7/49370873/reglamento_v6_24012018.pdf).

**Hardware and associate repositories:**
* Ion Motion Roboclaw, Is Dual DC motor driver: [Lib](http://www.ionmc.com/downloads)
* Pololu USB servo Control [POL-1353](https://www.pololu.com/product/1353)
* Hokuyo URG-04LX, [driver](http://wiki.ros.org/hokuyo_node)
* Raspberry PI 3+

## Getting Started

The following steps describe how to install in the raspberry pi the Mercury-Control.
* Install ROS: http://wiki.ros.org/kinetic/Installation/Ubuntu
* Install Joyd: http://wiki.ros.org/joy/Tutorials/ConfiguringALinuxJoystick
* Install Git: sudo apt-get install git-core
* Install GPIO: sudo apt-get install python-rpi.gpio [25,28, 29]
* Install Requests: pip install requests
* Install [Hamachi](https://medium.com/@KyleARector/logmein-hamachi-on-raspberry-pi-ad2ba3619f3a)
* Install URG_node: sudo apt-get install ros-kinetic-urg-node
* rosparam set hokuyo_node/calibrate_time false
* rosparam set hokuyo_node/port /dev/ttyACM0
* rosrun hokuyo_node hokuyo_node
* remove sudo --pass:
* sudo visudo
* root    ALL=(ALL:ALL) ALL
* %admin ALL=(ALL) NOPASSWD: ALL
* %sudo   ALL=(ALL:ALL) NOPASSWD: ALL
* where "admin" is the usser name

## USB Rules
* udevadm info -a -n /dev/ttyUSB1 | grep
* sudo nano /etc/udev/rules.d/99-robot.rules
* SUBSYSTEM=="tty", ATTRS{idVendor}=="03eb", ATTRS{idProduct}=="2404",  SYMLINK+="tty_roboclaw"
* SUBSYSTEM=="tty", ATTRS{idVendor}=="0424", ATTRS{idProduct}=="9514",  SYMLINK+="tty_pololu"
* sudo udevadm trigger
* sudo chmod 666 /dev/tty_roboclaw
* sudo chmod 666 /dev/tty_pololu

## Bash Functions
### On RPi
* export ROS_IP=<Rpi ip>
* export ROS_MASTER_URI=http://<Rpi ip>:11311
* sudo chmod 666 /dev/tty_roboclaw
* sudo chmod 666 /dev/tty_pololu
* roscore &
* python com.py &
* python control.py &

### On Remote
* export ROS_IP=<remote ip>
* export ROS_MASTER_URI=http://<Rpi ip>:11311
* rosparam set joy_node/dev "/dev/input/js1"
* rosrun joy joy_node &


## Autors

* Harold F. Murcia   - (www.haroldmurcia.com)
* Nickson Garcia     - (2420132006@estudiantesunibague.edu.co)
* Juan D. Valenciano - (jvalenciano@unal.edu.co)

## License

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org>
