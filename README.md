# AI Based Disaster Relief and Management System

🔍 Summary of DRAMS (Disaster Relief and Management System)
DRAMS is an AI-powered decision support system designed to optimize disaster response operations during all phases of a natural calamity:

1️⃣ Pre-Disaster (Detection & Prediction)

Uses Deep Learning (CNNs) and CCTV footage to detect disasters in real-time.
Predicts evacuation zones based on impact estimates & population clusters.
2️⃣ During Disaster (Alert & Rescue Operations)

Sends real-time alerts to affected users via Aadhaar, PAN & Aarogya Setu.
Uses DBSCAN clustering to identify high-distress areas.
Computes optimal rescue routes using GRASP & VND algorithms.
3️⃣ Post-Disaster (Relief & Recovery)

Restores connectivity by planning road reconstruction based on real-time data.
Deploys relief vehicles efficiently using AI-based routing algorithms.
🚀 Key Technologies Used:
✅ Deep Learning (CNNs, VGG-16) for disaster detection.
✅ DBSCAN clustering for identifying high-risk zones.
✅ GRASP & VND routing algorithms for optimized vehicle deployment.
✅ Kubernetes & Django for scalable system deployment.

🌍 Real-World Use Cases:
✔️ Flash Floods – Real-time tracking & evacuation planning.
✔️ COVID-19 Prevention – Crowd detection & social distancing enforcement.
✔️ City Fires – Automated alerts & rescue coordination.



## Model Trained files
https://drive.google.com/drive/folders/15Vjd-xRUxw0oky-7bXOGojqHF8vV-BLg?usp=sharing



## City-Fire Detector
Download the fire.model from the above drive link and add it in the output folder. \
To check its working run the predict_fire.py from command line with the required arguments ( Commented at the beginning of the .py file ). \
Input video can be taken from the videos folder by videos/( any fire video.mp4).


## Flood-Detector
Download the flood.model from the above drive link and add it in the output folder. \
To check its working run the predict_flood.py from command line with the required arguments ( Commented at the beginning of the .py file ). \
Input video can be taken from the videos folder by videos/(any flood video.mp4).

## Social-Distance-Detector
Copy the yolov3.weights file from the above drive link and paste in Social-Disatance-Detector/yolo-coco/ \
For Using GPU - Go to Social-Disatance-Detector/utils/social_distancing_config.py and change USE_GPU to True
Run the social_distance_detector.py from command line with the required arguments ( Commented at begining of .py file) 




