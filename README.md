# iKun 
根据Tang Nano 9k开发板官方example改编而来的spi 1.14inch lcd视频显示
### 显示效果

![image](https://github.com/Moeary/iKun/blob/main/readme%E7%94%A8%E6%96%87%E4%BB%B6/video_2023-10-15_15-57-03%2000_00_00-00_00_30.gif)
![image](https://github.com/Moeary/iKun/blob/main/readme%E7%94%A8%E6%96%87%E4%BB%B6/video_2023-10-15_15-57-19%2000_00_00-00_00_30.gif)

### 如何使用？
git pull或者git clone本项目至本地<br>
```
git clone https://github.com/Moeary/iKun.git
```
然后将想要转换的视频放入python处理文件的目录下，并修改视频路径为你视频的真实路径<br>
然后运行
```
python video2img.py
```
###### 在运行前确保你有一个相对完整的Python环境 需要安装FFmpeg（并添加到系统路径里）
执行完这这段代码之后该文件夹下回新增一个out子文件夹，并生成以frame****(*代表数字).bmp的视频帧文件<br>
之后修改bmp_image2hex_out.py文件中的第26行
```
for i in range(1,9):  # 假设你要处理1到9张图片 
```
将其改为你需要的数字，默认为1到9，如果你想处理第1001张图片到1100张图片可以修改为
'''
for i in range(1001,1100): 
'''
之后运行该程序
```
python bmp_image2hex_out.py
```
得到cxk.txt文件，内部大致如
```
assign cxk[1][32399:0] = 32400'h +"一大串16进制数字"+；
assign cxk[2][32399:0] = 32400'h +"一大串16进制数字"+；
.......
assign cxk[9][32399:0] = 32400'h +"一大串16进制数字"+；
```
###### PS：这里因为我偷懒 这个数组并没有从0开始，需要手动修改为从0开始，然后再丢入Verilog文件中
至此 准备工作全部完成，接下来需要进入Gowin IDE中进行修改
打开GowinIDE 点击左上角的文件->打开 选择我们clone下来的14_test.gprj 进行打开
lcd1![image](https://github.com/Moeary/iKun/assets/103913682/96197819-7abe-4cd5-8d3b-0b10f0482523)


