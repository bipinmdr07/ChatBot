<h1>Chatbot</h1>
A chatbot that is being created using reddit datasets using deep learning algorithm.

__Datasets Used__
* [Reddit Dataset](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment/?st=j9udbxta&sh=69e4fee7)

We have selected the one month datasets for this project.

__Dependencies__
* [python 3.5](www.python.org)
* [Tensorflow](www.tensorflow.org)
* [Pandas](https://pandas.pydata.org/)

__Setup__
* First download the dataset from above link and extract it to <code>./data</code> directory
* Populate the database by running the command:
<pre>
    $ python chatbot_database.py
</pre>
* Generate the test and train datas in the <code>./model</code> directory using the data in database by running following command:
<pre>
    $ python train.py
</pre>
