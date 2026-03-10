# AHU 普通课程自动抢课脚本

本脚本旨在实现安徽大学（AHU）教务系统课程的自动化抢课功能。

---

## ⚠️ 注意事项

1. **必要配置**：你需要修改代码中以下参数：
   - **学号**（新教务系统主页登录账号）
   - **密码**
   - **课程编号**
   - **上课班级编号**
   - **老师名称**
   - **抢课开始时间**

   *(参考下方配置位置：)*
   ![配置截图](https://github.com/user-attachments/assets/713bc66c-0354-4a0c-8383-80914a4e0e08)

2. **操作提示**：运行前请确保已手动**清理教务系统主页的弹窗通知**。

---

## 🛠️ 运行环境准备

### 1. 浏览器要求
* **浏览器版本**：Chrome 145.0.7632.160

### 2. WebDriver 配置
* **下载地址**：[chromedriver-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/144.0.7559.133/win64/chromedriver-win64.zip)
* **安装步骤**：下载完成后，请将 `chromedriver.exe` 所在的路径添加至系统的 **环境变量 (PATH)** 中。

### 3. 依赖安装
请在终端中运行以下命令以安装必要的 Python 库：
```bash
pip install selenium
