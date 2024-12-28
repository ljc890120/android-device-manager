class Config:
    """应用配置类"""
    
    # 调试模式
    DEBUG = True
    
    # API设置
    API_PREFIX = "/api"
    API_VERSION = "v1"
    
    # CORS设置（允许前端访问）
    CORS_ORIGINS = ["*"]
    
    # 【需要修改】默认监控的应用包名
    DEFAULT_APP_PACKAGE = "com.example.app"
    
    # 【可选配置】设备扫描超时时间（秒）
    SCAN_TIMEOUT = 30