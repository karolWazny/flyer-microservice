#!/bin/bash
cd /home/aeki
cd exsultate
source virt/bin/activate
export FLASK_APP=api/api
nohup flask run --host=0.0.0.0 &>/dev/null &