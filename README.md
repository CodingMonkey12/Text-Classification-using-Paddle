# Text-Classification-using-Paddle

## 🎨 Language

[English]: ./README.md	"English"
[中文]: ./README-中文.md	"中文"

* [English](/README.md)
* [中文](/README-中文.md)

## 📝 Description

This code is used `Paddle` to do a `text classification`.

The text can be Chinese or English, but the model is `monolingual`. It means that you must know the language of the text input, and choose the right model to predict.

The monolingual models I used:

* for Chinese text: `hfl/roberta-wwm-ext-large`
* for English text: `ernie-2.0-large-en`

Of course, you can use the `multilingual` model to train, maybe the accuracy will not better than the monolingual model, I guess.

## ⚙ Environment

* It used `1 * NVIDIA Tesla V100 32G` to train model(Recommended). Ensure that CUDA is installed.
* Of course you can use CPU to train model

## 🛠 Requirements

* Python 3.9
* paddlepaddle 2.1.3
  * If you need a `CPU only` version, please install the  this version
  * Else if you need a `GPU` version, please install the right version that based on your GPU and CUDA.
    For example: paddlepaddle-gpu==2.1.3.post101
* paddlenlp 2.1.0

If you want to deploy models, you also need to install:

* fastapi 0.79
* uvicorn 0.18.2

## 📚 Files

* There are two folders:
  * `1 - train`: Only to train a model that can predict text
  * `2 - deploy`: Only to deploy the trained model on VPS, and set up API
* It used `Jupyter Notebook` to easily start. Of course you can convert `.ipynb` to `.py`
* The step is the index of the files
* For example, you will run the file started with `1 - xxx.ipynb`, and then run the file started with `2 - xxx.ipynb`
* The files in `1 - train/checkpoint` and `2 - deploy/models` folder are fake files! You must get these files after running ipynb

## 📖 Data

* There are only some example text in data folder

* You need to convert your data into a `csv` file, which split by `\t`

* example data:

  | text_a                                                | label |
  | ----------------------------------------------------- | ----- |
  | Do you ever get a little bit tired of life            | A     |
  | Like you're not really happy but you don't wanna die  | B     |
  | ...                                                   | ...   |
  | Like you're hangin' by a thread but you gotta survive | B     |
  | 'Cause you gotta survive                              | C     |

* You have to confirm that there is no `\t` in text and labels. `Important!!!`

* You need to split the data into train(80%) and test(20%), of course the rate you can set by yourself

## 🎯 To Run

Maybe there are something you have to change. For example: path

* Step 1: run `train.ipynb`. After running, you can get the model in `checkpoint` folder
  * If your text language is Chinese, please run `1.1 - train_Chinese.ipynb`
  * Else if your text language is English, please run `1.2 - train_English.ipynb`
* Step 2(Optional): run `2 - evaluate.ipynb`. After running, you can get the classification reports
* Step 3(Optional): run `3 - predict.ipynb`. After running, you can get the prediction from your file
* Step 4(Optional): run `4 - predict_only_one.ipynb`. After running, you can predict only one text
* Step 5: run `5 - to_static.ipynb`. After running, you can get the infer model that can be deployed
* Step 6(Optional): run `6 - infer.ipynb`. A test to infer

## 📢 Deploy

After getting the infer model, you can deploy it by using FastAPI or other API framework.

Please copy your files into `2 - deploy/models/English` or `2 - deploy/models/Chinese` and make them in your model folder like:

* label_map.json
* model.pdiparams
* model.pdiparams.info
* model.pdmodel
* tokenizer_config.json
* vocab.txt

Run: `python main.py`

Visit: `localhost:1234/docs` to read docs

## 💡 Others

Docs about PaddlePaddle, PaddleNLP and FastAPI

* [PaddlePaddle](https://www.paddlepaddle.org.cn/en)
* [PaddleNLP](https://paddlenlp.readthedocs.io/en/latest/)
* [FastAPI](https://fastapi.tiangolo.com/)