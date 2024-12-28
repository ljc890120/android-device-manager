Android Device Manager - 部署文档
─────────────────────────────────
【项目说明】
基于 FastAPI 和 Vue.js 的安卓设备管理系统，用于管理 USB 连接的安卓设备并监控应用资产。
【环境要求】
1. Python 环境
∟ Python 3.7+
∟ pip (Python包管理器)
Node.js 环境
∟ Node.js 14+
∟ npm 或 yarn
Android 开发环境
∟ Android SDK Platform Tools
∟ USB 调试驱动
【环境配置步骤】
Python 配置
∟ 访问 https://www.python.org/downloads/
∟ 下载并安装 Python 3.7+（安装时勾选"Add Python to PATH"）
∟ 打开命令提示符验证：
python --version
pip --version
Node.js 配置
∟ 访问 https://nodejs.org/
∟ 下载并安装 Node.js
∟ 打开命令提示符验证：
node --version
npm --version
ADB 配置
∟ 访问 https://developer.android.com/studio/releases/platform-tools
∟ 下载 SDK Platform Tools
∟ 解压到指定目录（如 C:\Android\platform-tools）
∟ 添加到系统环境变量 Path
∟ 打开命令提示符验证：adb version
【项目部署】
后端部署
∟ cd backend
∟ pip install -r requirements.txt
∟ python main.py
前端部署
∟ cd frontend
∟ npm install (或 yarn)
∟ npm run serve (或 yarn serve)
【设备连接配置】
手机设置
∟ 开启开发者选项：设置 → 关于手机 → 版本号(点击7次)
∟ 启用 USB 调试：开发者选项 → USB调试
设备连接
∟ USB连接手机到电脑
∟ 允许 USB 调试授权
∟ 验证：adb devices
配置 uiautomator2
∟ pip install --upgrade uiautomator2
∟ python -m uiautomator2 init
【系统访问】
∟ 后端 API: http://localhost:8000
∟ 前端界面: http://localhost:8080
【常见问题】
adb unauthorized
∟ 检查 USB 调试授权
∟ 重新插拔 USB
∟ 重启 adb：
adb kill-server
adb start-server
2. uiautomator2 失败
∟ 确保手机解锁
∟ 检查 USB 调试
∟ 重新初始化
前端连接失败
∟ 检查后端服务
∟ 检查 CORS 配置
∟ 确认 API 地址
Python包安装失败
∟ 使用国内镜像源：
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
∟ 或者配置永久镜像源：
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
npm安装慢
∟ 使用淘宝镜像：
npm config set registry https://registry.npmmirror.com
∟ 或使用cnpm：
npm install -g cnpm --registry=https://registry.npmmirror.com
cnpm install
【开发工具】
∟ 推荐 VSCode
∟ 必装插件：
Python
Vetur
ESLint
Prettier
【调试指南】
∟ 后端调试：uvicorn main:app --reload --port 8000
∟ 前端调试：npm run serve -- --open
∟ ADB调试：
adb logcat (日志)
adb shell getprop (设备信息)
【注意事项】
∟ 保持 USB 连接稳定
∟ 定期检查设备状态
∟ 关注手机电量
∟ 使用专用 USB 端口
∟ 保持屏幕解锁
【更新日志 v1.0.0】
∟ 基础设备管理
∟ 资产监控
∟ Web管理界面