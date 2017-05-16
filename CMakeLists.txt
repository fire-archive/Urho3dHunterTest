cmake_minimum_required(VERSION 3.2.3)
include("cmake/HunterGate.cmake")
# If Hunter is cloned this line will not
# be used if fact. See 'testing' section for me info
HunterGate(
    URL "https://github.com/fire/hunter/archive/v2017-05-16T16.zip"
    SHA1 "3c3166516d4c05d252222413c2bb15ab27e3e32b"
)
project(UrhoHunterTest)
hunter_add_package(Urho3D)
file(READ "${URHO3D_ROOT}/licenses/Urho3D/LICENSE" urho3d_license_content)
file(READ "${CMAKE_SOURCE_DIR}/LICENSE.md" project_license)
set(output_license ${CMAKE_CURRENT_BINARY_DIR}/LICENSE.md)
file(
  WRITE
  "${output_license}"
  "${project_license}\n\n"
  "${urho3d_license_content}"
)
install(FILES ${output_license} DESTINATION .)
message("Project license: ${output_license}")
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
  install(DIRECTORY "${URHO3D_ROOT}/share/Resources/Autoload" DESTINATION share/Resources)
  install(DIRECTORY "${URHO3D_ROOT}/share/Resources/CoreData" DESTINATION share/Resources)
  install(DIRECTORY "${URHO3D_ROOT}/share/Resources/Data" DESTINATION share/Resources)
else()
  install(DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/Autoload" DESTINATION share/Urho3D/Resources)
  install(DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/CoreData" DESTINATION share/Urho3D/Resources)
  install(DIRECTORY "${URHO3D_ROOT}/share/Urho3D/Resources/Data" DESTINATION share/Urho3D/Resources)
endif()
if(WIN32)
install(FILES 42_PBRMATERIALS/.itch.toml DESTINATION .)
install(FILES ${URHO3D_ROOT}/bin/Urho3DPlayer.exe DESTINATION bin)
install(FILES ${URHO3D_ROOT}/bin/Editor.bat DESTINATION bin)
else()
endif()

add_subdirectory(42_PBRMaterials)
