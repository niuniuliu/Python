import os
import sys


video_path = r'/Users/TimLiu/Documents/Baidu/Android SDK Essential Training'
srt_path = r'/Users/TimLiu/Downloads/Android-tutorials-Android-SDK-Essential-Training'





v_list = os.listdir(video_path)
s_list = os.listdir(srt_path)

for x in s_list:
    tmp_path = srt_path + '/' + x
    if os.path.isdir(tmp_path):
        sub_files = os.listdir(tmp_path)
        for y in sub_files:
            filefullpath = tmp_path + '/' + y
            prefix = filefullpath.split('/')[-2][0:2]
            new_filefullPath = tmp_path + '/' + prefix + filefullpath.split('/')[-1]
            cmd = 'mv %r %r' %(filefullpath, new_filefullPath)
            # print cmd
            # os.system(cmd)

# Step 1, Copy files to root folder
for x in v_list:
    y = 'mv %r/*.mp4 %r' %((video_path + '/' + x), video_path)
    # print y
    # os.system(y)

for x in s_list:
    y = 'mv %r/*.srt %r' %((srt_path + '/' + x), srt_path)
    # print y
    # os.system(y)

list1 = []
list2 = []

for x in os.listdir(video_path):
    # print x[-3:]
    if x[-3:] == 'mp4':
        list1.append(x)

    elif x[-3:] == 'srt':
        list2.append(x)

print len(list1)
print len(list2)

for original,target in zip(list1, list2):
    # os.system('cd ' + '"' + video_path + '"')
    # os.system('mv ' + original + ' ' + target)
    target = target.replace('.srt', '.mp4')
    # print target
    # print target
    x = 'mv %r %r' %(video_path + '/' + original, video_path + '/' + target)
    # print x
    # os.system(x)

