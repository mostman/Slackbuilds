# Regarding the included python script from DavidBuchanan314 for Slackware aarch64 devices:
(This does however not concern ARM as the python script "widevine_fixup.py" is only used to resolve issues  
on aarch64 non-ChromeOS linux systems.)

IMPORTANT NOTE: On systems with >4k page size (e.g. Apple Silicon devices),
Using the patched binary *significantly* weakens the security of your web browser,
in two ways. Firstly, it disables the RELRO security mitigation, and secondly it
creates a RWX mapping.

I'm looking into ways around this, but it will require more advanced patching.

P.S. If you want to watch Netflix, you will need to spoof a ChromeOS useragent