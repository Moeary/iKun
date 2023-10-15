import subprocess

def split_and_resize_video(input_file, output_folder):
    command = f'ffmpeg -i {input_file} -vf "scale=240:135" -pix_fmt rgb565 {output_folder}/frame%04d.bmp'
    subprocess.call(command, shell=True) # 利用FFmpeg将视频切割成一帧，并重塑大小为240*135

# 指定输入视频文件和输出文件夹
input_file = 'bad_basketball.mp4' #请修改为你想要的视频
output_folder = 'out'

# 创建输出文件夹
subprocess.call(f'mkdir {output_folder}', shell=True)

# 调用函数进行分割和转换
split_and_resize_video(input_file, output_folder)
