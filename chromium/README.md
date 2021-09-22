# Alien BOB´s Chromium slackbuild adopted for Slackware ARM (SARPI Current)
Adopted Alien BOB´s Chromium Slackbuild for Slackware ARM SARPI-Current.
so one can compile chromium for your Slackware ARM Rasberry Pi.

This is only built on SARPI Current Rasberry Pi 4.
I have not tried to build this on any other device nore architecture other than ARM.

Might also want to download/copy the patches from the patch directory to Alien BOB´s patch directory of the chromium slackbuild directory.

# What i have done and what the diff/patch does is:
* Added lates patchset "93.0.4577.8"
* Repatched clang.toolchains.arm_i586.triple for ARM.
* Fixed chromium_conf for ARM
* Fixed target triple for ARM.
* Fixed ARM sysroot path/link for libsqlite3.so, glibconfig.h,
dbus-arch-deps.h, graphene-config.h and arm-linux-gnueabihf.conf.
* Fixed link for debians arm-linux-gnueabihf-readelf to slackwares readelf
* Fixed compiling google's internal clang for ARM.
* Also made it possible to use eithers systems llvm/clang version or my slackbuild llvm/clang version.
* Patched chromium for arm to support Widevine. (Using my patched glibc will also make Widevine 4.10.2252.0 working)

# Dependencies needed to build:
* ninja (Is avalible throught slack package)
* nodejs >= 15.6.0 (Is avalible at [Alien's SlackBuilds](http://www.slackware.com/~alien/slackbuilds/nodejs/build/))
* gcc >= 8 for bootstrapping gn (Is avalible throught slack package)
* nasm >= 2.14 (yasm no longer being used) (Is avalible throught slack package)
* cmake >= 3.13.4 (Is avalible throught slack package)
* python3 >= 3.7, python3-setuptools (Is avalible throught slack package)
* java runtime (Is avalible throught [SARPi Project](https://sarpi.penthux.net/index.php?p=rpiarmcurrentpkgs))
* Internet access (for downloading toolchain bins)

Some last notes.
Make sure you have at least 10-20 GB free space on your memory card, drive or USBstick (Or where ever you store the source code and tmp folder) and at least 1 GB swap space.
Recommended to set "gpu_mem" to 32 or 64 and then run system in runlevel 3 when compiling.
I´am sorry to say, that estimated compiling time will be at least thirty six hours if not even more.

