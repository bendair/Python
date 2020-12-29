import numpy
#from cv2 import cv2
import cv2

frameWidth = 960
frameHeight = 540

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[7]

############### Tracker Types #####################

#tracker = cv2.TrackerBoosting_create() #not very good
#tracker = cv2.TrackerMIL_create() #not very good
#tracker = cv2.TrackerKCF_create() #not very good
#tracker = cv2.TrackerTLD_create() #Really slow
#tracker = cv2.TrackerMedianFlow_create() #Interesting bbox resizing
#tracker = cv2.TrackerCSRT_create() #slower but more accurate
#tracker = cv2.TrackerMOSSE_create() #Ok, but can get distracted

########################################################

def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img,(x, y),((x+w),(y+h)),(0,255,255),2,1)

    cv2.putText(img, "Tracking", (75,75), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0), 2)

def CreateTracker(trackertype):
    if trackertype == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if trackertype == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if trackertype == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if trackertype == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if trackertype == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if trackertype == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    if trackertype == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if trackertype == "CSRT":
        tracker = cv2.TrackerCSRT_create()

    return tracker   

tracker = CreateTracker(tracker_type)
success, img = cap.read()
img = cv2.resize(img, (frameWidth, frameHeight))

bbox = cv2.selectROI("Tracking",img, False)
tracker.init(img,bbox)

while True:
    timer = cv2.getTickCount()
    #print(bbox, "Pre-Capture Read")
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))

    #print(bbox, "Post-Capture Read")
    success, bbox = tracker.update(img)
    #print(bbox, " After Tracker Update")

    if success: 
        drawBox(img,bbox)
    else:
        cv2.putText(img, "Lost", (75,75), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255), 2)
   
    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img, str(int(fps)), (75,50), cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255), 2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xff == ord('n'):
        #print(bbox, " Pre-bbox delete")
        del bbox
        tracker = CreateTracker(tracker_type)
        success, img = cap.read()
        img = cv2.resize(img, (frameWidth, frameHeight))

        bbox = cv2.selectROI("Tracking",img, False)
        #print(bbox, " Post-bbox delete")
        tracker.init(img,bbox)
        #print(bbox, " Post tracker initialise")
        print(bbox, " Created new tracker")

    if cv2.waitKey(1) & 0xff == ord('q'):
        print("Exiting Application!!")
        break

    