import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


def speech(text):
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output_path = "./audioOutputs/output.mp3"
    try:
        output.save(output_path)
        playsound(output_path)
    except FileNotFoundError:
        print("File does not exist")
        playsound("No sound to play")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Could not open computer camera")
    exit()

items = []

# while camera.isOpened():
#     ret, frame = camera.read()
#     face, confidence = cv.detect_face(frame)
#
#     # loop through detected faces
#     for idx, f in enumerate(face):
#         (startX, startY) = f[0], f[1]
#         (endX, endY) = f[2], f[3]
#
#         # draw rectangle over face
#         cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
#
#         text = "{:.2f}%".format(confidence[idx] * 100)
#
#         Y = startY - 10 if startY - 10 > 10 else startY + 10
#
#         # write confidence percentage on top of face rectangle
#         cv2.putText(frame, text, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
#                     (0, 255, 0), 2)
#
#     # display output
#     cv2.imshow("Real-time face detection", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

while True:
    ret, frame = camera.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    faces, confidences = cv.detect_face(output_image)
    if faces:
        print("your face", faces)
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

speech_text = " ".join(audioQueue)
print(speech_text)
speech(speech_text)