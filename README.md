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
26 for i in range(1,9):  # 假设你要处理1到9张图片 
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
![image](https://github.com/Moeary/iKun/assets/103913682/96197819-7abe-4cd5-8d3b-0b10f0482523)
<br>
打开后双击src/top.v文件 准备开始修改
<br>
![image](https://github.com/Moeary/iKun/assets/103913682/70af3537-3fb8-47d2-be80-1d075cd41517)
<br>
选中蓝色框住的10行assign代码 ，进行删除<br>
![image](https://github.com/Moeary/iKun/assets/103913682/2597a191-9581-4a3c-8d5a-2b65805f90be)
<br>
然后把之前cxk.txt文件中的10行assign代码Ctrl^C Ctrl^V复制进来<br>
至此 替换工作就完成了<br>
然后点击Process，右击Place&Route 选择Clean & Rerun All进行电路分析布线并生成BitStream文件进行烧录<br>
![image](https://github.com/Moeary/iKun/assets/103913682/920d53a4-8522-416c-9a73-06058de6c904)
![image](https://github.com/Moeary/iKun/assets/103913682/06b6f084-0d2c-4c5b-984c-0dbddcb89940)
<br>
再点击中上角的Programmer进行烧录<br>
![image](https://github.com/Moeary/iKun/assets/103913682/f6a33dcc-d5b5-4d87-acb3-66f10f7cdb9e)
<br>
会弹出一个新窗口用来烧录<br>
![image](https://github.com/Moeary/iKun/assets/103913682/fcfa3f29-dfd8-4347-9fb8-56f51dcb5342)
<br>
点击save，然后再点击中上角的下载器下载到SRAM里面<br>

###### 默认下载到SRAM，重启就没了，为了防止这个可以直接下载到flash里面不会丢失数据
<br>

![image](https://github.com/Moeary/iKun/assets/103913682/330f5b95-72be-4c02-acac-57f850bda07e)
<br>

![image](https://github.com/Moeary/iKun/assets/103913682/6e37c7b1-a6bb-458c-ab27-726f788b06f6)

<br>
等待一会就可以看到你的视频已经成功转进去并在lcd显示屏上面显示了 至此 就弄好了。
<br>

###### GowinIDE如果有不懂的可以去看看https://wiki.sipeed.com/hardware/zh/tang/Tang-Nano-9K/examples/LED.html
###### 这个先把IDE基本功能都弄明白一点再做会好很多
###### Verilog代码我我限制最多只有10帧，可以自行修改，需要修改的变量为
```
142 reg [3:0] time_cnt;   //[3:0]一共4bit最多只能循环16帧，可以自行拓展
143 wire [32399:0]cxk[9:0];  //后面9:0最多只能循环10帧 可以自行拓展
```
###### 如果修改了 time_cnt的bit数 则下面也需要修改
```
255                  if(time_cnt == 10) begin //达到10帧后
256                      time_cnt<=4'b0000;   //这里重置为0 重新开始循环
257                  end
```
###### 比如我想改成100帧可以这样改
```
142 reg [6:0] time_cnt;   //[6:0]一共7bit最多只能循环128帧
143 wire [32399:0]cxk[99:0];  //后面99:0最多只能循环100帧 


255                  if(time_cnt == 100) begin //达到100帧后
256                      time_cnt<=7'b000_0000;   //这里重置为0 重新开始循环
257                  end
```
###### 这个Verilog代码我我根据官方的代码来改的，我Verilog学的还不是很好，希望有大佬指点一下

