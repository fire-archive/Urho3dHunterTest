from conans import ConanFile, CMake
import os


channel = os.getenv("CONAN_CHANNEL", "testing")
username = os.getenv("CONAN_USERNAME", "demo")


class Urho3dTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "Urho3D/v1.7-pre0@%s/%s" % (username, channel)
    generators = "cmake_multi"
    default_options = "shared=True"
    options = {"shared": [True, False]}

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
