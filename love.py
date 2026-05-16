import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib.animation import FuncAnimation

# 设置页面布局
st.set_page_config(page_title="520 爱心表白", layout="wide")

# 隐藏 Matplotlib 坐标轴
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]

# 爱心函数
def heart(t, scale=10, shift_x=0, shift_y=0):
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x * scale + shift_x, y * scale + shift_y

# 生成爱心点
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart(t, scale=5, shift_x=0, shift_y=10)

# 创建画布
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-60, 60)
ax.set_ylim(-40, 80)
ax.axis('off')  # 隐藏坐标轴

# 初始化元素
heart_points, = ax.plot([], [], 'm.', alpha=0.8)  # 紫色爱心
message = ax.text(0, 30, '', fontsize=20, ha='center', va='center', color='pink')

# 帧更新函数
def update(frame):
    if frame < 100:
        countdown = 10 - frame // 10
        message.set_text(str(countdown))
        message.set_fontsize(40)
        heart_points.set_data([], [])
    elif frame < 200:
        message.set_text("宝宝")
        message.set_fontsize(30)
        heart_points.set_data([], [])
    elif frame < 300:
        message.set_text("I love you!")
        message.set_fontsize(25)
        heart_points.set_data([], [])
    elif frame < 400:
        message.set_text("我爱你")
        message.set_fontsize(30)
        heart_points.set_data([], [])
    else:
        message.set_text("我会永远陪着你")
        message.set_fontsize(20)
        t_frame = np.linspace(0, 2 * np.pi, frame - 390)
        x_frame, y_frame = heart(t_frame, scale=5, shift_x=0, shift_y=10)
        heart_points.set_data(x_frame, y_frame)
    return message, heart_points

# 生成动画
ani = FuncAnimation(fig, update, frames=500, interval=50, blit=True)

# Streamlit 显示动画
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>520 爱心表白</h1>", unsafe_allow_html=True)
st.pyplot(fig)