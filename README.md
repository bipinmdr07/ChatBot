<h1>Chatbot</h1>
A chatbot that is being created using reddit datasets using deep learning algorithm.

__Dependencies__
* [python 3.5](www.python.org)
* [Tensorflow](www.tensorflow.org)
* [Pandas](https://pandas.pydata.org/)

__Setup__
* First setup the database by running the command:
<pre>
    $ python chatbot_database.py
</pre>
* Generate the test and train datas in the <code>./model</code> directory using the data in database by running following command:
<pre>
    $ python train.py
</pre>
