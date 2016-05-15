cmake_minimum_required(VERSION 3.2.3)

include("cmake/HunterGate.cmake")

# If Hunter is cloned this line will not
# be used if fact. See 'testing' section for me info
HunterGate(
    URL "https://github.com/ruslo/hunter/archive/v0.14.12.tar.gz"
    SHA1 "2d444140db0d53393b5490604006bb4f4896a444"
    LOCAL
)

if (COMMAND cmake_policy)
    cmake_policy (SET CMP0003 NEW)
    if (CMAKE_VERSION VERSION_GREATER 2.8.12 OR CMAKE_VERSION VERSION_EQUAL 2.8.12)
        # INTERFACE_LINK_LIBRARIES defines the link interface
        cmake_policy (SET CMP0022 NEW)
    endif ()
    if (CMAKE_VERSION VERSION_GREATER 3.0.0 OR CMAKE_VERSION VERSION_EQUAL 3.0.0)
        # Disallow use of the LOCATION target property - so we set to OLD as we still need it
        cmake_policy (SET CMP0026 OLD)
        # MACOSX_RPATH is enabled by default
        cmake_policy (SET CMP0042 NEW)
    endif ()
endif ()

project(UrhoHunterTest)
hunter_add_package(Urho3D)

#file(READ "${URHO3D_LICENSE}" urho3d_license_content)
#set(project_license ${CMAKE_BINARY_DIR}/LICENSE.md)
#file(
#  WRITE
#  "${project_license}"
#  "## Urho3D\n\n"
#  "${urho3d_license_content}"
#)
#install(FILES ${project_license} DESTINATION .)

message("Project license: ${project_license}")

if(WIN32)
  set(CMAKE_MODULE_PATH ${URHO3D_ROOT}/share/CMake/Modules;${CMAKE_MODULE_PATH})
else()
  set(CMAKE_MODULE_PATH ${URHO3D_ROOT}/share/Urho3D/CMake/Modules;${CMAKE_MODULE_PATH})
endif()
include(Urho3D-CMake-common)

if(${URHO3D_LIB_TYPE} STREQUAL SHARED AND NOT WIN32)
 set(CMAKE_INSTALL_RPATH "../lib/Urho3D")
 install(DIRECTORY "${URHO3D_ROOT}/lib/Urho3D" DESTINATION lib)
endif()

if(WIN32)
  install(DIRECTORY "${URHO3D_ROOT}/share/Resources/CoreData" DESTINATION bin)
  install(DIRECTORY "${URHO3D_ROOT}/share/Resources/Data" DESTINATION bin)
else()
  install(DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/CoreData" DESTINATION bin)
  install(DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/Data" DESTINATION bin)
endif()

add_subdirectory(20_HugeObjectCount)

