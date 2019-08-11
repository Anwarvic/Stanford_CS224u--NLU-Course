# Stanford_CS224n (Natural Language Understanding)

This repository contains my solution to the Stanford course "[Natural Language Understanding](http://web.stanford.edu/class/cs224u/)" under CS224u code by prof. [Bill MacCartney](http://nlp.stanford.edu/~wcmac/) and Prof.[Christopher Potts](http://web.stanford.edu/~cgpotts/) in 2019-2020.

This repository contains my solution, but if you want the original assignment, they can be found via the official repository right [here](https://github.com/cgpotts/cs224u/). Also, you can watch the lectures for free on YouTube. Here is the official [playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rObpMCir6rNNUlFAn56Js20).


## About the Course

Project-oriented class focused on developing systems and algorithms for robust machine understanding of human language. Draws on theoretical concepts from linguistics, natural language processing, and machine learning. There will be special lectures on developing projects, presenting research results, and making connections with industry.

It's expected to learn these few concepts after taking this course:

- Lexical semantics
- Distributed representations of meaning
- Relation extraction
- Semantic parsing
- Sentiment analysis
- Dialogue agents

In this repository, you can find nine different lessons. Inside each project, you can find three folders at most:
 
 - *Lab*: which contains exploratory code snippets
 - *HW*: whch contains the homework for this lesson.
 - *Slides*: which contains the slides for this lesson.
 

## Getting Started

This course's code is written to run under Python 3.7. It's really recommended to install Anaconda3 for this course -to save a lot of time and effort- that can be done from [here](https://www.anaconda.com/distribution/).

After that, you need to install these few packages:
```bash
$ # Install Tensorflow
$ conda install -c conda-forge tensorflow

$ # Install PyTorch
$ conda install pytorch torchvision cpuonly -c pytorch

$ # Install mitten
$ pip install mittens

$ # Install popular packages in NLTK
$ python
>>> import nltk
>>> nltk.download('popular')
```

## Acknowledgement

Special Thanks to Stanford for making this great course publically available.

