import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw
import tkinter as tk
from tkinter import Canvas
 
class Net(torch.nn.Module):
    # 定义一个简单的全连接神经网络
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 64)
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc3 = torch.nn.Linear(64, 64)
        self.fc4 = torch.nn.Linear(64, 10)
 
    def forward(self, x):
        # 定义前向传播过程
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1)
        return x
 
class PaintApp:
    # 为模式2创建图形界面
    def __init__(self, root):
        self.root = root
        self.root.title("手写数字识别")
 
        self.canvas = Canvas(root, width=280, height=280, bg='white')
        self.canvas.pack()
        self.button_predict = tk.Button(root, text="预测", command=self.predict)
        self.button_predict.pack()
        self.button_clear = tk.Button(root, text="清除", command=self.clear)
        self.button_clear.pack()
 
        self.canvas.bind("<B1-Motion>", self.paint)
        self.image = Image.new("L", (280, 280), (0))
        self.draw = ImageDraw.Draw(self.image)
 
    def paint(self, event):
        # 在画布上绘制用户输入的手写数字
        x1, y1 = (event.x - 10), (event.y - 10)
        x2, y2 = (event.x + 10), (event.y + 10)
        self.canvas.create_oval(x1, y1, x2, y2, fill="white", width=20)
        self.draw.ellipse([x1, y1, x2, y2], fill="white", width=20)
 
    def clear(self):
        # 清除画布上的内容
        self.canvas.delete("all")
        self.image = Image.new("L", (280, 280), (0))
        self.draw = ImageDraw.Draw(self.image)
 
    def predict(self):
        # 对画布上的手写数字进行预测
        img = self.image.resize((28, 28), Image.LANCZOS)
        img_tensor = transforms.ToTensor()(img).unsqueeze(0)
        with torch.no_grad():
            output = net(img_tensor.view(-1, 28*28))
            prediction = torch.argmax(output, dim=1).item()
            print(f"预测结果: {prediction}")
 
net=Net()

def get_data_loader(is_train):
    # 创建数据加载器
    to_tensor = transforms.Compose([transforms.ToTensor()])
    data_set = MNIST("./codes/Project_MNIST", is_train, transform=to_tensor, download=True)
    return DataLoader(data_set, batch_size=15, shuffle=True)
 
def evaluate(test_data, net):
    # 评估模型在测试数据上的准确率
    n_correct = 0
    n_total = 0
    with torch.no_grad():
        for (x, y) in test_data:
            outputs = net.forward(x.view(-1, 28*28))
            for i, output in enumerate(outputs):
                if torch.argmax(output) == y[i]:
                    n_correct += 1
                n_total += 1
    return n_correct / n_total
 
def load_and_preprocess_image(image_path):
    # 加载图像并进行预处理
    image = Image.open(image_path).convert('L')     # 转换为灰度图
    transform = transforms.Compose([
        transforms.Resize((28, 28)),                # 调整为28x28
        transforms.ToTensor(),                      # 转换为Tensor
        transforms.Lambda(lambda x: x.view(-1))     # 将图片展平
    ])
    image_tensor = transform(image)
    return image_tensor
 
def model():
    # 加载或训练模型
    try:                                                                                # 尝试加载已保存的模型
        net.load_state_dict\
(torch.load("./codes/Project_MNIST/TrainedModels/Model.pth", weights_only=True))# 加载模型
        net.eval()                                                                      # 设置为评估模式
        print("载入本地模型成功。")
    except FileNotFoundError:
        print("未找到本地模型，正在训练新模型...")
        train_data = get_data_loader(is_train=True)
        test_data = get_data_loader(is_train=False)
        print("初始精确度：",evaluate(test_data,net))
        optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
        epoch_num=5                                                                     # 模型训练周期
        for epoch in range(epoch_num):
            for (x, y) in train_data:
                net.zero_grad()
                output = net.forward(x.view(-1, 28*28))
                loss = torch.nn.functional.nll_loss(output, y)
                loss.backward()
                optimizer.step()
            print("周期：",epoch+1,"    精确度：",evaluate(test_data,net))
        torch.save(net.state_dict(), "./codes/Project_MNIST/TrainedModels/Model.pth")
        print("模型已保存。")

def mode_1():
    # 模式1：输入本地图像文件名进行预测
    model()
    while True:
        prefix="./codes/Project_MNIST/TestImages/"
        file_name=input("请输入图像文件名,或输入“end”结束程序: ")
        custom_image_name=prefix+file_name
        if file_name == 'end':
            print("退出程序。")
            break
        try:
            custom_image_tensor = load_and_preprocess_image(custom_image_name)
            custom_image_tensor = custom_image_tensor.unsqueeze(0)
            predict = torch.argmax(net.forward(custom_image_tensor))
            print("图像预测结果: ", int(predict.item()))                # 输出预测结果
            # 可视化
            custom_image = Image.open(custom_image_name).convert('L')  # 重新加载图像以便于可视化
            plt.imshow(custom_image, cmap='gray')                      # 使用灰度图显示
            plt.title("Prediction: " + str(int(predict.item())))
            plt.axis('off')                                            # 关闭坐标轴
            plt.show()                                                 # 显示图像和预测结果
        except Exception as e:
            print(f"加载图像出错: {e}")
 
def mode_2():
    # 模式2：手写数字进行预测
    model()
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
 
def mode_3():
    # 模式3：从MNIST数据集中随机抽取3张图片进行预测
    model()
    test_data = get_data_loader(is_train=False)
    for (n, (x, _)) in enumerate(test_data):
        num=3                                                                          # 抽取的图片数量
        if n >= num:
            break
        predict = torch.argmax(net.forward(x[0].view(-1, 28*28)))
        plt.figure(n)
        plt.imshow(x[0].view(28, 28))
        plt.title("prediction: " + str(int(predict)))
    plt.show()
 
if __name__ == "__main__":
    # 主程序入口，选择预测模式
    while True:
        print("\
\n请输入数字以选择预测模式：\
\n1.输入本地图像文件名进行预测\
\n2.手写数字进行预测\
\n3.从MNIST数据集中随机抽取3张图片进行预测\
\n4.退出程序")
 
        mode=input("请输入数字：")
        if mode == '1':
            mode_1()
        elif mode == '2':
            mode_2()
        elif mode == '3':
            mode_3()
        elif mode == '4':
            print("退出程序。")
            break
        else:
            print("输入错误，请重新输入。")