📦 Pygame demo
=======================

这个代码库的存在是为了提供一个 AI悦创·编程一对一教学而产生的库，这个库的作用是配套我未来将要出版的书籍中的代码示例，其实也就是游戏案例库。

## 0. Installation

```cmd
pip install pygame-demo
```



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
from pygame_demo import football, concise

football.run()  # 完整代码运行
# concise.run()  # 简洁代码运行
```

#### 2. 游戏代码显示

```python
from pygame_demo import show_code

print(show_code("concise"))  # 课上代码输出
# print(show_code("full"))  # 完整代码输出
```

## 4. License

使用请留下版权信息，切勿删除！！！
