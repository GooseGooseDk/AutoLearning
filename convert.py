import os


def find_vip_folders(path=r'E:\music',vip_folder_name='VipSongsDownload'):
    vip_folders=[]
    for root,dirs,files in os.walk(path):
        for dirname in dirs:
            if dirname==vip_folder_name:
                full_path=root+'\\'+dirname
                vip_folders.append(full_path)
                # print(full_path)
    return vip_folders

def mgg2ogg(input_path,output_path,core_path=r'E:\music\um.exe'):
    cmd='%s -o %s -i "%s"' % (core_path,output_path,input_path)
    print('cmd: '+cmd)
    if_error=os.system(cmd)
    return if_error

def main():
    vip_folders=find_vip_folders()
    print(vip_folders)
    task_list={}
    for vip_folder in vip_folders:
        task_list[vip_folder]=False
    for vip_folder in vip_folders:
        print('%s: %s' % (vip_folder,task_list[vip_folder]))

    for vip_folder in vip_folders:
        print(vip_folder)
        # 单个专辑转换
        for root,dirs,files in os.walk(vip_folder):
            # 单个文件转换
            for file in files:
                # 去掉提示
                if '.txt' not in file:
                    input_path=os.path.join(vip_folder,file)
                    # print(input_path)
                    parent = os.path.join(vip_folder, os.pardir)
                    output_path=os.path.abspath(parent)
                    # print(output_path)
                    a=mgg2ogg(input_path=input_path ,output_path=output_path)
                    if a: 
                        print('error!')
                        input()
        print('\n%s has done!\n' % vip_folder)
        task_list[vip_folder]=True

        for vip_folder in vip_folders:
            print('%s: %s' % (vip_folder,task_list[vip_folder]))
    
    print('done')


main()
