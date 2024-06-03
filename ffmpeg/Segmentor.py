import subprocess
import shlex
import sys

#extraction of audio from an mp4 file using ffmpeg :
input_AV_file = sys.argv[1]
output_aac_file = sys.argv[2]
output_segment_dir = sys.argv[3]

Audio_extract_command = "ffmpeg -i " + input_AV_file + " -vn -acodec copy tmp/" + output_segment_dir + "/audio-input.aac"
print("Audio_extract_command =>" + Audio_extract_command)

#Vocal from Audio:
Vocal_command = "ffmpeg -i tmp/" + output_segment_dir + "/audio-input.aac -af " + "\"" + "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn'"+ "\"" + " tmp/" + output_segment_dir + "/vocal-only.aac"
print("Vocal_command =>" + Vocal_command)

#Noise reduction:
Noise_red_command = "ffmpeg -i tmp/" + output_segment_dir + "/vocal-only.aac -af " + "\"" + "arnndn=m='rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn'"+ "\"" + " " + "tmp/" + output_segment_dir + "/" + output_aac_file
print("Noise_red_command =>" + Noise_red_command)

#10 sec segments :
audio_segment_dir = "Audio_Segment_" + output_segment_dir
Audio_segment_command = "ffmpeg -i tmp/" + output_segment_dir + "/audio-input.aac -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 tmp/" + audio_segment_dir + "/Aud_Segment_%d.aac"
print("Audio Segment Command =>" + Audio_segment_command)

#10 sec video segment
video_segment_dir = output_segment_dir +"/Video_Segment_" + output_segment_dir
Video_segment_command = "ffmpeg -i " + input_AV_file + " -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 tmp/" + video_segment_dir +"/AV_Segment_%d.mp4"
print("Video Segment Command =>" + Video_segment_command)

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

