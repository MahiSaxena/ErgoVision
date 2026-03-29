import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_drawing = mp.solutions.drawing_utils

def calculate_angle(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c

    angle = math.degrees(
        math.atan2(cy - by, cx - bx) -
        math.atan2(ay - by, ax - bx)
    )

    angle = abs(angle)

    if angle > 180:
        angle = 360 - angle

    return angle

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:

            landmarks = results.pose_landmarks.landmark
            height, width, _ = frame.shape

            left_ear = [
                landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x * width,
                landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y * height
            ]

            left_shoulder = [
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x * width,
                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y * height
            ]

            left_hip = [
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x * width,
                landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y * height
            ]

            neck_angle = calculate_angle(left_ear, left_shoulder, left_hip)

            GOOD_POSTURE_THRESHOLD = 145

            if neck_angle > GOOD_POSTURE_THRESHOLD:
                status = "GOOD POSTURE"
                color = (0, 255, 0)
            else:
                status = "SLOUCHING - SIT UP!"
                color = (0, 0, 255)

            cv2.line(frame,
                    (int(left_shoulder[0]), int(left_shoulder[1])),
                    (int(left_ear[0]), int(left_ear[1])),
                    color, 4)

            cv2.circle(frame,
                        (int(left_ear[0]), int(left_ear[1])),
                        8, color, -1)

            cv2.circle(frame,
                        (int(left_shoulder[0]), int(left_shoulder[1])),
                        8, color, -1)
            
            cv2.putText(frame, status,
                        (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        color,
                        3)
            
            cv2.putText(frame,
                        f"Neck Angle: {int(neck_angle)}",
                        (20, 90),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (255, 255, 255),
                        2)
            
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

        cv2.imshow("ErgoVision", frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()