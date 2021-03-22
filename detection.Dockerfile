# FROM datamachines/jetsonnano-cuda_tensorflow_opencv:10.0_2.1.0_4.3.0-LOCALBUILD
FROM nvcr.io/nvidia/l4t-base:r32.4.4

RUN apt-get update && apt-get install -y \
    pkg-config \
    libblas-dev \
    liblapack-dev \
    libhdf5-dev \
    libgtk2.0-dev \
    gfortran
ENV LD_LIBRARY_PATH /usr/lib/aarch64-linux-gnu/hdf5/serial:$LD_LIBRARY_PATH

RUN apt-get install -y python3 python3-pip && \
    python3 -m pip install --upgrade pip

COPY ./requirements.txt /tmp/
RUN pip3 install Cython
RUN pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v44 -r /tmp/requirements.txt
RUN pip3 install python-socketio==4.* aiohttp

COPY ./libdarknet.so /usr/local/lib
ENV LIB_DARKNET /usr/local/lib/libdarknet.so

RUN mkdir /app && \
    mkdir /input
WORKDIR /app

CMD ["python3", "/app/main.py"]
