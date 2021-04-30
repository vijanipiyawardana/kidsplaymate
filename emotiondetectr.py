import cv2
from deepface import DeepFace
import time
#import matplotlib.pyplot as plt 

start = time.time()

img = cv2.imread('images/img144.jpg')
#plt.imshow(img)

predictions = DeepFace.analyze(img, actions=['emotion'])
#print(predictions)
print(predictions['dominant_emotion'])

end = time.time()

print(end - start)


