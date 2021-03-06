import tensorflow as tf
from tensorflow.keras import layers


def get_architecture_op(num_nodes=512):
    def architecture_op(ranking_features):
        first_dense = layers.Dense(num_nodes, activation="relu", name="first_dense")(
            ranking_features
        )
        first_dropout = layers.Dropout(rate=0.3, name="first_dropout")(first_dense)
        final_dense = layers.Dense(64, activation="relu", name="final_dense")(first_dropout)
        # _ = tf.keras.layers.Dropout(rate=0.1g)(_)
        scores = layers.Dense(1, name="scores")(final_dense)

        # Collapse extra dimensions
        scores = tf.squeeze(scores, axis=-1)

        return scores

    return architecture_op
