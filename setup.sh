#!/bin/bash

# git clone https://github.com/mdegans/nano_build_opencv
# chmod a+x ./nano_build_opencv/build_opencv.sh
# ./nano_build_opencv/build_opencv.sh
# rm -rf ./nano_build_opencv

if [ ! -f ./libdarknet.so ]; then
    PATH="/usr/local/cuda-10.2/bin:$PATH"
    LD_LIBRARY_PATH="/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH"
    git clone https://github.com/AlexeyAB/darknet
    cd ./darknet
    make \
        GPU=1 \
        CUDNN=1 \
        LIBSO=1 \
        ARCH=' -gencode arch=compute_53,code=[sm_53,compute_53]'
    cp ./libdarknet.so ..
    cd ..
    # rm -rf darknet
fi

# docker-compose build