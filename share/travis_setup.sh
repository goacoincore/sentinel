#!/bin/bash
set -evx

mkdir ~/.goacoincore

# safety check
if [ ! -f ~/.goacoincore/.goacoin.conf ]; then
  cp share/goacoin.conf.example ~/.goacoincore/goacoin.conf
fi
