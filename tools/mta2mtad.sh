#!/bin/bash

runit=false

echo "param: $1"

if [ "$1" = "dryrun" ] ; then
    runit=false
else
    runit=true
fi

if [ "$runit" = true ] ; then
    echo "Actually running these commands."
else
    echo "Performing a dry run."
fi

function exec_or_dump() {

        xcmd=$1
        echo $xcmd
        if [ "$runit" = true ] ; then
            eval $xcmd
        fi

}

cmd='cp mta.yaml mtad.yaml'
exec_or_dump "$cmd"

#cmd='sed -i -e "s/html5/'$gitname'/g" '$lcorg'_mta_nodejs_cf.job'
#exec_or_dump "$cmd"

echo ""
echo "Done."
