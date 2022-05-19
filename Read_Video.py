import cv2

#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if(vid.isOpened()==False):
    print("unable to capture the video")
    



height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))

fps = int(vid.get(cv2.CAP_PROP_FPS))

print(height)
print(width)
print(fps)

boxing = cv2.VideoWriter("class105",cv2.VideoWriter_fourcc(*'DIVX'),fps,(width,height))

while (True):
    
    ret,frame = vid.read()
    cv2.imshow("Web cam" , frame)
    boxing.write(frame)
    if cv2.waitKey(fps) == 32:
        break
    
vid.release()
boxing.release()

cv2.destroyAllWindows()