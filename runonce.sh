#!/bin/bash

if ! pgrep -f 'zwaluw.py/zwaluw.py'; then
        /usr/bin/python3 /home/ilambal/zwaluw.py/zwaluw.py > /dev/null;
        echo "starting zwaluw.py"
else
        echo "zwaluw.py is already running"
fi

#pgrep -f zwaluw.py | xargs kill
#/usr/bin/python3 /home/ilambal/zwaluw.py/zwaluw.py