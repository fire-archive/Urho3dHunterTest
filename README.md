# Urho3DHunterTest

## Setup
* Get the latest cmake `cinst cmake` (From chocolatey)
* Get msvc 2015 update 2 (Current version of MSVC c++ compiler)
* Set HUNTER_ROOT environment variable to the location of `https://github.com/fire/hunter/tree/Urho3D`.
* Generate project: `cmake -H. -B_builds -DCMAKE_BUILD_TYPE=RelWithDebInfo`
* Run build: `cmake --build _builds --config RelWithDebInfo`
* Run test: `cd _builds && ctest -C RelWithDebInfo -VV`

sudo apt install -y mingw-w64
-DCMAKE_C_COMPILER=/usr/binx/86_64-w64-mingw32-gcc -DCMAKE_CXX_COMPILER=/usr/bin/x86_64-w64-mingw32-g++