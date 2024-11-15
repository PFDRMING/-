import os
from datetime import datetime

def generate_file_list():
    # 询问用户输入原文件夹路径
    folder_path = input("请输入原文件夹路径：")
    
    # 检查文件夹是否存在
    if not os.path.isdir(folder_path):
        print("指定的文件夹路径不存在。请检查后重新运行程序。")
        return
    
    # 获取文件夹中的所有文件名，过滤掉子目录，并按字母排序
    files = sorted([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    # 询问用户生成文件的保存路径
    output_folder = input("请输入生成文件保存的文件夹路径：")
    
    # 检查生成文件夹是否存在，不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"生成文件夹不存在，已创建：{output_folder}")
    
    # 获取当前日期并格式化为"YYYY-MM-DD"
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 指定输出文件名和路径
    output_file = os.path.join(output_folder, f"名单-{current_date}.txt")
    
    # 将文件名写入TXT文件
    with open(output_file, "w", encoding="utf-8") as f:
        for i, file_name in enumerate(files, start=1):
            f.write(f"{i}. {file_name}\n")
    
    print(f"文件列表已生成：{output_file}")

# 调用函数
generate_file_list()
