#!/bin/bash

RPC_SCRIPT="/home/"$(whoami)"/helixLSP/main.py"


while true; do
    if pgrep -i helix > /dev/null; then
        echo "Helix Open"
        file_name=$(pgrep -a helix | sed 's/^[^ ]* *[^ ]* *//')

        if ! pgrep -f /home/"$(whoami)"/helixLSP/main.py > /dev/null; then
            python "$RPC_SCRIPT" "$file_name" &
            echo "RPC Set"
        fi        
    else
        pkill -f /home/"$(whoami)"/helixLSP/main.py
    fi
done
