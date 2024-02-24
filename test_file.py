import os
 
def traverse_folder(path):
    result = []
    
    for root, dirs, files in os.walk(path):
        # 获取当前目录路径
        current_dir = os.path.basename(root)
        
        # 添加当前目录到结果列表
        result.append((current_dir, 'directory'))
        
        # 遍历子目录
        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            
            # 获取子目录路径
            sub_dir_name = os.path.basename(sub_dir_path)
            
            # 添加子目录到结果列表
            result.append((sub_dir_name, 'directory'))
        
        # 遍历文件
        for file in files:
            file_path = os.path.join(root, file)
            
            # 获取文件路径
            file_name = os.path.basename(file_path)
            
            # 添加文件到结果列表
            result.append((file_name, 'file'))
    
    return result
 
# 调用函数进行测试
result = traverse_folder('/code/xiaojia2/app')
print(result)