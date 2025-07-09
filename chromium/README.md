# Alien BOB´s Chromium slackbuild adopted for Slackware ARM (SARPI 15.0) and Slackware AArch64 (SARPI Current)
Adopted Alien BOB´s Chromium Slackbuild for Slackware ARM SARPI-15.0 and Slackware AArch64 SAPRI-Current so one can compile chromium/chromium-ungoogled for your Slackware ARM and AArch64 Rasberry Pi.

This is built on SARPI 15.0 and SARPI Current Rasberry Pi 4.
I have not tried to build this on any other device.

Might also want to download/copy the patches from the patch directory to Alien BOB´s patch directory of the chromium slackbuild directory.

# What i have done and what the slackbuild/diff/patch does is:
* Repatched clang.toolchains.arm_i586.triple for ARM.
* Fixed chromium_conf for ARM
* Fixed target triple for ARM.
* Fixed ARM sysroot path/link for libsqlite3.so, glibconfig.h,
dbus-arch-deps.h, graphene-config.h and arm-linux-gnueabihf.conf.
* Fixed link for debians arm-linux-gnueabihf-readelf to slackwares readelf
* Fixed compiling google's internal llvm/clang for ARM and aarch64.
* Also made it possible to use eithers systems llvm/clang version or my slackbuild llvm/clang version instead of chromiums llvm/clang build.
* Patched chromium for arm and aarch64 to support Widevine. (Using my patched glibc will also make Widevine 4.10.2252.x and latest 4.10.2557.x working on ARM and aarch64)

# Dependencies needed to build:
* ninja (Is avalible throught slack package)
* nodejs >= 18.7.0 (For ARM this is avalible at [Alien's SlackBuilds](http://www.slackware.com/~alien/slackbuilds/nodejs/build/))  
  Note: (For Slackware aarch64 Current it is avalible throught slack package)
* gcc >= 8 for bootstrapping gn (Is avalible throught slack package)
* nasm >= 2.14 (yasm no longer being used) (Is avalible throught slack package)
* cmake >= 3.13.4 (Is avalible throught slack package)
* python3 >= 3.7, python3-setuptools (Is avalible throught slack package)
* java runtime (Slackware ARM package Is avalible [here](https://github.com/mostman/Slackbuilds/releases/download/21.2/jdk-8u381-arm-1_SLse.tgz) and AArch64 package [here](https://github.com/mostman/Slackbuilds/releases/download/21.2/jdk-8u451-aarch64-1_SBo.tgz))
* Internet access (for downloading toolchain bins)

# Optional dependencies to build:
* llvm >= 16.0.x (Is avalible throught slack package or my [llvm](https://github.com/mostman/Slackbuilds/tree/main/llvm) buildscript or prebuilt [llvm slackware x86_64 and ARM](https://github.com/mostman/Slackbuilds/releases/tag/16.0.6) package).
To speed up the build and not having to build Chromiums internal llvm/clang everytime, to get around this issue you can install my llvm/clang package for Slackware Arm 15.0.
By doing this you save about a day comping time on a RPI4.

# Patch AlienBob´s [chromium.Slackbuild](http://www.slackware.com/~alien/slackbuilds/chromium/build/)
* Download all aliens chromium slackbuild as described by him self.
* Download my additional patches in to the patch directory.
* Download the chromium.arm.SlackBuild.diff file to build directory and patch the build script "patch -p0 < chromium.arm.SlackBuild.diff".

# Replace the buildscript with AlienBob´s [chromium.Slackbuild](http://www.slackware.com/~alien/slackbuilds/chromium/build/)
* Download all aliens chromium slackbuild as described by him self.
* Download my additional patches in to the patch directory.
* Rename AlienBob´s chromium.Slackbuild to chromium.Slackbuild.alien
* Download the chromium.Slackbuild file to build directory.

Some last notes.
Make sure you have at least 15-20 GB free space on your memory card, drive or USBstick (Or where ever you store the source code and tmp folder) and at least 1 GB swap space.
Recommended to set "gpu_mem" to 32 or 64 and then run system in runlevel 3 when compiling.
I´am sorry to say, that estimated compiling time will be at least thirty six hours if not even more.

