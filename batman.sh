#stop network manager to make the mesh network work

#configure the wlan interface to operate with mtus of 1532(batman requires it) and turn enc off to ensure it works
ifconfig wlan0 down
ifconfig wlan0 mtu 1532
iwconfig wlan0 enc off

#add the interface to the ad-hoc network - or create it.
iwconfig wlan0 mode ad-hoc essid NCMESHNET ap 02:12:34:56:78:9A channel 1

#load the module up
modprobe batman-adv

#add wlan0 to the batman-adv virtual interface(so it can communicate with other batman-adv nodes)
batctl if add wlan0
ifconfig wlan0 up
ifconfig bat0 up

ifconfig bat0 192.1.2.2