---
repository: "libffcv/ffcv"
github_id: 416829986
url: "https://github.com/libffcv/ffcv"
description: "FFCV: Fast Forward Computer Vision (and other ML workloads!)"
starred_at: "2022-02-02T11:45:33Z"
language: "Python"
topics: ["data-science", "machine-learning", "pytorch"]
homepage: "https://ffcv.io"
license: "Apache-2.0"
archived: false
---

# libffcv/ffcv

FFCV: Fast Forward Computer Vision (and other ML workloads!)

**GitHub:** https://github.com/libffcv/ffcv

## README excerpt

> Fast Forward Computer Vision: train models at a fraction of the cost with accelerated data loading!
>
>
> [install]
> [quickstart]
> [features]
> [docs]
> [support slack]
> [homepage]
> [paper]
>
> Maintainers:
>
> `ffcv` is a drop-in data loading system that dramatically increases data throughput in model training:
> - [Train an ImageNet model](#prepackaged-computer-vision-benchmarks)
> on one GPU in 35 minutes (98¢/model on AWS)
> - [Train a CIFAR-10 model](https://docs.ffcv.io/ffcv_examples/cifar10.html)
> on one GPU in 36 seconds (2¢/model on AWS)
> - Train a `$YOUR_DATASET` model `$REALLY_FAST` (for `$WAY_LESS`)
> Keep your training algorithm the same, just replace the data loader! Look at these speedups:
> `ffcv` also comes prepacked with [fast, simple code](https://github.com/libffcv/imagenet-example) for [standard vision benchmarks]((https://docs.ffcv.io/benchmarks.html)):
> ## Installation
> ### Linux
> conda create -y -n ffcv python=3.9 cupy pkg-config libjpeg-turbo opencv pytorch torchvision cudatoolkit=11.3 numba -c pytorch -c conda-forge
> conda activate ffcv
> pip install ffcv
> Troubleshooting note 1: if the above commands result in a package conflict error, try running ``conda config --env --set channel_priority flexible`` in the environment and rerunning the installation command.
> Troubleshooting note 2: on some systems (but rarely), you'll need to add the ``compilers`` package to the first command above.
> Troubleshooting note 3: courtesy of @kschuerholt, here is a [Dockerfile](https://github.com/kschuerholt/pytorch_cuda_opencv_ffcv_docker) that may help with conda-free installation
> ### Windows
> * Install opencv4
> * Add `..../opencv/build/x64/vc15/bin` to PATH environment variable
> * Install libjpeg-turbo, download libjpeg-turbo-x.x.x-vc64.exe, not gcc64
> * Add `..../libjpeg-turbo64/bin` to PATH environment variable
> * Install pthread, download last release.zip
> * After unzip, rename Pre-build.2 folder to pthread
> * Open `pthread/include/pthread.h`, and add the code below to the top of the file.
> #define HAVE_STRUCT_TIMESPEC
> * Add `..../pthread/dll` to PATH environment variable
> * Install cupy depending on your CUDA Toolkit version.
> * `pip install ffcv`
> ## Citation
> If you use FFCV, please cite it as:
> @inproceedings{leclerc2023ffcv,
> author = {Guillaume Leclerc and Andrew Ilyas and Logan Engstrom and Sung Min Park and Hadi Salman and Aleksander Madry},
> title = {{FFCV}: Accelerating Training by Removing Data Bottlenecks},
> year = {2023},
> booktitle = {Computer Vision and Pattern Recognition (CVPR)},
> n

## Personal notes

<!-- Optional. Manual notes are never overwritten by sync. -->
