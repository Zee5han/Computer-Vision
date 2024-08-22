from moviepy.editor import VideoFileClip, concatenate_videoclips


clip_1 = VideoFileClip("/media/cle-184/CLE/RELEASES/RELEASE 2 - Dec-Feb/3.Data Annotation/Annotated-Data/V0351_H/V0351_H.mp4")
clip_2 = VideoFileClip("/media/cle-184/CLE/RELEASES/RELEASE 2 - Dec-Feb/3.Data Annotation/Annotated-Data/V0353_H/V0353_H.mp4")
final_clip = concatenate_videoclips([clip_1,clip_2])
final_clip.write_videofile("final.mp4")
