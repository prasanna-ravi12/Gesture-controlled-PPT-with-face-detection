# # import cv2
# # import numpy as np
# # import os
# # import time
# #
# # def create_database():
# #     count = 0
# #     size = 4
# #     fn_haar = 'haarcascade_frontalface_default.xml'
# #     fn_dir = 'database'
# #
# #     # Ask for the number of persons
# #     print("-------------DIVE INTO THE WORLD OG GESTURE POWERED PRESENTATION-------------")
# #     num_persons = int(input("Enter number of persons: "))
# #
# #     # Create database folder if not exists
# #     if not os.path.isdir(fn_dir):
# #         os.mkdir(fn_dir)
# #
# #     for _ in range(num_persons):
# #         fn_name = input("Enter the person's name: ")
# #         path = os.path.join(fn_dir, fn_name)
# #         if not os.path.isdir(path):
# #             os.mkdir(path)
# #
# #         (im_width, im_height) = (112, 92)
# #         haar_cascade = cv2.CascadeClassifier(fn_haar)
# #         webcam = cv2.VideoCapture(0)
# #
# #         print(f"-----------------------Taking pictures for {fn_name}----------------------")
# #         print("--------------------DAZZLE WITH THE MAGIC OF YOUR EXPRESSIONS---------------------")
# #
# #         while count < 45:
# #             (rval, im) = webcam.read()
# #             im = cv2.flip(im, 1, 0)
# #             gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# #             # Applying histogram equalization to improve contrast
# #             gray = cv2.equalizeHist(gray)
# #             mini = cv2.resize(gray, (gray.shape[1] // size, gray.shape[0] // size))
# #             faces = haar_cascade.detectMultiScale(mini, scaleFactor=1.2, minNeighbors=5)
# #             faces = sorted(faces, key=lambda x: x[3])
# #             if faces:
# #                 face_i = faces[0]
# #                 (x, y, w, h) = [v * size for v in face_i]
# #                 face = gray[y:y + h, x:x + w]
# #                 face_resize = cv2.resize(face, (im_width, im_height))
# #                 pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path) if n[0] != '.'] + [0])[-1] + 1
# #                 cv2.imwrite(f'{path}/{pin}.png', face_resize)
# #                 cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
# #                 cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
# #                 count += 1
# #             cv2.imshow('OpenCV', im)
# #             key = cv2.waitKey(10)
# #             if key == 27:
# #                 break
# #         print(str(count) + f" images taken and saved to {fn_name} folder in database ")
# #         count = 0
# #
# # create_database()
# #
# # print('Training...')
# # # Create a list of images and a list of corresponding names
# # (images, labels, names, id) = ([], [], {}, 0)
# # for (subdirs, dirs, files) in os.walk('database'):
# #     for subdir in dirs:
# #         names[id] = subdir
# #         subjectpath = os.path.join('database', subdir)
# #         for filename in os.listdir(subjectpath):
# #             path = os.path.join(subjectpath, filename)
# #             label = id
# #             images.append(cv2.imread(path, 0))
# #             labels.append(int(label))
# #         id += 1
# #
# # (width, height) = (130, 100)
# #
# # # Create a Numpy array from the two lists above
# # (images, labels) = [np.array(lst) for lst in [images, labels]]
# #
# # # OpenCV trains a model from the images
# # model = cv2.face.LBPHFaceRecognizer_create()
# # model.train(images, labels)
# #
# # haar_file = 'haarcascade_frontalface_default.xml'  # Define haar cascade file
# # face_cascade = cv2.CascadeClassifier(haar_file)
# # webcam = cv2.VideoCapture(0)
# #
# # # Delay for 5 seconds
# # print("Delaying for 5 seconds before starting live feed...")
# # time.sleep(5)
# #
# # access_granted = False
# #
# # while not access_granted:
# #     _, im = webcam.read()
# #     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# #     # Applying histogram equalization to improve contrast
# #     gray = cv2.equalizeHist(gray)
# #     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
# #     for (x, y, w, h) in faces:
# #         cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
# #         face = gray[y:y + h, x:x + w]
# #         face_resize = cv2.resize(face, (width, height))
# #
# #         # Try to recognize the face
# #         prediction = model.predict(face_resize)
# #         print('------s', prediction)
# #         confidence = int(prediction[1])
# #         if confidence < 100:  # Adjust this threshold as needed
# #             recognized_name = names[prediction[0]]
# #             cv2.putText(im, recognized_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
# #             print("Access Granted")
# #             access_granted = True
# #             os.system("python HAND_GESTURE.py")  # Modified this line
# #         else:
# #             confidence = 100 - confidence  # converting to a confidence level
# #             cv2.putText(im, 'Unknown', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
# #             cv2.putText(im, f'Confidence: {confidence}%', (x - 10, y + h + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
# #             print(f"Unknown face with confidence: {confidence}%")
# #             print("Access Denied")
# #             access_granted = True
# #
# #     cv2.imshow('OpenCV', im)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # webcam.release()
# # cv2.destroyAllWindows()
#
#
# import cv2
# import numpy as np
# import os
# import time
#
# def create_database():
#     count = 0
#     size = 4
#     fn_haar = 'haarcascade_frontalface_default.xml'
#     fn_dir = 'database'
#
#     # Ask for the number of persons
#     num_persons = int(input("Enter number of persons: "))
#
#     # Create database folder if not exists
#     if not os.path.isdir(fn_dir):
#         os.mkdir(fn_dir)
#
#     for _ in range(num_persons):
#         fn_name = input("Enter the person's name: ")
#         path = os.path.join(fn_dir, fn_name)
#         if not os.path.isdir(path):
#             os.mkdir(path)
#
#         (im_width, im_height) = (112, 92)
#         haar_cascade = cv2.CascadeClassifier(fn_haar)
#         webcam = cv2.VideoCapture(0)
#
#         print(f"-----------------------Taking pictures for {fn_name}----------------------")
#         print("--------------------Give some expressions---------------------")
#
#         while count < 45:
#             (rval, im) = webcam.read()
#             im = cv2.flip(im, 1, 0)
#             gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#             # Applying histogram equalization to improve contrast
#             gray = cv2.equalizeHist(gray)
#             mini = cv2.resize(gray, (gray.shape[1] // size, gray.shape[0] // size))
#             faces = haar_cascade.detectMultiScale(mini, scaleFactor=1.2, minNeighbors=5)
#             faces = sorted(faces, key=lambda x: x[3])
#             if faces:
#                 face_i = faces[0]
#                 (x, y, w, h) = [v * size for v in face_i]
#                 face = gray[y:y + h, x:x + w]
#                 face_resize = cv2.resize(face, (im_width, im_height))
#                 pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path) if n[0] != '.'] + [0])[-1] + 1
#                 cv2.imwrite(f'{path}/{pin}.png', face_resize)
#                 cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
#                 cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
#                 count += 1
#             cv2.imshow('OpenCV', im)
#             key = cv2.waitKey(10)
#             if key == 27:
#                 break
#         print(str(count) + f" images taken and saved to {fn_name} folder in database ")
#         count = 0
#
# create_database()
#
# print('Training...')
# # Create a list of images and a list of corresponding names
# (images, labels, names, id) = ([], [], {}, 0)
# for (subdirs, dirs, files) in os.walk('database'):
#     for subdir in dirs:
#         names[id] = subdir
#         subjectpath = os.path.join('database', subdir)
#         for filename in os.listdir(subjectpath):
#             path = os.path.join(subjectpath, filename)
#             label = id
#             images.append(cv2.imread(path, 0))
#             labels.append(int(label))
#         id += 1
#
# (width, height) = (130, 100)
#
# # Create a Numpy array from the two lists above
# (images, labels) = [np.array(lst) for lst in [images, labels]]
#
# # OpenCV trains a model from the images
# model = cv2.face.LBPHFaceRecognizer_create()
# model.train(images, labels)
#
# haar_file = 'haarcascade_frontalface_default.xml'  # Define haar cascade file
# face_cascade = cv2.CascadeClassifier(haar_file)
# webcam = cv2.VideoCapture(0)
#
# # Delay for 5 seconds
# print("Delaying for 5 seconds before starting live feed...")
# time.sleep(5)
#
# access_granted = False
#
# while not access_granted:
#     _, im = webcam.read()
#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     # Applying histogram equalization to improve contrast
#     gray = cv2.equalizeHist(gray)
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         face = gray[y:y + h, x:x + w]
#         face_resize = cv2.resize(face, (width, height))
#
#         # Try to recognize the face
#         prediction = model.predict(face_resize)
#         print('------s', prediction)
#         confidence = int(prediction[1])
#         if confidence < 100:  # Adjust this threshold as needed
#             recognized_name = names[prediction[0]]
#             cv2.putText(im, recognized_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
#             print("Access Granted")
#             access_granted = True
#             os.system("python HAND_GESTURE.py")  # Modified this line
#         else:
#             confidence = 100 - confidence  # converting to a confidence level
#             cv2.putText(im, 'Unknown', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
#             cv2.putText(im, f'Confidence: {confidence}%', (x - 10, y + h + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
#             print(f"Unknown face with confidence: {confidence}%")
#             print("Access Denied")
#             access_granted = True
#
#     cv2.imshow('OpenCV', im)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# webcam.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np
import os
import time

