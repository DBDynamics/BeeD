# Bee-D



## About DBD
DBD is a startup manufacturer of innovative matrix motion technologies, and as a manufacturer and developer of motor drives, controllers, and systems, DBD is designing its technology with emphasis on performance, efficiency, reliability, safety and simplicity.
## About BeeD
Bee-D是DBD团队开发的一款超小型创客神器,尺寸只有50mm x 38mm, 它采用ARM Cortex-M0内核的32位处理器, 主频80MHz, 内置双路步进电机驱动,运行空间矢量控制算法及动态力矩调节算法, 可以完美控制2台42及以下型号小功率步进电机.
## Technical Support
- If any questions, please feel free to contact us:
- 如果有任何问题, 请联系我们:

![Wechat](images/wechat.jpg)


## 目录 
----
- [产品介绍](#产品介绍)
  - [性能参数](#性能参数)
  - [产品细节](#产品细节)
  - [机械尺寸](#机械尺寸)
  - [接口布局](#接口布局)
  - [接线图](#接线图)
----  
- [玩法介绍](#玩法介绍)
  - [回零模式](#运行模式)
  - [位置模式](#位置模式)
  - [速度模式](#速度模式)
  - [插补模式](#插补模式)  
----
- [开发者](#开发者)
    - [快速上手](#快速上手)
      - [树莓派](#树莓派)
      - [Windows](#windows-pc)
      - [Linux](#linux-pc)
      - [Mac OS](#mac-os)
  - [高级玩法](#环境搭建)
    - [USB485-Max](#pyv3s控制器)
    - [PyV3s控制器](#pyv3s控制器)
    - [PyH6Pro控制器](#pyh6s控制器)
----
- [应用案例](#应用案例)
  - [矩阵开发套件](#矩阵开发套件)
  - [矩阵升降球](#矩阵升降球)
  - [矩阵伸缩杆](#矩阵伸缩杆)
  - [机械臂](#机械臂)
  - [同步轮自由机](#同步轮自由机)
----

## 性能参数

| 属性 | 值 |
|------|----|
| 重量 | 40g |
| 电机 | 4线2相步进电机 |
| 细分 | 256 |
| 工作电压 | DC12V |
| 最大持续输出电流 | 2x1.0A |
| PWM频率 | 20KHz |
| 输入IO | 2路(内部10K电阻上拉) |
| RS485总线 | 最高10Mbps,默认250Kbps |
| 运行温度 | -10 to +60摄氏度 |

## 产品细节

![BeeD-front](images/BeeD-front.png)
![BeeD-back](images/BeeD-back.png)

## 机械尺寸

![size](images/size.png)

## 接口布局

![StepperD](images/StepperD.png)

## 接线图

![Connection](images/Connection.png)

## 传感器接口

## 运行模式

| 模式 | 描述 |
|------|------|
| 回零模式 | 进入回零模式后,根据设定的回零方向和目标速度开始运动,直到传感器触发,达到设置回零电平参数后停止运行,并且自动将运行模式恢复为进入回零模式前的运行模式. |
| 位置模式 | 位置模式用于点位运动,可以设置加速时间,最大运行速度和目标位置 |
| 插补模式 | 插补模式全称同步位置插补模式,用于实现最多64轴电机的同步插补运动.该模式通常用于3D打印机,写字机,画图机,雕刻机,点胶机等需要多轴联动,并且执行连续轨迹的设备. |

## 开发者

### BeeD Tuner for Windows

[点击下载](downloads/BeeD.zip)

### 通信协议

[点击下载](downloads/BeeD通信协议V050114.xls)

### Python SDK

[![Python](images/Python.png)](downloads/BeeD-SDK.zip)

## 相关视频

[![视频](//player.bilibili.com/player.html?aid=993886569&bvid=BV1cx4y1A7iZ&cid=1066574485&p=1)](//player.bilibili.com/player.html?aid=993886569&bvid=BV1cx4y1A7iZ&cid=1066574485&p=1)
