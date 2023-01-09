import os


def find_vip_folders(path=r'E:\music',vip_folder_name='VipSongsDownload'):
    vip_folders=[]
    for dirpath,dirnames in os.walk(path):
        for dirname in dirnames:
            if dirname==vip_folder_name:
                full_path=dirpath+'\\'+dirname
                vip_folders.append(full_path)
                print(full_path)
    return vip_folders

def mgg2ogg(input_path,output_path,core_path=r'E:\music\um.exe'):
    cmd='%s -o %s -i "%s"' % (core_path,output_path,input_path)
    print(cmd)
    ord=os.popen(cmd)
    echo=ord.read()
    return echo

# E:\music\王菲\浮躁\VipSongsDownload\王菲 - 想像.mgg

input_path='E:\music\王菲\浮躁\VipSongsDownload\王菲 - 想像.mgg'
output_path='E:\music\王菲\浮躁\VipSongsDownload'

print(mgg2ogg(input_path,output_path))
print('done')