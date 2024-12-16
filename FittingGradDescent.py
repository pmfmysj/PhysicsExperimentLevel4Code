import numpy as np
import matplotlib.pyplot as plt

# 定义模型
def model(T, I_0, A, B):
    return I_0 / (1 + A * np.exp(B / T))  # 使用 B 替代 delta_E

# 定义损失函数（均方误差）
def loss_function(T, I, I_0, A, B):
    predictions = model(T, I_0, A, B)
    return np.mean((predictions - I) ** 2)

# 计算损失函数关于参数的梯度
def gradients(T, I, I_0, A, B):
    pred = model(T, I_0, A, B)
    
    # 对 I_0 求导
    dL_dI0 = -2 * np.mean((I - pred) / (1 + A * np.exp(B / T)))
    
    # 对 A 求导
    dL_dA = 2 * np.mean((I - pred) * np.exp(B / T) / (1 + A * np.exp(B / T))**2)
    
    # 对 B 求导
    dL_dB = 2 * np.mean((I - pred) * A * np.exp(B / T) / (T * (1 + A * np.exp(B / T))**2))
    
    return dL_dI0, dL_dA, dL_dB

# 梯度下降法拟合参数
def gradient_descent(T, I, I_0_init, A_init, B_init, learning_rate=0.01, epochs=1000):
    I_0, A, B = I_0_init, A_init, B_init
    
    # 迭代更新参数
    for epoch in range(epochs):
        # 计算梯度
        grad_I_0, grad_A, grad_B = gradients(T, I, I_0, A, B)
        
        # 更新参数
        I_0 -= learning_rate * grad_I_0
        A -= learning_rate * grad_A
        B -= learning_rate * grad_B
        
        # 每100次迭代打印一次损失
        if epoch % 100 == 0:
            loss = loss_function(T, I, I_0, A, B)
            print(f"Epoch {epoch}, Loss: {loss:.4e}")
    
    return I_0, A, B

# 数据
iDatas = np.load("iData.npy")
print(iDatas)
I = iDatas
T = np.arange(313.15, 474, 20) 

# 初始参数B = -deltaE / k_B
I_0_init = 223.09006195930672
A_init = 46017.10745732001
B_init = -3712.111895142567

# 使用梯度下降法拟合
I_0_fit, A_fit, B_fit = gradient_descent(T, I, I_0_init, A_init, B_init, learning_rate=0.001, epochs=10000)

# 打印拟合结果
print(f"拟合结果: I_0 = {I_0_fit}, A = {A_fit}, B = {B_fit}")

# 可视化拟合曲线
T_fine = np.linspace(min(T), max(T), 500)
I_fine = model(T_fine, I_0_fit, A_fit, B_fit)

plt.scatter(T, I, color='red', label="Data")
plt.plot(T_fine, I_fine, label="Fitted curve", color='blue')
plt.xlabel("Temperature (K)")
plt.ylabel("Intensity (I)")
plt.legend()
plt.show()