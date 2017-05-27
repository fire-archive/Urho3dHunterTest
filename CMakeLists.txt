cmake_minimum_required(VERSION 3.2.3)
project(UrhoHunterTest)
# Set CMake modules search path
set (CMAKE_MODULE_PATH $ENV{URHO3D_HOME}/Share/CMake/Modules)
# Include Urho3D Cmake common module
include (UrhoCommon)
add_subdirectory (42_PBRMaterials)