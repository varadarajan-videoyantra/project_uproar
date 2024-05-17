#extraction of audio from an mp4 file using ffmpeg : 
ffmpeg -i <path> -vn -acodec copy audio-input.aac

#Vocal from Audio:
ffmpeg -i audio-input.aac -af "arnndn=m='rnnoise-models/somnolent-hogwash-2018-09-01/sh.rnnn'" Fifa-vocal-only.aac

#Noise reduction:
ffmpeg -i Fifa-vocal-only.aac -af "arnndn=m='rnnoise-models/marathon-prescription-2018-08-29/mp.rnnn'" Fifa-vocal-noise-rem-only.aac

#10 sec segments : 

ffmpeg -i audio-input.aac -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 segment/output_time_%d.aac

#10 sec video segment
ffmpeg -i VFifo.mp4 -acodec copy -f segment -segment_time 10 -vcodec copy -reset_timestamps 1 -map 0 VSegments/output_time_%d.mp4


#Switching comma
ffmpeg -i output_time_0.mp4 -i output_time_2.mp4 -i output_time_3.mp4 -i output_time_4.mp4 -i output_time_5.mp4 -i output_time_13.mp4 -i output_time_14.mp4 -i output_time_15.mp4 -i output_time_17.mp4 -i output_time_20.mp4 -i output_time_21.mp4 -i output_time_23.mp4 -i output_time_31.mp4 -i output_time_35.mp4 -i output_time_36.mp4 -i output_time_37.mp4 -i output_time_38.mp4 -i output_time_43.mp4 -i output_time_48.mp4 -i output_time_50.mp4 -i output_time_53.mp4 -i output_time_54.mp4 -i output_time_56.mp4 -i output_time_67.mp4 -i output_time_71.mp4 -i output_time_74.mp4 -i output_time_77.mp4 -i output_time_78.mp4 -i output_time_81.mp4 -i output_time_84.mp4 -i output_time_89.mp4 -i output_time_90.mp4 -i output_time_92.mp4 -i output_time_94.mp4 -i output_time_98.mp4 -i output_time_105.mp4 -i output_time_106.mp4 -i output_time_107.mp4 -i output_time_108.mp4 -i output_time_111.mp4 -i output_time_114.mp4 -i output_time_116.mp4 -i output_time_117.mp4 -i output_time_130.mp4 -i output_time_132.mp4 -i output_time_135.mp4 -i output_time_136.mp4 -i output_time_138.mp4 -i output_time_139.mp4 -i output_time_140.mp4 -i output_time_141.mp4 -i output_time_142.mp4 -i output_time_143.mp4 -i output_time_147.mp4 -i output_time_148.mp4 -filter_complex  "[0:0][0:1][1:0][1:1][2:0][2:1][3:0][3:1][4:0][4:1][5:0][5:1][6:0][6:1][7:0][7:1][8:0][8:1][9:0][9:1][10:0][10:1][11:0][11:1][12:0][12:1][13:0][13:1][14:0][14:1][15:0][15:1][16:0][16:1][17:0][17:1][18:0][18:1][19:0][19:1][20:0][20:1][21:0][21:1][22:0][22:1][23:0][23:1][24:0][24:1][25:0][25:1][26:0][26:1][27:0][27:1][28:0][28:1][29:0][29:1][30:0][30:1][31:0][31:1][32:0][32:1][33:0][33:1][34:0][34:1][35:0][35:1][36:0][36:1][37:0][37:1][38:0][38:1][39:0][39:1][40:0][40:1][41:0][41:1][42:0][42:1][43:0][43:1][44:0][44:1][45:0][45:1][46:0][46:1][47:0][47:1][48:0][48:1][49:0][49:1][50:0][50:1][51:0][51:1][52:0][52:1][53:0][53:1][54:0][54:1]concat=n=55:a=1[outv][outa]" -map "[outv]" -map "[outa]"  output.mp4