import uiautomator2 as u2
import time
from datetime import datetime
from typing import Dict, Any, List, Optional

class DeviceManager:
    """设备管理类"""
    
    def __init__(self):
        """初始化设备管理器"""
        # 存储所有已连接设备的信息
        self.devices: Dict[str, Dict[str, Any]] = {}
    
    def connect_device(self, serial: str) -> bool:
        """连接设备
        
        Args:
            serial: 设备序列号
            
        Returns:
            bool: 连接是否成功
        """
        try:
            # 连接设备
            d = u2.connect(serial)
            # 测试连接
            d.info
            # 存储设备信息
            self.devices[serial] = {
                'device': d,
                'status': 'connected',
                'last_seen': datetime.now(),
                'assets': None
            }
            return True
        except Exception as e:
            print(f"连接设备失败: {str(e)}")
            return False
    
    def scan_assets(self, serial: str, app_package: str) -> Dict[str, Any]:
        """扫描设备上的应用资产
        
        【需要修改】
        根据实际应用的UI布局修改操作步骤
        
        Args:
            serial: 设备序列号
            app_package: 应用包名
        """
        if serial not in self.devices:
            return {'error': '设备未连接'}
            
        d = self.devices[serial]['device']
        try:
            # 启动应用
            d.app_start(app_package)
            time.sleep(2)  # 等待应用启动
            
            # 【需要修改】以下步骤根据实际应用修改
            # 示例：点击资产按钮并获取金额
            d(text="资产").click()
            time.sleep(1)
            
            # 【需要修改】根据实际的UI元素获取资产数据
            amount = d(resourceId="asset_amount").get_text()
            
            # 更新设备资产信息
            asset_info = {
                'amount': float(amount),
                'timestamp': datetime.now(),
                'status': 'success'
            }
            
            self.devices[serial]['assets'] = asset_info
            return asset_info
            
        except Exception as e:
            error_info = {'error': str(e)}
            self.devices[serial]['assets'] = error_info
            return error_info
    
    def get_device_info(self, serial: str) -> Optional[Dict[str, Any]]:
        """获取设备信息"""
        if serial not in self.devices:
            return None
            
        device_data = self.devices[serial]
        return {
            'serial': serial,
            'status': device_data['status'],
            'last_seen': device_data['last_seen'],
            'assets': device_data.get('assets')
        }
    
    def get_all_devices(self) -> List[Dict[str, Any]]:
        """获取所有设备的信息"""
        return [
            self.get_device_info(serial)
            for serial in self.devices
        ]
    
    def disconnect_device(self, serial: str) -> bool:
        """断开设备连接"""
        if serial in self.devices:
            try:
                self.devices[serial]['device'].app_stop_all()
                del self.devices[serial]
                return True
            except Exception as e:
                print(f"断开设备失败: {str(e)}")
        return False