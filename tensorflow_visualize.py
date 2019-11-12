# From https://gist.github.com/nlothian/0cd4540389f7091717ece6f4b89b6604 - modified

from tensorflow.contrib.tensorboard.plugins import projector
import tensorflow as tf
import numpy as np
import os


def tf_visualize(data, meta_file, output_path, labels=None):
    """
    Visualize data contained in Pandas DataFrame in TensorBoard to explore data.
    
    Looks for a labels column but default is to use the index. Assumes all data is numerical.
    
    :param data: pandas data frame with data
    :param meta_file: file to save labels too (for each point in the data frame)
    :param output_path: folder to save tensorboard files
    :param labels: name of column in data frame containing labels of each data point (default is to use indices of data frame)
    """
    if labels in data.columns:
        np.savetxt(os.path.join(output_path,meta_file), data[labels].values)
        placeholder = data.loc[:, data.columns != labels].values
    else:
        np.savetxt(os.path.join(output_path,meta_file), data.index.values)
        placeholder = data.values

    # define the model without training
    sess = tf.InteractiveSession()

    embedding = tf.Variable(placeholder, trainable=False, name=meta_file[:-4])
    tf.global_variables_initializer().run()

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter(output_path, sess.graph)

    # adding into projector
    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.tensor_name = meta_file[:-4]
    embed.metadata_path = meta_file

    # Specify the width and height of a single thumbnail.
    projector.visualize_embeddings(writer, config)
    saver.save(sess, os.path.join(output_path, meta_file[:-4]+'.ckpt'))
    print('Num nodes: {}'.format(data.shape[0]))
    print('Run `tensorboard --logdir={0} --port xxxx --host 0.0.0.0` to run visualize result on tensorboard'.format(output_path))

    
