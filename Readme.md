# Chatbot based on Transformer NMT Model

nmt-chatbot is the implementation of chatbot using [Google's Transformer model for language understanding](https://www.tensorflow.org/tutorials/text/transformer).
Main purpose of that project is to make a chatbot, but it's fully compatible with Neural Machine Translation and still can be used for sentence translations between two languages.

## Getting Started

```
pip install -r requirements.txt
```

### Testing the Chatbot

In the ``config.yml`` change the ``type`` parameter to ``test`` and run the following command

```
python main.py
```

You would get an interface in the terminal itself.git

### Configuring the Training Parameters

Change the parameters in ``config.yml`` and change the ``type`` to ``train`` and run the following command

```
python main.py
```

The training data should be inside the ``data`` folder.
The conversation data should be kept in 2 files ``train.to`` and ``train.from``.
Each line denotes the id of each 1-1 conversation in from and to form.
``train.from``:

```
Hey
How are you

```

``train.from``:
```
Hi
I am fine
```

### Train on Reddit's conversation threads

You can directly train it over reddit conversations just by providing the subreddits and number of pages for which you want the data.
You can configure this using ``config.yml`` and change the ``reddit_data`` to ``True``. You can mention the subreddits, pages, sorting criteria in ``reddit_config.yml``.
Change the ``type`` in ``config.yml`` to ``train`` and run the following command

```
python main.py

```