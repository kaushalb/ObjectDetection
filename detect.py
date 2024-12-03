import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound
import os


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

output_dir = "./captured_frames"
os.makedirs(output_dir, exist_ok=True)

person_detected = False
frames_captured = 0
frames_to_capture = 20
image_set = []
person_counter = 0

while True:
    ret, frame = camera.read()
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    cv2.imshow("Object Detection", output_image)

    if "person" in label:
        person_counter += 1

    if "person" in label:
        if not person_detected:
            person_detected = True
            frames_captured = 0  # Reset frame counter

        # Capture frames if the "person" label is detected
        if frames_captured < frames_to_capture:
            image_set.append(frame)
            frame_filename = os.path.join(output_dir, f"person_{person_counter}_frame_{frames_captured + 1}.jpg")
            cv2.imwrite(frame_filename, frame)
            frames_captured += 1
        break
    else:
        person_detected = False

    for item in label:
        if item in items:
            pass
        else:
            items.append(item)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

print(image_set)
if len(image_set) >= 20:
    training_set = image_set[:10]
    target_set = image_set[10:20]


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

camera.release()
cv2.destroyAllWindows()