from main import *
import cv2
new_model = load_model('brailledetect2.h5',
                                   compile=False)

# Starts camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    # clips out frame 
    frame = frame[50:500, 50:500, :]


    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # resizes image 
    resized = tf.image.resize(rgb, (120, 120))
    print(type(frame))
    # saves the classification and regression prediction to yhat
    yhat = new_model.predict(np.expand_dims(resized / 255, 0))
    ans = round(yhat[0][0][0] * 100, 2)
    # getting the bounding box coordinates
    sample_coords = yhat[1][0]

    if yhat[0] > 0.5:
        # Controls the bbox main label rectangle
        cv2.rectangle(frame,
                      tuple(np.multiply(sample_coords[:2], [450, 450]).astype(int)),
                      tuple(np.multiply(sample_coords[2:], [450, 450]).astype(int)),
                      (255, 0, 0), 2)
        
        # Controls the labeling rectangle
        cv2.rectangle(frame,
                      tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                   [0, -30])),
                      tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                   [80, 0])),
                      (255, 0, 0), -1)

        # Controls the rendered text 
        cv2.putText(frame, f'braille', tuple(np.add(np.multiply(sample_coords[:2], [450, 450]).astype(int),
                                                [0, -5])),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f'confidence: {ans} %',
                    tuple(np.add(np.multiply(sample_coords[:2], [450, 350]).astype(int),
                                 [0, -5])),
                    cv2.FONT_HERSHEY_SIMPLEX, .7, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('Braille Detect', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()