from PIL import Image

def image_to_binary(image_path):
    img = Image.open(image_path)
    img = img.resize((240, 135)) #图像重新塑性为240*135的分辨率
    img = img.convert("L")  #转换为灰度图像

    binary_data = ""

    for pixel in img.getdata():
        if pixel < 128:  # 假设亮度小于128为黑色 亮度大于128为白色
            binary_data += "1"
        else:
            binary_data += "0"

    return binary_data

def binary_to_hex(binary_data):
    hex_data = hex(int(binary_data, 2))[2:]
    return hex_data.rjust(len(binary_data)//4, '0')

def save_hex_data_to_file(hex_data, file_name, img_num):
    with open(file_name, 'a') as file:  # 使用 'a' 模式以追加方式打开文件
        file.write(f'assign cxk[{img_num-1}][32399:0] = 32400\'h{hex_data};\n')

# 处理多张图片
for i in range(1,1000):  # 假设你要处理1到9张图片
    image_path = f"out/frame{str(i).zfill(4)}.bmp"  # 根据图片的命名规则来拼接图片路径
    binary_data = image_to_binary(image_path) 
    hex_data = binary_to_hex(binary_data)
    save_hex_data_to_file(hex_data, "cxk.txt", i) #保存至当前目录下的cxk.txt
