## 目标
通过监听特定键盘来实现宏命令。目标是用py执行键盘模拟，用subpress库/bash执行命令。xlib好像可以用来搞xwindow，没准儿能做到对特定窗口有特定功能。

## 流程
先问，是设置还是执行
1. 设置：写新的配置文件。
	1. 查看哪个键盘。
	2. 查看所有按键
	3. 查看所有已经有功能的按键
	4. 查看按下的按键是什么，并确定是否有功能。
		1. 有，查看功能。
		2. 没有，新建一个py和bash文件。
			1. 功能用KEY_X.py的形式存在相应的keyboard文件夹里。
			2. 每个py里有数个方法分别对应分别的应用程序，和一个默认方法。
 2. 执行。 
	1. 监听并挂起键盘。
	2. 按下时执行已经定义好的py/bash。
