import cv2
import mediapipe as mp

# Initialize mediapipe pose class.
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
# Setup the Pose function for videos - for video processing.
pose = mpPose.Pose()
cap = cv2.VideoCapture('B.mp4')
count = 0
left = False
def detectpose(results, count):
    #print(results.pose_landmarks)
    global left
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        points = {}
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x*w), int(lm.y*h)
            points[id] = cx, cy

        cv2.circle(img, points[14], 14, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[16], 14, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[13], 14, (255,0,0), cv2.FILLED)
        cv2.circle(img, points[15], 14, (255,0,0), cv2.FILLED)
        
        if not left and points[14][0]+30<points[16][0]:
            print('left') 
            left = True
            count += 1
        elif points[14][0]>points[16][0]:
            print('right')
            left = False
    return count

# Initialize mediapipe drawing class - to draw the landmarks points.
while True:
    success, img = cap.read()
    if not img:
        break 
    img = cv2.resize(img, (1280,720))
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    count = detectpose(results, count)
    cv2.putText(img, str(count-1), (100,150), cv2.FONT_HERSHEY_PLAIN, 14, (255,0,0), 14)
    cv2.imshow("img", img)
    cv2.waitKey(10)