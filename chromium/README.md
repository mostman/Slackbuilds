# Alien BOB´s Chromium slackbuild adopted for Slackware ARM (SARPI Current)
Adopted Alien BOB´s Chromium Slackbuild for Slackware ARM SARPI-Current.
so one can compile chromium for your Slackware ARM Rasberry Pi.

This is only built on SARPI Current Rasberry Pi 4.
I have not tried to build this on any other device nore architecture other than ARM.

Might also want to download/copy the patches from the patch directory to Alien BOB´s patch directory of the chromium slackbuild directory.

# What i have done and what the slackbuild/diff/patch does is:
* Added lates patchset "93.0.4577.8"
* Repatched clang.toolchains.arm_i586.triple for ARM.
* Fixed chromium_conf for ARM
* Fixed target triple for ARM.
* Fixed ARM sysroot path/link for libsqlite3.so, glibconfig.h,
dbus-arch-deps.h, graphene-config.h and arm-linux-gnueabihf.conf.
* Fixed link for debians arm-linux-gnueabihf-readelf to slackwares readelf
* Fixed compiling google's internal llvm/clang for ARM.
* Also made it possible to use eithers systems llvm/clang version or my slackbuild llvm/clang version instead of chromiums llvm/clang build.
* Patched chromium for arm to support Widevine. (Using my patched glibc will also make Widevine 4.10.2252.0 working on ARM)

# Dependencies needed to build:
* ninja (Is avalible throught slack package)
* nodejs >= 15.6.0 (Is avalible at [Alien's SlackBuilds](http://www.slackware.com/~alien/slackbuilds/nodejs/build/))
* gcc >= 8 for bootstrapping gn (Is avalible throught slack package)
* nasm >= 2.14 (yasm no longer being used) (Is avalible throught slack package)
* cmake >= 3.13.4 (Is avalible throught slack package)
* python3 >= 3.7, python3-setuptools (Is avalible throught slack package)
* java runtime (Is avalible throught [SARPi Project](https://sarpi.penthux.net/index.php?p=rpiarmcurrentpkgs))
* Internet access (for downloading toolchain bins)

# Optional dependencies to build:
* llvm >= 12.0.0 (Is avalible throught slack package or my [llvm](https://github.com/mostman/Slackbuilds/tree/main/llvm) buildscript or prebuilt [llvm slackware ARM](https://github.com/mostman/Slackbuilds/releases/tag/13.0.0-rc3) package).
Might be a good consideration if you are intending to build chromium/comium-ungoogled your self, as Slackware ARM´s llvm/clang version is missing lld.

# Patch AlienBob´s chromium.Slackbuild
* Download all aliens chromium slackbuild as described by him self.
* Download my additional patches in to the patch directory.
* Download the chromium.arm.SlackBuild.diff file to build directory and patch the build script "patch -p0 < chromium.arm.SlackBuild.diff".

# Replace the buildscript with AlienBob´s chromium.Slackbuild
* Download all aliens chromium slackbuild as described by him self.
* Download my additional patches in to the patch directory.
* Rename AlienBob´s chromium.Slackbuild to chromium.Slackbuild.alien
* Download the chromium.Slackbuild file to build directory.

Some last notes.
Make sure you have at least 15-20 GB free space on your memory card, drive or USBstick (Or where ever you store the source code and tmp folder) and at least 1 GB swap space.
Recommended to set "gpu_mem" to 32 or 64 and then run system in runlevel 3 when compiling.
I´am sorry to say, that estimated compiling time will be at least thirty six hours if not even more.

