cmake_minimum_required(VERSION 3.17)
project(kmeans C)

set(CMAKE_C_STANDARD 90)
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -ansi -Wall -Wextra -Werror -pedantic-errors")
add_executable(kmeans kmeans.c eigengap_heuristic.c)

set(Python3_EXECUTABLE "C:/Users/eyal/AppData/Local/Programs/Python/Python37-32")

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)

include_directories(${Python3_INCLUDE_DIRS})

include_directories(${Python3_LIBRARIES})

target_link_libraries(kmeans ${PYTHON_LIBRARIES})