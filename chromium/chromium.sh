#!/bin/bash

# Allow users to override command-line options
# Based on Gentoo's chromium package (and by extension, Debian's)
for FILE in /etc/chromium@SRCEXT@/*.conf ; do
  [[ -f ${FILE} ]] && source "${FILE}"
done

# Prefer user defined @CRUSERFLAGS@ flags (from environment) over
# system default @CRFLAGS@ (from /etc/chromium@SRCEXT@)/)
@CRFLAGS@=${@CRUSERFLAGS@:-$@CRFLAGS@}

export CHROME_WRAPPER=$(readlink -f "$0")
export CHROME_DESKTOP=chromium@SRCEXT@.desktop
export CHROME_VERSION_EXTRA="by Minime for Slackware"

exec /usr/lib@LIBDIRSUFFIX@/chromium@SRCEXT@/chromium@SRCEXT@ $@CRFLAGS@ "$@"

