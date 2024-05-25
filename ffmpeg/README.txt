Prereqsuite : insatll ffmpeg package and add it to the system environament.
1. Copy the source Video file in the directoty
2. Execute the Segmentor.py file using : python Segmentor.py <inpu file name{coped in Step1}>
3. Run the prediction. keep in generated csv file in the same folder. Keep the coulmn name same as one added sample csv commited in GIT repo.
   Any change in column name will have code change
4. Execute the Highlight_Generator.py  using : python Highlight_Generator.py

Note: once the step 2 is executed all segmented audio file will be present in Audio_Segment folder which can be used for MEL Spectograph analysis.
