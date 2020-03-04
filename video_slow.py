import cv2

fileName=input("Enter the file name \n")     
slomo_frame = int(input("Enter the frames you want to change to \n"))  
cap = cv2.VideoCapture(fileName)       # load the video
while(cap.isOpened()):                    # play the video by reading frame by frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1500, 1000))
    if ret==True:
        cv2.imshow('frame',frame)              # show the video
        cv2.waitKey(slomo_frame)
        if 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()