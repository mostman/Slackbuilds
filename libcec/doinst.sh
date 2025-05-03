if [ -e /dev/vchiq ]; then
  chown root:video /dev/vchiq
  chmod g+rw /dev/vchiq
  echo 'KERNEL=="vchiq",GROUP="video",MODE="0660"' > /etc/udev/rules.d/10-vchiq-permissions.rules
elif [ -e /dev/vc-sm ]; then
  chown root:video /dev/vc-sm
  chmod g+rw /dev/vc-sm
  echo 'KERNEL=="vc-sm",GROUP="video",MODE="0660"' > /etc/udev/rules.d/10-vc-sm-permissions.rules
elif [ -e /dev/bcm2708_vcio ]; then
  chown root:video /dev/bcm2708_vcio
  chmod g+rw /dev/bcm2708_vcio
  echo 'KERNEL=="bcm2708_vcio",GROUP="video",MODE="0660"' > /etc/udev/rules.d/10-bcm2708_vcio-permissions.rules
fi
