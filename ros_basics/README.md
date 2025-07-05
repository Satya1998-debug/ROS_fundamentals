# 🛠️ ros_basics

A ROS 2 package showcasing the **core building blocks** of ROS 2 using `rclpy` (Python).   (using **ROS2 Humble**)

This contains implementation as per the **Official ROS2 Documentation** and **Udemy** online courses on ROS2 (beginner + intermediate).This is still in progress, I update as I learn concurrently!!

---

## 📚 Features

This package demonstrates the following ROS 2 concepts:

| Component           | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| ✅ Publisher         | Publishes a `String` or `Twist` message at a regular interval      |
| ✅ Subscriber        | Listens to a topic and logs received messages                      |
| ✅ Service (Server)  | Implements a service (e.g. add two ints, echo string)              |
| ✅ Service (Client)  | Calls the service and prints the response                          |
| ✅ Action (Server)   | Executes a long-running goal like countdown or Fibonacci           |
| ✅ Action (Client)   | Sends goal requests to the action server                           |
| ✅ Parameters        | Reads and sets node parameters dynamically                         |
| ✅ Custom Interface  | Uses `.msg`, `.srv`, or `.action` files to define custom types     |

---


## 🧱 Package Structure

```
    ros_basics/
    ├── package.xml
    ├── setup.py
    ├── resource/
    ├── ros_basics/
    │   ├── __init__.py
    │   ├── publisher_node.py
    │   ├── subscriber_node.py
    │   ├── server_node.py
    │   ├── client_node.py
    │   ├── action_server.py
    │   ├── action_client.py
    │   ├── parameter_node.py
    ├── msg/
    │   └── CustomMessage.msg
    ├── srv/
    │   └── AddTwoInts.srv
    ├── action/
    │   └── Countdown.action
```

## Run Examples

Publisher:
``` ros2 run ros_basics talker ```

Subscriber:
``` ros2 run ros_basics listener ```

### Server
``` ros2 run ros_basics server ```

### Client
``` ros2 run ros_basics client num1 num2```

### Practice Modules

This also includes many of my python-based modules (clubbed tigether into same ros-package) which I created for testing and practice puprose. This covers all the implementation of the **Activities/Tasks** that were mentioned in the online course on **ROS 2 for Beginners (ROS Jazzy - 2025)** in **Udemy**. 

PS: I persoanlly used ROS2 Humble instead of Jazzy.





