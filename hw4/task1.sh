#!/bin/bash

ps -u | grep 'bash.*infinite.sh$' | gawk '{print $2}' | xargs --no-run-if-empty -I {} sh -c 'kill {} 2>/dev/null'
