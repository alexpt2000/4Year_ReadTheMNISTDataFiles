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

        images = []

        for i in range(noimg):
            rows = []
            for r in range(norow):
                cols = []
                for c in range(nocol):
                    cols.append(int.from_bytes(f.read(1), 'big'))
                rows.append(cols)
            images.append(rows)
    return images

print("========== Read Labels ===========")
train_labels = read_labels_from_file("data/train-labels-idx1-ubyte.gz")
test_labels = read_labels_from_file("data/t10k-labels-idx1-ubyte.gz")

print("\n========== Read Images ===========")
train_images = read_images_from_file("data/train-images-idx3-ubyte.gz")
test_images = read_images_from_file("data/t10k-images-idx3-ubyte.gz")

for row in test_images[4999]:
    for col in row:
        print('.' if col <= 127 else '#', end='')
    print()

value = 4999

img = train_images[value]
img = np.array(img)
img = pil.fromarray(img)
img = img.convert('RGB')

img.show()
img.save("images/" + value + ".png")


