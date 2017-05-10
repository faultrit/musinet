import os.path


seq_length = 512
num_channels = 4
save_path = 'save/value_net.sav'
data_path = '../data/train.pkl'
batch_size = 32
default_lr = 0.001


def can_restore():
    return os.path.exists(save_path)
