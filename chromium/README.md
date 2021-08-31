# Alien BOB´s Chromium slackbuild adopted for Slackware ARM (SARPI Current)
Adopted Alien BOB´s Chromium Slackbuild for Slackware ARM SARPI-Current.
so one can compile chromium for your Slackware ARM Rasberry Pi.

This is only built on SARPI Current Rasberry Pi 4.
I have not tried to build this on any other device nore architecture other than ARM.

This is also just a diff patch.

You can download the script from [Alien BOB´s site](http://www.slackware.com/~alien/slackbuilds).
And then all you need to do is to patch the [chromium.Slackbuild](http://www.slackware.com/~alien/slackbuilds/chromium/build/) with this diff.

This is done by placing the diff file in the same directory as chromium.SlackBuild
and then to apply the patch by typing the following command in the terminal:

$ patch -s -p0 < chromium.arm.SlackBuild.diff

Might also want to download/copy the patches from the patch directory to Alien BOB´s patch directory of the chromium slackbuild directory.

# What i have done and what the diff/patch does is:
* Added lates patchset "92.0.4515.x"
* Repatched clang.toolchains.arm_i586.triple for ARM.
* Fixed chromium_conf for ARM
* Fixed target triple for ARM.
* Fixed ARM sysroot path/link for libsqlite3.so, glibconfig.h,
dbus-arch-deps.h, graphene-config.h and arm-linux-gnueabihf.conf.
* Fixed link for debians arm-linux-gnueabihf-readelf to slackwares readelf
* Fixed compiling google's internal clang for ARM.

Some last notes.
Make sure you have at least 15-30 GB free space on your memory card, drive or USBstick (Or where ever you store the source code and tmp folder) and at least 1 GB swap space.
Recommended to set "gpu_mem" to 32 or 64 and then run system in runlevel 3 when compiling.
I´am sorry to say, that estimated compiling time will be at least 24 hours if not even more.

