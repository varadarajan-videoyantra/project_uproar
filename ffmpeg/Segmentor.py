import subprocess
import shlex
import sys

#extraction of audio from an mp4 file using ffmpeg :
input_AV_file = sys.argv[1]

Audio_extract_command = "ffmpeg -i " + input_AV_file + " -vn -acodec copy audio-input.aac"

#Vocal from Audio:
Vocal_command = "ffmpeg -i audio-input.aac -af " + "\"" + "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn'"+ "\"" + " vocal-only.aac"

#Noise reduction:
Noise_red_command = "ffmpeg -i vocal-only.aac -af " + "\"" + "arnndn=m='rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn'"+ "\"" + " vocal-noise-rem-only.aac"

#10 sec segments :

Audio_segment_command = "mkdir Audio_Segment && ffmpeg -i audio-input.aac -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 Audio_Segment/Aud_Segment_%d.aac"

#10 sec video segment
Video_segment_command = "mkdir Video_Segments && ffmpeg -i " + input_AV_file + " -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 Video_Segments/AV_Segment_%d.mp4"

process = subprocess.Popen(Audio_extract_command, shell=True, stdout=subprocess.PIPE)
process.wait()

process = subprocess.Popen(Vocal_command, shell=True, stdout=subprocess.PIPE)
process.wait()

process = subprocess.Popen(Noise_red_command, shell=True, stdout=subprocess.PIPE)
process.wait()

process = subprocess.Popen(Audio_segment_command, shell=True, stdout=subprocess.PIPE)
process.wait()

process = subprocess.Popen(Video_segment_command, shell=True, stdout=subprocess.PIPE)
process.wait()

