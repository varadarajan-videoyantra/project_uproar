Prereqsuite : insatll ffmpeg package and add it to the system environament.
1. Copy the source Video file in the directoty
2. Execute the Segmentor.py file using : python Segmentor.py <inpu file name{coped in Step1}>
3. Run the prediction. keep in generated csv file in the same folder. Keep the coulmn name same as one added sample csv commited in GIT repo.
   Any change in column name will have code change
4. Execute the Highlight_Generator.py  using : python Highlight_Generator.py

Note: once the step 2 is executed all segmented audio file will be present in Audio_Segment folder which can be used for MEL Spectograph analysis.
      link to ffmpeg : https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/

This code has been setup in 2 IDEs, Pycharm for the ffmpeg related code, as well as VSCode for the jupiter notebook.
Pycharm has been configured in 3 different ways
1. Segmentor_train_test - This is to prepare the audio segments to generate melspectorgram for training.
This runs segmentor.py with the following arguments - <Path to VFifa_original.mp4> vocal-noise-rem-only.aac
2. Segmentor_serve - This is to prepare the audio segments to generate melspectorgram for prediction.
This runs segmentor.py with the following arguments - <Path to Fifa-World_trimmed.mp4> vocal-noise-rem-only.aac.
Fifa-World_trimmed.mp4 is the File we will predict highlights.
3. Highlight_generator_serve - This is to stitch the video based on prediction_served.csv.
This runs Highlight+generator.py with <path to prediction_serving.csv> highlights_served.mp4 serve
python.exe Highlight_Generator.py <path to prediction_serving.csv> highlights_served.mp4 serve



python.exe D:/projects/jitheesh/project_uproar/ffmpeg/Highlight_Generator.py ..\prediction_serving.csv highlights_served.mp4 serve
