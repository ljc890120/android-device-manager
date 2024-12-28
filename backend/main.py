import uvicorn
from app import create_app

app = create_app()

if __name__ == "__main__":
    """启动服务器"""
    uvicorn.run(
        app,
        host="0.0.0.0",  # 允许外部访问
        port=8000,       # 服务端口
        reload=True      # 开发模式下启用热重载
    )