📦 Pygame demo
=======================

这个代码库的存在是为了提供一个 AI悦创·编程一对一教学而产生的库，这个库的作用是配套我未来将要出版的书籍中的代码示例，其实也就是游戏案例库。

## 0. Installation

### MacOS

```python
pip3 install PygameCase
```

### Windows

```python
pip install PygameCase
```

### 获取最新版

如果你换源了，请用下面的命令获取最新版本：

```python
pip3 install PygameCase -i https://pypi.org/simple
```

```python
pip install PygameCase -i https://pypi.org/simple
```

国内镜像源同步，比较缓慢，一般需要一天左右才会同步。



## 1. All Game

| 序号 | 名称     | 简介               | 教程                     |
| ---- | -------- | ------------------ | ------------------------ |
| 01   | 足球弹动 | 足球碰到边缘就反弹 | [Football](#31-football) |

## 2. 长期招收编程一对一学员

- AI悦创：[https://bornforthis.cn/](https://bornforthis.cn/)

## 3. Demonstration

### 3.1 Football

#### 1. 游戏体验

```python
from PygameCase import football, concise

football.run()  # 完整代码运行
# concise.run()  # 简洁代码运行
```

#### 2. 游戏代码显示

```python
from PygameCase import show_code

print(show_code("concise"))  # 课上代码输出
# print(show_code("full"))  # 完整代码输出
```

## 4. License

使用请留下版权信息，切勿删除！！！
