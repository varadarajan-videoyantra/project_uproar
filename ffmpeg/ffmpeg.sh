#extraction of audio from an mp4 file using ffmpeg : 
ffmpeg -i <path> -vn -acodec copy audio-input.aac

#Vocal from Audio:
ffmpeg -i audio-input.aac -af "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn'" Fifa-vocal-only.aac

#Noise reduction:
ffmpeg -i Fifa-vocal-only.aac -af "arnndn=m='rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn'" Fifa-vocal-noise-rem-only.aac

#10 sec segments : 

ffmpeg -i audio-input.aac -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 segment/output_time_%d.aac