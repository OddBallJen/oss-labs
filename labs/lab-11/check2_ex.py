# TensorFlow and tf.keras
import tensorflow as tf


# Helper libraries
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# print(tf.__version__)

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

train_images.shape

print("type is: " + str(type(train_images))+"\n")
len(train_labels)

train_labels

test_images.shape

len(test_labels)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images = train_images / 255.0

test_images = test_images / 255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
# plt.show()

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

# print('\nTest accuracy:', test_acc)

# -- training complete -- 

# make predictions
probability_model = tf.keras.Sequential([model, 
                                         tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

print(predictions[0])

np.argmax(predictions[0])

test_labels[0]


def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

i = 0
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
# plt.show()

i = 12
plt.figure(figsize=(6,3))
plt.subplot(1,2,1)
plot_image(i, predictions[i], test_labels, test_images)
plt.subplot(1,2,2)
plot_value_array(i, predictions[i],  test_labels)
# plt.show()

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i+9000, predictions[i], test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_labels)
plt.tight_layout()
plt.show()


# Grab an image from the test dataset.
#img = test_images[1]

#print(img.shape)

# Add the image to a batch where it's the only member.
#img = (np.expand_dims(img,0))

#print(img.shape)

#predictions_single = probability_model.predict(img)

#print(predictions_single)

#plot_value_array(1, predictions_single[0], test_labels)
#_ = plt.xticks(range(10), class_names, rotation=45)
#plt.show()

#np.argmax(predictions_single[0])

######################### Checkpoint 3 ####################################

img1 = Image.open("clothes1_edited.jpg")
img2 = Image.open("clothes2_edited.jpg")
img3 = Image.open("clothes3_edited.jpg")

img1 = np.array(img1)
img2 = np.array(img2)
img3 = np.array(img3)

img1 = img1/255.0
img2 = img2/255.0
img3 = img3/255.0

np_img1 = np.expand_dims(img1, 0)
np_img2 = np.expand_dims(img2, 0)
np_img3 = np.expand_dims(img3, 0)

print ("image 1\n")
print(np_img1.shape)
predictions_single1 = probability_model.predict(np_img1)
print(predictions_single1)
plot_value_array(1, predictions_single1[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
print(np.argmax(predictions_single1[0]))
print("\n")

print ("image 2\n")
print(np_img2.shape)
predictions_single2 = probability_model.predict(np_img2)
print(predictions_single2)
plot_value_array(1, predictions_single2[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
print(np.argmax(predictions_single2[0]))
print("\n")

print ("image 3\n")
print(np_img3.shape)
predictions_single3 = probability_model.predict(np_img3)
print(predictions_single3)
plot_value_array(1, predictions_single3[0], test_labels)
_ = plt.xticks(range(10), class_names, rotation=45)
plt.show()
print(np.argmax(predictions_single3[0]))




