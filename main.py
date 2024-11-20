import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./audioOutputs/output.mp3")
    playsound("./audioOutputs/output.mp3")

camera = cv2.VideoCapture(0)
items = []

while True:
    ret, frame = camera.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)

    cv2.imshow("Object Detection", output_image)

    for item in label:
        if item in items:
            pass
        else:
            items.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
i = 0
audioQueue = []
for label in items:
    if i == 0:
        audioQueue.append(f"That is a {label}, and ")
    else:
        audioQueue.append(f"a {label}")
    i += 1

print(" ".join(audioQueue))