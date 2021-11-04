<div align="center" id="top"> 
  <img src="img/img.png" alt="Speech Recognition System" />

  &#xa0;

  <!-- <a href="https://audioapp.netlify.app">Demo</a> -->
</div>

<h1 align="center">Speech Recognition System</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/human-ai2025/Speech-Recognition-System?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/human-ai2025/Speech-Recognition-System?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/human-ai2025/Speech-Recognition-System?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/human-ai2025/Speech-Recognition-System?color=56BEB8">

  <!-- <img alt="Github issues" src="https://img.shields.io/github/issues/human-ai2025/Speech-Recognition-System?color=56BEB8" /> -->

  <!-- <img alt="Github forks" src="https://img.shields.io/github/forks/human-ai2025/Speech-Recognition-System?color=56BEB8" /> -->

  <!-- <img alt="Github stars" src="https://img.shields.io/github/stars/human-ai2025/Speech-Recognition-System?color=56BEB8" /> -->
</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Speech Recognition System 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/human-ai2025" target="_blank">Author</a>
</p>

<br>

## :dart: About ##

Over the last few years, Voice Assistants have become ubiquitous with the popularity of Google Home, Amazon Echo, Siri, Cortana, and others.These are the most well-known examples of Automatic Speech Recognition (ASR). This class of applications starts with a clip of spoken audio in some language and extracts the words that were spoken, as text. For this reason, they are also known as Speech-to-Text algorithms.Of course, applications like Siri and the others mentioned above, go further. 

> outline
 - extraced features from the  [dataset click here to download](http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz).
 - Build and trained a CNN model. 
 - Deployed the Deeplearning model locally with the help of docker and using flask, uWSGI and nginx to handle web server and traffic routing. 
 - Deployed the same model in cloud [AWS EC2](https://aws.amazon.com/)


## :rocket: Technologies ##

The following tools were used in this project:

- [Docker](https://www.docker.com/)
- [Tensorflow](https://www.tensorflow.org/)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [uWSGI](https://uwsgi-docs.readthedocs.io/en/latest/)
- [nginx](https://www.nginx.com/)
- [AWS](https://aws.amazon.com/)
- [Git](https://git-scm.com)

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Docker](https://www.docker.com/) and [Python](https://www.python.org/) installed. 

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/human-ai2025/Speech-Recognition-System

# Access
$ cd Speech-Recognition-System

# Prepare the data from dataset after downloading it 
$ python prepare_dataset.py
# after running that a data.json file will be created 

# make a testing directory and add some wav files for testing
# train and infer 
$ python main.py --do_train --do_predict

# After doing this, it will give you the model weights [make sure to use the same versions of tensorflow in docker and while buiding the model]

# For docker 
$ docker compose build
$ docker compose up

# This will fire up the web serice for making predictions.
# The server will initialize in the "http://127.0.0.1/predict"
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


Made with :heart: by <a href="https://github.com/human-ai2025" target="_blank">Tarini Tanaya Mohapatra</a>


[image credits](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40ageitgey%2Fmachine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a&psig=AOvVaw09RpyS10gCZyKO9JAoXWTF&ust=1636040269198000&source=images&cd=vfe&ved=0CAwQjhxqFwoTCOChjILD_PMCFQAAAAAdAAAAABAD)
&#xa0;

<a href="#top">Back to top</a>
