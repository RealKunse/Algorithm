import torch
import pickle
import matplotlib.pyplot as plt

broken_image = torch.FloatTensor(pickle.load(open('./broken_image_t.p', 'rb'), encoding='latin10'))

plt.imshow(broken_image.view(100, 100))


def weird_function(x, n_iter=5):
    h = x
    filt = torch.tensor([-1. / 3, 1. / 3, -1. / 3])
    for i in range(n_iter):
        zero_tensor = torch.tensor([1.0*0])
        h_l = torch.cat((zero_tensor, h[:-1]),0)
        h_r = torch.cat((h[1:], zero_tensor),0)
        h = filt[0] * h + filt[2] * h_l + filt[1] * h_r
        if i % 2 == 0:
            h = torch.cat((h[h.shape[0]//2:], h[:h.shape[0]//2]), 0)

    return h
