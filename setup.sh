#!/bin/bash

if [ ! -f ./libdarknet.so ]; then
    rm -rf ./darknet
    git clone https://github.com/AlexeyAB/darknet
    cd ./darknet
    make \
        LIBSO=1
    cp ./libdarknet.so ..
    cd ..
fi

sudo apt update
sudo apt install npm
sudo npm install -g n
sudo n stable
sudo npm install -g npm

cd webserver
npm install
cd ..