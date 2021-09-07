import face_recognition
import cv2
#face=["top","right","bottom","left"]
def blurFaces(img):
    kwidth=23
    kheight=23
    faces=face_recognition.face_locations(img)#top right bottom left
    for face in faces:
        croppedImg=img[face[0]:face[2],face[3]:face[1]]
        blurImg=cv2.blur(croppedImg,(kwidth,kheight))
        img[face[0]:face[2],face[3]:face[1]]=blurImg
    return img
