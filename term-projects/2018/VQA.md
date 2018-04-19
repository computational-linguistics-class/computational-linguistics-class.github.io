---
layout: default
img: python.jpg
img_link: http://xkcd.com/353/
caption: Hello world!
title: Text Visual Question and Answering
active_tab: homework
term_project: true
---

# Visual Question and Answering 


Visual Question and Answering is one of the new hot topics in AI today. The task involves answering open-ended questions about images. These questions require an understanding of vision, language and commonsense knowledge to answer. Please make sure to know the basics of  PyTorch before starting this assignment. This should be a good basic tutorial: http://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html




##  Setup


Clone the base repository from GitHub: https://github.com/hengyuan-hu/bottom-up-attention-vqa. Make sure to have the following prerequisties:
<ul>
        <li> Python 2.7 +
        </li>
        <li> Pytorch with Cuda
        </li>
        <li> Install h5py</li>
</ul>


Once the requirements have been satisfied, let's now move on to downloading the required data for the project. Go to the main directory and run the bash script tools/download.sh. Once the files have been downloaded, let's do some preprocessing. The questions are preprocessed using the python script create_dictionary.py in the tools folder, the image features are loaded in the script detection_features_converter.py and the soft scores for the answers is generated in the compute_softscore.py. Make sure to run all 3 of these files in the given order.


Once the preprocessing has been done, simply run python main.py to train and get accuracy for both training and validation data.


This setup could be tedious and run the main.py for atleast 2 epochs.


## Data Augmentation


Once setup, comprehending the flow and architecture of the model is important. To understand the method better, ensure to read the following papers:
<ul>
        <li>Bottom-Up and Top-Down Attention for Image Captioning and Visual Question Answering: https://arxiv.org/abs/1707.07998 </li>
        <li>Tips and Tricks for Visual Question Answering: Learnings from the 2017 Challenge: https://arxiv.org/abs/1708.02711 </li>
</ul>
The fields of the json file are described here: http://visualqa.org/download.html
For this step, you would be modifying the preprocessing files to add more data to the pickle files that are used for training. As per our presentation, generate data to balance the Yes/No questions using the random assignment idea. Make sure to use the attributes of the json file wisely.


## Spatial features


Download the MSCOCO images from http://cocodataset.org/#download 2015 version. Feed this images using the VGG19 network to extract the features from the Conf5_4 layer (14*14 *512). Store these features and image id as a pickle file. To extract these features, run the following code: (https://github.com/pytorch/vision/blob/master/torchvision/models/vgg.py). Then, load them into our main model and add it as an input to the network (as shown in the slides) in combination with the question embedding was passed into the attention layer to generate the obtained results. 


## POSTag

We found that use of POS tags could result in better performance in the following paper: https://arxiv.org/abs/1801.07853. Easiest way to incorporate the POS tags is to append it to the end of the feature vector (currently the GloVe embedding results in a 300 dimension vector, if you could append ‘n’ dimension vector for POS tags; it will result in a (300+n) dimension vector)


## Results

For each of these features, tabulate your training and validation scores for atleast 5-10 epochs.  

