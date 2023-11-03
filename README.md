## Berkeley Speech Group's Fall 2023 Speech + ML Workshop

Hi! Welcome to an interactive workshop hosted by Robbie from the Berkeley Speech Group on a quick introduction to speech and machine learning. 

### Installation Requirements

Must have `PyTorch 2.1` and `Torchaudio 2.1`  installed. Please follow the install instructions [here](https://pytorch.org/get-started/locally/) to download PyTorch. If you have a CUDA compatible device, we recommend you install the CUDA-compatible version. If not, the CPU is fine! This should not be *too* compute intensive.

Other packages include: 
* `matplotlib`
* `seaborn`
* `pandas`
* `numpy`

The workbooks in this tutorial should be compatible with Python >=3.8. 

### How to navigate this Repo

This repo contains the slides and the workbooks associated with the workshop! The goal was to design an interactive tutorial for people with varying degrees of exposure to speech and machine learning, meaning there are multiple ways to work through this repo. The notebooks are split in the following way:
* `0X`: Data Exploration with Pandas
* `1X`: Classical ML and Deep Learning

If you are completely new to Pandas, Speech, and Machine Learning, we recommend you start proceed through the workbooks in `audio_ml_workshop_2023/workbooks/` in numerical order, possibly skipping over workbooks beginning with `0X` if you want to jump straight into Machine Learning. Pandas familiarity is not necessary, but might make the code easier to understand!

If you already have some experience with classical Machine Learning, you can skip workbook `10_hubert_prediction.ipynb`, but note that it contains helpful code for reading in audio files and processing them with a pre-trained HuBERT Model. 

A quick note, if you get stuck, feel free to bug Robbie or check out the `notebooks/` dir for the answers! Try to give it your best shot before checking the answer key, of course, but also don't leave yourself out to dry too long! 

If you are already experienced with both Speech and Deep Learning, this workbook is a challenge. Your goal is to design and train a deep architecture that outperforms Random Forest on predicting Perceptual Quality (PQ) vectors from HuBERT features, which measured as validation RMSE averaged across all PQs is roughly `12.85`. All of this must be done locally on your machine (no lab compute!) and within the span of the workshop (1.5-2 hrs). At the end of the workshop, we'll compare folks models' architectures and designs. Feel free to start with the model in `notebooks/11_deep_hubert_prediction.ipynb` and make a bunch of variations--Well, the variations your compute will allow!

### What's the prediction task?

In this workshop, we'll be trying to predict [Perceptual Quality (PQ) vectors](https://arxiv.org/abs/2310.02497) from HuBERT features. Specifically, we will try to predict the five PQs from the Consensus Auditory-Perceptual Evaluation of Voice  (CAPE-V): Pitch, Roughness, Loudness, Strain, and Breathiness. The data we'll be using is located in `audio_ml_workshop_2023/data/pvqd`, and comes from the [Perceptual Voice Qualities Database (PVQD)](https://voicefoundation.org/perceptual-voice-qualities-database/). The workbook `00_data_exploration` looks over some high-level statistics about the dataset, if you're curious. The README from the dataset isn't in this Repo, so if you want more information, you're either going to have to look at the data yourself, or go searching the internet for it!

You'll get this info though: The labels are CAPE-V 1-100 ratings, where `100` signifies a voice high in a particular perceptual quality. In the case of Pitch or Loudness, it might not be what you think. (Listen to the data or read a paper if you're curious!). Your goal is to predict the PQ vector for a given speaker with low Root Mean Squared Error on the validation set.

Don't touch the test set. Don't do it!

### Why are you being so cagey with info?

When you do research, often times the code you find online, or the papers you read, are incomplete, incorrect, and messy as all get out. This workshop is trying to emulate that experience--a bit. The code in these notebooks, and the recommended way you work through it, might not be all that good. You might wonder why I choose to implement a code snippet a particular way, or you think to yourself that something is incredibly inefficient. 

Good. You should be asking these questions. 

Part of doing research, in my opinion, is holding the egocentric belief that you can do something better, or at the very least differently, than others. Look for the holes in people's code or methods, question why they decided to do things the way they did, and think about how to do it the way you want to. That's how research is done. 

Good luck!
