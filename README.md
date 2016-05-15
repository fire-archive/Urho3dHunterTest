# Urho3DHunterTest

## Setup
* Set HUNTER_ROOT environment variable to an empty folder location
* Generate project: `cmake -H. -B_builds -DCMAKE_BUILD_TYPE=RelWithDebInfo`
* Run build: `cmake --build _builds --config RelWithDebInfo`
* Run test: `cd _builds && ctest -C RelWithDebInfo -VV`
