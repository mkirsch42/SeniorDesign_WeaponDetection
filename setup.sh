#!/bin/bash

# git clone https://github.com/mdegans/nano_build_opencv
# chmod a+x ./nano_build_opencv/build_opencv.sh
# ./nano_build_opencv/build_opencv.sh
# rm -rf ./nano_build_opencv

if [ ! -f ./libdarknet.so ]; then
    git clone https://github.com/AlexeyAB/darknet
    cd ./darknet
    make \
        LIBSO=1
    cp ./libdarknet.so ..
    cd ..
    # rm -rf darknet
fi

# docker-compose build