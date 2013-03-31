MONITDIR="path to monti dir"
scp user@domain.com:/var/log/monit.log $MONITDIR
cd $MONITDIR; 
python $MONITDIR/alert.py &
