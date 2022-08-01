import cv2

img = cv2.imread("images/solar-system.jpg")
print(img)

sunText = "Sun"
mercuryText = "Mercury"
venuseText = "Venuse"
earthText = "Earth"
marsText = "Mars"
jupiterText = "Jupiter"
saturnText = "Saturn"
uranusText = "Uranus"
neptuneText = "Neptune"

# Sun
cv2.putText(img,sunText,(110,100),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=1.7,color=(0,0,255))

# Mercury
cv2.putText(img,mercuryText,(122,245),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.4,color=(255,255,255))

# Venuse
cv2.putText(img,venuseText,(185,260),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.55,color=(255,255,255))

# Earth
cv2.putText(img,earthText,(280,270),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=(255,255,255))

# Mars
cv2.putText(img,marsText,(375,260),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))

# Jupitor
cv2.putText(img,jupiterText,(560,380),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))

# Saturn
cv2.putText(img,saturnText,(760,310),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))

# Uranus
cv2.putText(img,uranusText,(960,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.8,color=(255,255,255))

# Neptune
cv2.putText(img,neptuneText,(1100,290),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=0.7,color=(255,255,255))

cv2.imshow("New Window",img)
cv2.waitKey(0)

cv2.imwrite("images/solar-system1.jpg",img)