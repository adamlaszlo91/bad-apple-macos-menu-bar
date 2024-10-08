import cv2 as cv
import time
import imutils
import rumps
from threading import Thread

video_path = 'video/bad_apple.mp4'
app = rumps.App("")


def play_video() -> None:
    cap = cv.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.release()
            rumps.quit_application()
            return

        # Threshold the image then make the background transparent
        image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        image = imutils.resize(image, height=18)
        _, image = cv.threshold(src=image, thresh=127, maxval=255, type=cv.THRESH_BINARY)
        image = cv.merge([image.copy(), image.copy(), image.copy(), image.copy()],4)
        
        # Write image to file, as rumps currently accepts only an image path
        cv.imwrite(img= image, filename= 'frame.png')
        app.icon = 'frame.png'
        time.sleep(0.04)

if __name__ == '__main__':
    thread = Thread(target = play_video)
    thread.start()
    app.run()
