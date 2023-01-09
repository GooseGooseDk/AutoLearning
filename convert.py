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





