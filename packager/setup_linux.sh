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
    export PYTHONHOME="$pylith"
    export PATH="$pylith/bin:$PATH"
    export PYTHONPATH="$pylith/lib/python3.10/site-packages:$pylith/lib64/python3.10/site-packages"
    export LD_LIBRARY_PATH="$pylith/lib:$pylith/lib64"

    for arg in "$@"; do
    	if [ $arg = "add-wsl-libs" ]; then
    	    if test ! -d lib-tmp; then
                mkdir lib-tmp
                ln -s /usr/lib/x86_64-linux-gnu/libstdc++.so.6 lib-tmp/
                echo "Created lib-tmp with symbolic link for libstdc++.so.6."
            fi
    	    export LD_LIBRARY_PATH=$pylith_dir/lib-tmp:$LD_LIBRARY_PATH
        elif [ $arg = "enable-software-rendering" ]; then
            export LIBGL_ALWAYS_SOFTWARE=1
            echo "Set LIBGL_ALWAYS_SOFWARE=1."
        else
            echo "Unknown argument '$arg'."
            echo "Usage: source setup.sh [add-wsl-libs] [enable-software-rendering]"
        fi
    done

    echo "Ready to run PyLith."
fi

