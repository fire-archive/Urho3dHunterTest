cmake_minimum_required(VERSION 3.2.3)

include("cmake/HunterGate.cmake")

# If Hunter is cloned this line will not
# be used if fact. See 'testing' section for me info
HunterGate(
    URL "https://github.com/ruslo/hunter/archive/v0.14.12.tar.gz"
    SHA1 "2d444140db0d53393b5490604006bb4f4896a444"
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

if(Win32)
set(CMAKE_MODULE_PATH ${URHO3D_ROOT}/share/CMake/Modules;${CMAKE_MODULE_PATH})
else()
set(CMAKE_MODULE_PATH ${URHO3D_ROOT}/share/Urho3D/CMake/Modules;${CMAKE_MODULE_PATH})
endif()
include(Urho3D-CMake-common)
add_subdirectory(20_HugeObjectCount)

if(Win32)
INSTALL( DIRECTORY "${URHO3D_ROOT}/share/Resources/CoreData" DESTINATION bin )
INSTALL( DIRECTORY "${URHO3D_ROOT}/share/Resources/Data" DESTINATION bin )
else()
INSTALL( DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/CoreData" DESTINATION bin )
INSTALL( DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/Data" DESTINATION bin )
endif()

