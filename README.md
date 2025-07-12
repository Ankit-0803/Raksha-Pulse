Empowering Rapid Disaster Detection, Response & Relief through Intelligence.

Raksha-Pulse is an AI-driven disaster management platform that supports government authorities and emergency responders across all stages of a natural or man-made crisis. From real-time detection to post-disaster recovery, the system integrates computer vision, clustering algorithms, and smart routing to ensure timely action and resource deployment.

🔁 System Capabilities
🔹 Pre-Disaster — Detection & Prediction
Utilizes Deep Learning (CNNs, VGG-16) on live CCTV feeds to detect disasters like floods and fires.

Predicts potential evacuation zones using impact analysis and population density data.

🔹 During Disaster — Alerts & Rescue Operations
Sends automated alerts to users (linked via Aadhaar, PAN, Aarogya Setu).

Identifies high-stress locations using DBSCAN clustering.

Optimizes rescue paths with GRASP & VND route planning algorithms.

🔹 Post-Disaster — Relief & Recovery
Plans road reconstructions dynamically using damage estimation.

Routes relief vehicles optimally based on updated real-time conditions.

🧠 Core Technologies
✅ CNNs & VGG-16 for real-time video-based disaster detection

✅ DBSCAN for hotspot identification

✅ GRASP + VND for route optimization

✅ Kubernetes + Django for scalable deployment

🔧 Modules Overview
🔥 Fire Detector
Place fire.model in the output/ folder.

Run predict_fire.py with the desired video file from videos/.

🌊 Flood Detector
Place flood.model in the output/ folder.

Run predict_flood.py with a video from the videos/ folder.

🧍‍♂️ Social Distance Detector
Copy yolov3.weights into Social-Disatance-Detector/yolo-coco/.

Enable GPU by setting USE_GPU = True in utils/social_distancing_config.py.

Run social_distance_detector.py with appropriate arguments.


