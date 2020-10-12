# Deep Twitter Q&A

## Introduction

Have you ever wanted to know how someone special would reply on Twitter? Train a model on their twitter data.

This repository has adapted [Conchylicultor/DeepQA](https://github.com/Conchylicultor/DeepQA) to specifically ONLY work with tweets.
Note that by default scraping Twitter and using their API will only yield you a maximum of 3200 tweets; most likely less.
Twitter data will be collected by using the Twitter API. More specifically, all the answers of the person of interest in respond to questions is what the model will be trained on.


If there are companies out there who would like to have a custom QA application, feel free to contact me.

## Usage

### Twitter API Credentials
1) Register a Twitter API Developer account

3) Fill in your Twitter dev credentials in `chatbot/credentials.json`.

### Building the Bot
Then you can run:

    python main.py --twitter_name gvanrossum

to build a model after the BDFL (where gvanrossum would be replaced by the username of the Twitter user you'd like to build the bot after)

... 20 minutes later ...

### Testing your Bot
Run

    python main.py --twitter_name gvanrossum --test interactive

to have an interactive QA session with Guido.

## Example

Question asked after having trained on default settings:

    Q: which editor do you use ?
    A: emacs of course !

## Twitter data

You can see the collected twitter data at:

    data/tweets/<username>-answers.txt
    data/tweets/<username>-questions.txt

## Installation (quoting Conchylicultor)

### Dependencies
The program requires the following dependencies:

 * python 3.5
 * tensorflow (tested with v0.9.0 and v0.11.0)
 * numpy
 * CUDA (for using gpu, see TensorFlow [installation page](https://www.tensorflow.org/versions/master/get_started/os_setup.html#optional-install-cuda-gpus-on-linux) for more details)
 * nltk (natural language toolkit for tokenized the sentences)
 * tqdm (for the nice progression bars)

### Installing Dependencies
 * These are easy to install using pip in terminal/CMD (example: pip install nltk)
 * Or simply use "pip pip install -r requirements.txt" in terminal/CMD (Which will install all requirments - minus CUDA)
 * Or simply use the provided 1) Install requirments.bat file (on Windows) to do the above

## Further instructions

You're advised to experiment with the possible parameters to make it a better model.

Have a look at the [original repo](https://github.com/Conchylicultor/DeepQA) for more information.
