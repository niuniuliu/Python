import os
import sys

# Video and src Path - Ensure the folder only contain the folders. And only one level subfolder
video_path = r'/Users/TimLiu/Downloads/Temp/PowerShell 3.0 for Administrators {AceMerlin}'
srt_path = r'/Users/TimLiu/Desktop/PowerShell-tutorials-PowerShell-30-Administrators'

# print os.path.dirname(video_path)
v_list = os.listdir(video_path)
s_list = os.listdir(srt_path)

for original,target in zip(v_list, s_list):
    # os.system('cd ' + '"' + video_path + '"')
    # os.system('mv ' + original + ' ' + target)
    target = target.replace('.srt', '.mp4')
    # print target
    # print target
    x = 'mv %r %r' %(original,target)
    print x
    # os.system(x)


# for x in s_list:
#     y = 'mv %r/* ./' %x
#     os.system(y)

# for x in s_list:
#     tmp_path = srt_path + '/' + x
#     if os.path.isdir(tmp_path):
#         sub_files = os.listdir(tmp_path)
#         for y in sub_files:
#             filefullpath = tmp_path + '/' + y
#             prefix = filefullpath.split('/')[-2][0:2]
#             new_filefullPath = tmp_path + '/' + prefix + filefullpath.split('/')[-1]
#             cmd = 'mv %r %r' %(filefullpath, new_filefullPath)
#             print cmd
#             os.system(cmd)

    # print  srt_path + '/' + x

    


    # print y

# os.system('ls -l')