from conans import ConanFile, CMake, tools
import os

class Urho3dConan(ConanFile):
    name = "Urho3D"
    version = "v1.7-pre0"
    license = "MIT"
    url = "https://github.com/urho3d/Urho3D.git"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone %s Urho3D" % (self.url))
        # This small hack might be useful to guarantee proper /MT /MD linkage in MSVC
        # if the packaged project doesn't have variables to set it properly
        tools.replace_in_file("Urho3D/CMakeLists.txt", "project (Urho3D)", '''project (Urho3D)
        include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
        conan_basic_setup()
        unset(CMAKE_ARCHIVE_OUTPUT_DIRECTORY)
        unset(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_RELEASE)
        unset(CMAKE_ARCHIVE_OUTPUT_DIRECTORY_DEBUG)''')

    def build(self):
        cmake = CMake(self)
        shared = "-DURHO3D_LIB_TYPE=SHARED " if self.options.shared else ""
        install = "-DCMAKE_INSTALL_PREFIX=%s " % self.package_folder
        # TODO Break apart options
        options = "-DURHO3D_C++11=ON \
        -DURHO3D_ANGELSCRIPT=OFF \
        -DASSIMP_BUILD_3DS_IMPORTER=OFF \
        -DASSIMP_BUILD_3D_IMPORTER=OFF \
        -DASSIMP_BUILD_AC_IMPORTER=OFF \
        -DASSIMP_BUILD_ASE_IMPORTER=OFF \
        -DASSIMP_BUILD_ASSBIN_IMPORTER=OFF \
        -DASSIMP_BUILD_ASSXML_IMPORTER=OFF \
        -DASSIMP_BUILD_B3D_IMPORTER=OFF \
        -DASSIMP_BUILD_BLEND_IMPORTER=OFF \
        -DASSIMP_BUILD_BVH_IMPORTER=OFF \
        -DASSIMP_BUILD_COB_IMPORTER=OFF \
        -DASSIMP_BUILD_COLLADA_IMPORTER=ON \
        -DASSIMP_BUILD_CSM_IMPORTER=OFF \
        -DASSIMP_BUILD_DXF_IMPORTER=OFF \
        -DASSIMP_BUILD_FBX_IMPORTER=ON \
        -DASSIMP_BUILD_HMP_IMPORTER=OFF \
        -DASSIMP_BUILD_IFC_IMPORTER=OFF \
        -DASSIMP_BUILD_IRR_IMPORTER=OFF \
        -DASSIMP_BUILD_LWO_IMPORTER=OFF \
        -DASSIMP_BUILD_LWS_IMPORTER=OFF \
        -DASSIMP_BUILD_MD2_IMPORTER=OFF \
        -DASSIMP_BUILD_MD3_IMPORTER=OFF \
        -DASSIMP_BUILD_MD5_IMPORTER=OFF \
        -DASSIMP_BUILD_MDC_IMPORTER=OFF \
        -DASSIMP_BUILD_MDL_IMPORTER=OFF \
        -DASSIMP_BUILD_MS3D_IMPORTER=OFF \
        -DASSIMP_BUILD_NDO_IMPORTER=OFF \
        -DASSIMP_BUILD_NFF_IMPORTER=OFF \
        -DASSIMP_BUILD_OBJ_IMPORTER=OFF \
        -DASSIMP_BUILD_OFF_IMPORTER=OFF \
        -DASSIMP_BUILD_OGRE_IMPORTER=OFF \
        -DASSIMP_BUILD_OPENGEX_IMPORTER=OFF \
        -DASSIMP_BUILD_PLY_IMPORTER=OFF \
        -DASSIMP_BUILD_Q3BSP_IMPORTER=OFF \
        -DASSIMP_BUILD_Q3D_IMPORTER=OFF \
        -DASSIMP_BUILD_RAW_IMPORTER=OFF \
        -DASSIMP_BUILD_SMD_IMPORTER=OFF \
        -DASSIMP_BUILD_STL_IMPORTER=OFF \
        -DASSIMP_BUILD_TERRAGEN_IMPORTER=OFF \
        -D-DASSIMP_BUILD_XGL_IMPORTER=OFF \
        -DASSIMP_BUILD_X_IMPORTER=OFF \
        -DURHO3D_PCH=OFF \
        -DURHO3D_LUA=OFF \
        -DURHO3D_OPENGL=ON"

        self.run('cmake Urho3D %s %s %s %s' % (cmake.command_line, shared, install, options))
        self.run("cmake --build . --target install %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="Urho3D")
#        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Urho3D"]