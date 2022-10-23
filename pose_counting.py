import cv2
import mediapipe as mp

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
left = False
counter = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1280,720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    #print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        points = {}
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            points[id] = cx, cy

        cv2.circle(img, points[14], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[16], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[13], 15, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[15], 15, (255,0,0), cv2.FILLED)
        
        if not left and points[16][0] + 30 <points[14][0]:
            print('left')  
            left = True
            counter += 1
        elif points[16][0]>points[14][0]:
            print('right')
            left = False
        
        #print('.....................', counter)
    cv2.putText(img, str(counter), (100,150), cv2.FONT_HERSHEY_PLAIN, 14, (255,0,0), 14)
    cv2.imshow("img", img)
    cv2.waitKey(10)