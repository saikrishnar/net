from net import RecurrentNetwork, load_fruitspeech, labels_to_chars
import matplotlib.pyplot as plt
import numpy as np

(train_x, train_y), (valid_x, valid_y), (test_x, test_y) = load_fruitspeech()
clf = RecurrentNetwork(learning_alg="rmsprop",
                       hidden_layer_sizes=[500],
                       max_iter=100, cost="encdec", bidirectional=True,
                       learning_rate=0.00002, momentum=0.9,
                       recurrent_activation="lstm",
                       random_seed=1999)

all_frames = np.vstack(train_x)
means = np.mean(all_frames, axis=0)
std = np.std(all_frames, axis=0)
for n, t in enumerate(train_x):
    train_x[n] = (t - means) / std

for n, v in enumerate(valid_x):
    valid_x[n] = (v - means) / std

from IPython import embed; embed()


clf.fit(train_x, train_y, valid_x, valid_y)
y_hat = labels_to_chars(clf.predict(valid_x[0])[0])
y = labels_to_chars(valid_y[0])
print(y_hat)
print(y)
