#!/bin/bash

env
if [[ -a build-failer ]]
  then
    echo "found build-failer, failing build."
    exit 1
fi

echo "didnt find build-failer."
