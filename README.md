![](https://github.com/smiletoeveryone/create_workspace_of_ros/blob/master/ros_logo.png)

# create_workspace_of_ros

# please run your terminal in advance

***create_workspace
1. mkdir -p ~/catkin_ws/src
2. cd catkin_ws
3. catkin_make
4. echo 'source /home/pi/catkin_ws/devel/setup.bash' >> ~ /.bashrc
5. source ~/.bashrc
***creat_package
1. cd src
2. catkin_create_pkg beginner_tutorials std_msgs rospy roscpp // include programming languages
3. cd ..
4. catkin_make
5. echo 'source ~/catkin_ws/devel/setup.sh' >> ~/.bashrc
5. . ~/catkin_ws/devel/setup.bash or source ~/catkin_ws/devel/setup.bash
***programming for a publish node
1. cd /home/pi/catkin_ws/src/beginner_tutorials/src // in the file manager
2. code for a publish_node
3. cd /home/pi/catkin_ws/src/beginner_tutorials/src // in the terminal
4. chmod +x helloworld.py
5. make sure 'roscore' you have ran
6. pi@raspberrypi:~ $ rosrun beginner_tutorials helloworld.py
***useful commands
rostopic list
rostopic info /chat
rostopic echo /chat
***programming for a publish node
1. cd /home/pi/catkin_ws/src/beginner_tutorials/src // in the file manager
2. code for a subsrib_node
3. cd /home/pi/catkin_ws/src/beginner_tutorials/src // in the terminal
4. chmod +x helloworld_listener.py
5. make sure 'roscore' you have ran
6. pi@raspberrypi:~ $ rosrun beginner_tutorials helloworld_listener.py
***visualize
rqt_graph
