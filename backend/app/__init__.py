from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import Config

def create_app() -> FastAPI:
    """创建FastAPI应用"""
    
    app = FastAPI(title="Android Device Manager")
    
    # CORS配置
    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 导入路由
    from .routes import router
    app.include_router(
        router,
        prefix=f"{Config.API_PREFIX}/{Config.API_VERSION}"
    )
    
    return app