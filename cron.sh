MONITDIR="/Users/codeshepherd/Sites/git/automation/others/monit/"
scp ubuntu@hashcube.com:/var/log/monit.log $MONITDIR
cd $MONITDIR; 
python $MONITDIR/alert.py &
