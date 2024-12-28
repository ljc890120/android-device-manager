from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
from .device import DeviceManager
from .config import Config

router = APIRouter()
device_manager = DeviceManager()

@router.post("/devices/connect")
async def connect_device(serial: str) -> Dict[str, str]:
    """连接设备
    
    Args:
        serial: 设备序列号
    """
    if device_manager.connect_device(serial):
        return {
            "status": "success",
            "message": f"设备 {serial} 已连接"
        }
    raise HTTPException(
        status_code=400,
        detail="连接设备失败"
    )

@router.post("/devices/{serial}/scan")
async def scan_device_assets(
    serial: str,
    app_package: str = Config.DEFAULT_APP_PACKAGE
) -> Dict[str, Any]:
    """扫描设备资产
    
    Args:
        serial: 设备序列号
        app_package: 应用包名
    """
    result = device_manager.scan_assets(serial, app_package)
    if 'error' in result:
        raise HTTPException(
            status_code=400,
            detail=result['error']
        )
    return result

@router.get("/devices")
async def get_devices() -> Dict[str, List[Dict[str, Any]]]:
    """获取所有设备列表"""
    return {
        "devices": device_manager.get_all_devices()
    }

@router.delete("/devices/{serial}")
async def disconnect_device(serial: str) -> Dict[str, str]:
    """断开设备连接
    
    Args:
        serial: 设备序列号
    """
    if device_manager.disconnect_device(serial):
        return {
            "status": "success",
            "message": f"设备 {serial} 已断开连接"
        }
    raise HTTPException(
        status_code=400,
        detail="断开设备失败"
    )