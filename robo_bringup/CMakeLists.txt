cmake_minimum_required(VERSION 3.8)
project(robo_bringup)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

# everything we will write inside the launch directory will be installed
# any new folder inside bringup need ro be added here with space separated names with launch
install(DIRECTORY 
  launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
