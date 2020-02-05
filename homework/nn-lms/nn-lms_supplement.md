---
layout: default
title: Homework 6 - Biglab, local  setup
active_tab: homework
release_date: 2019-02-26
due_date: 2017-03-12T23:59:00EST

---

#### Local/Biglab setup
Miniconda is a package, dependency and environment management for python (amongst other languages). It lets you install different versions of python, different versions of various packages in different environments which makes working on multiple projects (with different dependencies) easy.

There are two ways to use miniconda,

1. **Use an existing installation from another user**: On ```biglab```, add the following line at the end of your ```~/.bashrc``` file.
```
export PATH="/home1/c/cis530/miniconda3/bin:$PATH"
```
Then run the following command
```
source ~/.bashrc
```
If you run the command ```$ which conda```, the output should be ```/home1/c/cis530/miniconda3/bin/conda```.

2. **Installing Miniconda from scratch**: On ```biglab```, run the following commands. Press Enter/Agree to all prompts during installation.
```
$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ chmod +x Miniconda3-latest-Linux-x86_64.sh
$ bash Miniconda3-latest-Linux-x86_64.sh
```
After successful installation, running the command ```$ which conda``` should output ```/home1/m/$USERNAME/miniconda3/bin/conda```.

#### Installing Pytorch and Jupyter

For this assignment, you'll be using [Pytorch](http://pytorch.org/) and [Jupyter](http://jupyter.org/).

1. If you used the existing miniconda installation from 1. above, you're good to go. Stop wasting time and start working on the assignment!

2. Intrepid students who installed their own miniconda version from 2. above, need to install their own copy of Pytorch and Jupyter.
To install Pytorch, run the command
```
conda install pytorch-cpu torchvision -c pytorch
```
To check, run python and ```import torch```. This should run without giving errors.
To install jupyter, run the command (it might take a while)
```
conda install jupyter
```
Running the command ```jupyter --version``` should yield the version installed.

#### How to use Jupyter notebook
For this homework, you have the option of using [jupyter notebook](https://jupyter.org/), which lets you interactively edit your code within the web browser. Jupyter reads files in the `.ipynb` format. To launch from biglab, do the following.

1. On ```biglab```, navigate to the directory with your code files and type `jupyter notebook --port 8888 --no-browser`. If you are having token issues, you may need to also add the argument `--NotebookApp.token=''`.
2. In your local terminal, set up port forward by typing `ssh -N -f -L localhost:8888:localhost:8888 yourname@biglab.seas.upenn.edu`.
3. In your local web browser, navigate to `localhost:8888`.
