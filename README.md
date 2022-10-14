# speech2number
E2E method for conversion spoken numbers to text numbers

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
