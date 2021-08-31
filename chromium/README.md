# Alien Bob´s Chromium slackbuild adopted for Slackware ARM (SARPI Current)
Addopted Alienbob´s Chromium Slackbuild for Slackware ARM SARPI-Current.
so one can compile chromium for your Slackware ARM Rasberry Pi.

This is only built on SARPI Current Rasberry Pi 4.
I have not tried to build this on any other device nore architecture other than ARM.

This is also just a diff patch.

You can download the script from [Alien BOB´s site](http://www.slackware.com/~alien/slackbuilds).
And then all you need to do is to patch the [chromium.Slackbuild](http://www.slackware.com/~alien/slackbuilds/chromium/build/) with this diff.

Might also want to add the patches from the patch directory.

# What i have done and what the diff/patch does is:
* Added lates patchset "92.0.4515.x"
* Repatched clang.toolchains.arm_i586.triple for ARM.
* Fixed chromium_conf for ARM
* Fixed target triple for ARM.
* Fixed ARM sysroot path/link for libsqlite3.so, glibconfig.h,
dbus-arch-deps.h, graphene-config.h and arm-linux-gnueabihf.conf.
* Fixed link for debians arm-linux-gnueabihf-readelf to slackwares readelf
* Fixed compiling google's internal clang for ARM.
* Fixed missing link to debias readelf for ARM.
