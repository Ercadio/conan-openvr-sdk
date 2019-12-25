from conans import ConanFile, CMake, tools

class OpenVRSDKConan(ConanFile):
    name = "openvr-sdk"
    version = "1.8.19"
    license = "Apache 2.0"
    author = "Vincent-Olivier Roch <vroch@edu.uwaterloo.ca>"
    url = "https://github.com/Ercadio/conan-openvr"
    description = "Valve's OpenVR SDK"
    topics = ("vr", "valve", "steam")
    settings = "os", "build_type", "arch_build"
    generators = "cmake"

    def source(self):
        self.run(f'git clone https://github.com/ValveSoftware/openvr.git')
        self.run('cd openvr && git checkout 176b58f6ccaaae3e9d14efaf612c50b72ec5da76')

    def package(self):
        os_map = {
            'Windows': 'win',
            'Linux': 'linux',
            'Macos': 'osx',
        }
        arch_map = {
            'x86': '32',
            'x86_64': '64',
        }
        category = f"{os_map[str(self.settings.os)]}{arch_map[str(self.settings.arch_build)]}"
        self.copy("LICENSE", dst=".", src='openvr')
        self.copy("*.h", dst="include", src="openvr/headers")
        self.copy("*", dst="bin", src=f"openvr/bin/{category}/")
        self.copy("*", dst='lib', src=f"openvr/lib/{category}/")

    def package_info(self):
        self.cpp_info.libs = ["openvr_api"]
