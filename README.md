<h1>Chatbot</h1>
A chatbot that is being created using reddit datasets using deep learning algorithm.

__Datasets Used__
* Google Drive link to [Reddit Dataset](https://drive.google.com/uc?id=1s77S7COjrb3lOnfqvXYfn7sW_x5U1_l9&export=download)

We have selected the one month datasets for this project.

__Dependencies__
* [python 3.5](www.python.org)
* [Tensorflow](www.tensorflow.org)

__Setup__
* First download the dataset from above link and extract it to <code>./data/</code> directory
</pre>
* Generate the test and train datas in the <code>./model</code> directory using the data in database by running following command:
<pre>
    $ python train.py
</pre>
* If you want to resume the training of the model from where you have left then.
<pre>
    # set load_model to True and run
    $ python train.py
</pre>