def create_database():
    count = 0
    size = 4
    fn_haar = 'haarcascade_frontalface_default.xml'
    fn_dir = 'database'

    # Ask for the number of persons
    print("------------DIVE INTO THE WORLD OG GESTURE POWERED PRESENTATION-------------")
    num_persons = int(input("Enter number of persons: "))

    # Create database folder if not exists
    if not os.path.isdir(fn_dir):
        os.mkdir(fn_dir)

    for _ in range(num_persons):
        fn_name = input("Enter the person's name: ")
        path = os.path.join(fn_dir, fn_name)
        if not os.path.isdir(path):
            os.mkdir(path)

        (im_width, im_height) = (112, 92)
        haar_cascade = cv2.CascadeClassifier(fn_haar)
        webcam = cv2.VideoCapture(0)

        print(f"-----------------------Taking pictures for {fn_name}----------------------")
        print("-------------------DAZZLE WITH THE MAGIC OF YOUR EXPRESSIONS---------------------")

        while count < 45:
            (rval, im) = webcam.read()
            im = cv2.flip(im, 1, 0)
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            # Applying histogram equalization to improve contrast
            gray = cv2.equalizeHist(gray)
            mini = cv2.resize(gray, (gray.shape[1] // size, gray.shape[0] // size))
            faces = haar_cascade.detectMultiScale(mini, scaleFactor=1.2, minNeighbors=5)
            faces = sorted(faces, key=lambda x: x[3])
            if faces:
                face_i = faces[0]
                (x, y, w, h) = [v * size for v in face_i]
                face = gray[y:y + h, x:x + w]
                face_resize = cv2.resize(face, (im_width, im_height))
                pin = sorted([int(n[:n.find('.')]) for n in os.listdir(path) if n[0] != '.'] + [0])[-1] + 1
                cv2.imwrite(f'{path}/{pin}.png', face_resize)
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 255, 0), 3)
                cv2.putText(im, fn_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
                count += 1
            cv2.imshow('OpenCV', im)
            key = cv2.waitKey(10)
            if key == 27:
                break
        print(str(count) + f" images taken and saved to {fn_name} folder in database ")
        count = 0

create_database()

print('Training...')
# Create a list of images and a list of corresponding names
(images, labels, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk('database'):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join('database', subdir)
        for filename in os.listdir(subjectpath):
            path = os.path.join(subjectpath, filename)
            label = id
            images.append(cv2.imread(path, 0))
            labels.append(int(label))
        id += 1

(width, height) = (130, 100)

# Create a Numpy array from the two lists above
(images, labels) = [np.array(lst) for lst in [images, labels]]

# OpenCV trains a model from the images
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

haar_file = 'haarcascade_frontalface_default.xml'  # Define haar cascade file
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

# Delay for 5 seconds
print("Delaying for 5 seconds before starting live feed...")
time.sleep(5)

access_granted = False

while not access_granted:
    _, im = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Applying histogram equalization to improve contrast
    gray = cv2.equalizeHist(gray)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))

        # Try to recognize the face
        prediction = model.predict(face_resize)
        print('------s', prediction)
        confidence = int(prediction[1])
        if confidence < 100:  # Adjust this threshold as needed
            recognized_name = names[prediction[0]]
            cv2.putText(im, recognized_name, (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            print("Access Granted")
            access_granted = True
            os.system("python HAND_GESTURE.py")  # Modified this line
        else:
            confidence = 100 - confidence  # converting to a confidence level
            cv2.putText(im, 'Unknown', (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            cv2.putText(im, f'Confidence: {confidence}%', (x - 10, y + h + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))
            print(f"Unknown face with confidence: {confidence}%")
            print("Access Denied")

    cv2.imshow('OpenCV', im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
