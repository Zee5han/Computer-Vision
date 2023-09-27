import cv2

# Specify the video file path
video_path = 'test.AVI'
output_path = "Output"

# Specify the time interval between frames in milliseconds (e.g., 1000ms = 1 second)
time_interval_ms = 1000  # Change this value to your desired interval

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Error: Could not open video file")
    exit()

# Set the video's frame rate (this may vary depending on the video)
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the frame capture interval based on the time interval
capture_interval = int(frame_rate * (time_interval_ms / 1000.0))

# Initialize a frame counter
frame_count = 0

# Loop to extract frames based on the specified time interval
while True:
    ret, frame = cap.read()

    # Break the loop if the video is finished
    if not ret:
        break

    # Save the frame to a file (you can customize the file naming)
    frame_filename = f'{output_path}/frame_{frame_count:04d}.jpg'
    cv2.imwrite(frame_filename, frame)

    # Increment the frame counter
    frame_count += 1

    # Skip frames according to the capture interval
    for _ in range(capture_interval - 1):
        cap.read()

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()

print(f"Extracted {frame_count} frames with a time interval of {time_interval_ms} milliseconds between frames.")
