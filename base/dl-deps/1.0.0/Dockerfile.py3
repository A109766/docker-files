FROM datmo/python-base:cpu-py35

MAINTAINER Datmo devs <dev@datmo.com>"

# Add Bazel distribution URI as a package source
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list \
    && curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -

RUN apt-get update && apt-get install -y \
        cmake \
        python-opencv \
        libavcodec-dev \
        libavformat-dev \
        libav-tools \
        libavresample-dev \
        libdc1394-22-dev \
        libgdal-dev \
        libgphoto2-dev \
        libgtk2.0-dev \
        libjasper-dev \
        liblapacke-dev \
        libopencore-amrnb-dev \
        libopencore-amrwb-dev \
        libopencv-dev \
        libopenexr-dev \
        libswscale-dev \
        libtbb2 \
        libtbb-dev \
        libtheora-dev \
        libv4l-dev \
        libvorbis-dev \
        libvtk6-dev \
        libx264-dev \
        libxine2-dev \
        libxvidcore-dev \
        qt5-default \
        && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

RUN pip --no-cache-dir install \
        Cython \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        path.py \
        pyyaml \
        scipy \
        six \
        sklearn \
        sympy \
        Pillow \
        zmq \
        dlib \
        incremental \
        nltk \
        textacy \
        scikit-image \
        spacy \
        tqdm \
        wheel

# Install xgboost
RUN git clone --recursive https://github.com/dmlc/xgboost \
    && cd xgboost \
    && make -j$(nproc) \
    && cd python-package \
    && python setup.py install \
    && cd ../.. \
    && rm -rf xgboost
