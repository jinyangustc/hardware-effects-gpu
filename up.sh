#!/usr/bin/env bash

docker run --gpus all --rm -it --mount type=bind,source="$(pwd)",target=/hardware-effects hardware-effects-gpu
