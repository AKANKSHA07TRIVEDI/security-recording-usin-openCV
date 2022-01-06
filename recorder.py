import cv2
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')


def recordVideo(filename, config):
  out = cv2.VideoWriter(f'recordedVideos/{filename}.mp4', fourcc, config.get('fps'), (640, 480))

  while True:
    ret,frame = cap.read()

    cv2.imshow('Recording Video', frame)
    out.write(frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

  cv2.destroyAllWindows()
  cap.release()
  out.release()