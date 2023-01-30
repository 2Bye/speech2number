# speech2number
E2E method for conversion spoken numbers to text numbers

P.S.

This project is a test task. The goal of the project is to show how the problem can be approached. Quality and results have a lower priority

## Description 

The method receives an **Russian-speech** WAV audio (mono, 16000KHz) file and uses it as an input to the model, based on a [QuartzNET - deep convolutional neural network.](https://arxiv.org/abs/1910.10261) 

The implementation of the model is taken from [NeMo framework](https://github.com/NVIDIA/NeMo)

The method uses an ASR-trained model with a specific vocabulary that covers all possible numerical verbal transcriptions up to 1,000,000

It also uses an open source library [text2num](https://pypi.org/project/text2num/) and [num2words](https://pypi.org/project/num2words/)

## How the model was trained

The training dataset had file paths and numbers that are spoken in the audio file. The numbers were translated into text using an open source library [num2words](https://pypi.org/project/num2words/). Next, the ASR model was trained. Model recognizes spoken numbers. Transcription of the audio file is converted back to a number using library [text2num](https://pypi.org/project/text2num/)


## How does it work?

The user should run the script and provide the path to the csv file, as well as the path to the output file. Output file will contain two columns: path and number. Input file should contain one column : path

**Example**:

``` sh inference.sh examples/example_input.csv results.csv ```

Examples of input and output files can be found in the folder **examples/**

## Results

Below are the validation graphs when training the model

<img width="250" alt="image" src="https://user-images.githubusercontent.com/45552093/195869022-856475a3-ef19-4570-bcb7-27bd4d2a9345.png">
<img width="250" alt="image" src="https://user-images.githubusercontent.com/45552093/195869061-2a00f676-c7a6-4775-82f8-d7acd177954f.png">

The model was also tested on test data

* WER: 0.1313
* CER: 0.0532

However, when the model was tested on "in the wild data", the results were poor.
This can be solved by increasing the unique speakers and increasing the amount of training data.

## Installation and Requirements

* Python 3.8 or above
* Pytorch 1.10.0 or above
* NVIDIA GPU for fast inference

**Сreating an environment**

```
conda create --name russian_numbers python==3.8
conda install pytorch torchaudio cudatoolkit=11.3 -c pytorch
apt-get update && apt-get install -y libsndfile1 ffmpeg

# or pip3
pip install Cython 
pip install nemo_toolkit['asr']
pip install text_unidecode
```

## To Do list

* Create end-to-end inference without using bash console
* Сreate training guide

## Possible improvements

* Improve data labeling _(in this case, automatic labeling was used)_
* More training data _(in this case, 5500 samples were used)_
* Increase model  _(up to 2 mb, in this case - 500Kb or ~94k parameters)_
