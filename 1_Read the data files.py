# Author: Alexander Souza
# Date: 20/10/2017

import gzip
import PIL.Image as pil
import numpy as np


def read_labels_from_file(filename):
    with gzip.open(filename, 'rb') as f:
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("\nMagic is: ", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels: ", nolab)

        labels = [f.read(1) for i in range(nolab)]
        labels = [int.from_bytes(label, 'big') for label in labels]

    return labels


def read_images_from_file(filename):
    with gzip.open(filename, 'rb') as f:

        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("\nMagic is: ", magic)

        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images: ", noimg)

        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of Col: ", nocol)

        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of Row: ", norow)


        # Adapted from
        # https://gist.github.com/akesling/5358964#file-mnist-py-L26
        buffer = f.read(norow * nocol * noimg)
        images = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)
        images = images.reshape(noimg, norow, nocol, 1)

    return images


def print_image(value):
    for row in train_images[value]:
        for col in row:
            print('.' if col <= 127 else '#', end='')
        print()


def save_image(valueStat, valueEnd):
    for total in range(valueStat, valueEnd):
        img = train_images[total]
        img = np.asarray(img, dtype=np.float32)
        img = pil.fromarray((img) ** 16, mode='RGBA').convert('L', dither=pil.NONE)
        img.show()
        img.save('./images/train-%d-%d.png' % (total, train_labels[total]))


print("========== Read Labels ===========")
train_labels = read_labels_from_file("data/train-labels-idx1-ubyte.gz")
test_labels = read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")

print("\n========== Read Images ===========")
train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")
test_images = read_images_from_file("data/t10k-images-idx3-ubyte.gz")


# This value 4999 represents the number 2
value = 4999

# Print image on screen
print_image(value)

# Save each image into a file
# To reduce the time consume to save all images, I just passing 5 images
# save_image(image Start,  Image Finish)
save_image(0, 5)




