import cv2
img=cv2.imread("solar-system.jpg")
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.putText(img,
            "Sun",
             (20,300),
             cv2.FONT_HERSEY_COMPLEX,
             0.5,
             (255,255,255)
             )
cv2.putText(img,
            "mercury",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "venus",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "Earth",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "mars",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "jupiter",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "saturn",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "uranus",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.putText(img,
            "neptune",
             (20,250),
             cv2.TIMES_NEW_ROMAN,
             0.5,
             (0,150,255)
             )
cv2.imwrite(“Solar_system.jpg”,img)
