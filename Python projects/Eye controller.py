#https://youtu.be/k3PcVruvZCs
import cv2  #Mediapipe is a cross-platform library developed by Google that provides amazing ready-to-use ML solutions for computer vision tasks. OpenCV library in python is a computer vision library that is widely used for image analysis, image processing, detection, recognition, etc.
import mediapipe as mp
import pyautogui #PyAutoGUI is a Python automation library used to click, drag, scroll, move, etc.
cam= cv2.VideoCapture(0)
face_mesh= mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)#for refined landmarks we use refine_landmarks
screen_w, screen_h= pyautogui.size() 
while True:
    _, frame= cam.read()
    frame=cv2.flip(frame, 1)#here 1 is for flipping vertically..we do flip to erase the mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#bgr to rgb
    output= face_mesh.process(rgb_frame)
    landmark_points= output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    if landmark_points:
        landmarks= landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):#focusing on eye by 474 475 476
            #enumerate gives us the index
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,225,0)) #to find the center...draw the circle on the frame so circle(frame)
            #(x,y) the center...3 is radius ..(0,225,0) color code for lime
            if id==1:
                screen_x= screen_w/frame_w*x 
                screen_y=screen_h/frame_h*y                  #another simple option= screen_x=int(landmark.x*screen_w)
                                                                      #screen_y= int(landmark.y*screen_h)
                pyautogui.moveTo(screen_x, screen_y)
        left=[landmarks[145], landmarks[159]]
         #eye blink detection landmark in opp eye      #two specific landmark
        for landmark in left:
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,225,225))
        if (left[0].y-left[1].y)<0.004:
            pyautogui.click() 
            pyautogui.sleep(1)
            
    cv2.imshow('Eye controlled mouse', frame)
    cv2.waitKey(1)
