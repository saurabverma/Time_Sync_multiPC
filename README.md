# Time_Sync_multiPC

***Automatically once at boot-up:***


From a user perspective, no effort is required to sync the two PCs because the Slave PC will automatically set its own date-time equal to the one on Master PC within about a few millisecond difference, under the following two conditions:

    Slave and Master PC are on the same network
    After about 10-15s from switching ON the Slave PC, it pings Master PC to get the date-time details - at that point of time the Master PC must be ON and ready to handle the incoming ssh signal from the Slave PC.

Hence, once we switch ON both Slave and Master PC collectively, within about 20s the two PC must be time-synced.
Also, this works every-time the Slave PC boots-up (regardless manual or via software i.e. restart).



***Manually request to keep checking for time sync periodically:***

However, if only the Master PC is restarted, it's time may change and this change may not be reflected on the Slave PC.
Therefore, in order to continuously make the Slave PC periodically sync time with the Master PC, a ROS node (placed on the desktop folder of Slave PC, I think) can be used. The sync frequency can be input as a ROS param.  



***Additional points:***

Currently, the best way to check if the two PC are synced is to type 'date' command on both PC terminals an, manually check that the date-time for the two PCs are very close.

Note that this whole setup is kind-of-a manual approach towards time synchronization completely devised by myself - but it should suffice well for our MATAR robot requirements.
Just FYI, a more accurate way is to set 'chrony' but I have had very unpleasant experiences with it w.r.t. convenience and robustness, which is why I don't prefer it.

Hope this all helps, let me know if any further clarification is needed.
