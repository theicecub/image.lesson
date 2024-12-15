import cv2 #open cv библиотека для работы с изображениями 

image_path = 'cat.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Файл cat не найден")

cv2.imshow('Cat', image)
cv2.waitKey() #команда, которая ждет пока мы не нажмем на кнопку

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

if cat_face_cascade.empty():
    raise FileNotFoundError("Файл haarcascade_frontalcatface не найден")

cat_faces = cat_face_cascade.detectMultiScale(gray_image)
print("Координаты мордочек:", cat_faces)

for(x, y, w, h) in cat_faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("Прямоугольник", image)
cv2.waitKey()

from PIL import Image
cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')

for(x, y, w, h) in cat_faces:
    glasses_recised = glasses.resize((w, int(h/3)))
    cat.paste(glasses_recised, (x, y + int(h/4)), glasses_recised)

ouput_path="cat_with_glasses.png"
cat.save(ouput_path)

result = cv2.imread("cat_with_glasses.png")
cv2.imshow("Cat with glasses", result)
cv2.waitKey()