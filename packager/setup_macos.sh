pylith=`pwd`

if test ! -f bin/pylith; then
    echo
    echo "*** Error! ***"
    echo
    echo "Source this script from the top-level PyLith directory:"
    echo
    echo "    cd [directory containing 'setup.sh']"
    echo "    source setup.sh"
    echo 
else
    export TERM="xterm-256color"
    export PYTHONHOME="$pylith"
    export PATH="$pylith/bin:/bin:/usr/bin:/sbin/:/usr/sbin:$PATH"
    export PYTHONPATH="$pylith/lib/python3.12/site-packages"
    export FI_PROVIDER="tcp"
    echo "Ready to run PyLith."
fi
