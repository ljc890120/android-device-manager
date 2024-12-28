<template>
  <div class="device-list">
    <!-- 添加设备 -->
    <div class="add-device">
      <input 
        v-model="newDeviceSerial" 
        placeholder="输入设备序列号"
      >
      <button @click="connectDevice">连接设备</button>
    </div>

    <!-- 设备列表 -->
    <div class="devices">
      <div 
        v-for="device in devices" 
        :key="device.serial" 
        class="device-card"
      >
        <div class="device-header">
          <h3>设备 {{ device.serial }}</h3>
          <span class="status" :class="device.status">
            {{ device.status }}
          </span>
        </div>

        <!-- 资产信息 -->
        <div class="assets" v-if="device.assets">
          <template v-if="device.assets.error">
            <p class="error">{{ device.assets.error }}</p>
          </template>
          <template v-else>
            <p>资产: {{ device.assets.amount }}</p>
            <p>更新时间: {{ formatTime(device.assets.timestamp) }}</p>
          </template>
        </div>

        <!-- 操作按钮 -->
        <div class="actions">
          <input 
            v-model="device.appPackage" 
            placeholder="应用包名"
          >
          <button 
            @click="scanAssets(device.serial, device.appPackage)"
            class="scan-btn"
          >
            扫描资产
          </button>
          <button 
            @click="disconnectDevice(device.serial)"
            class="disconnect-btn"
          >
            断开连接
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DeviceList',
  
  data() {
    return {
      devices: [],
      newDeviceSerial: ''
    }
  },
  
  methods: {
    // 连接设备
    async connectDevice() {
      if (!this.newDeviceSerial) {
        alert('请输入设备序列号')
        return
      }
      
      try {
        await this.$axios.post(`/devices/connect`, {
          serial: this.newDeviceSerial
        })
        
        this.devices.push({
          serial: this.newDeviceSerial,
          status: 'connected',
          appPackage: '',
          assets: null
        })
        
        this.newDeviceSerial = ''
      } catch (error) {
        alert('连接设备失败: ' + error.response?.data?.detail || error.message)
      }
    },
    
    // 扫描资产
    async scanAssets(serial, appPackage) {
      if (!appPackage) {
        alert('请输入应用包名')
        return
      }
      
      try {
        const response = await this.$axios.post(
          `/devices/${serial}/scan`,
          { app_package: appPackage }
        )
        
        const device = this.devices.find(d => d.serial === serial)
        if (device) {
          device.assets = response.data
        }
      } catch (error) {
        alert('扫描资产失败: ' + error.response?.data?.detail || error.message)
      }
    },
    
    // 断开设备
    async disconnectDevice(serial) {
      try {
        await this.$axios.delete(`/devices/${serial}`)
        this.devices = this.devices.filter(d => d.serial !== serial)
      } catch (error) {
        alert('断开设备失败: ' + error.response?.data?.detail || error.message)
      }
    },
    
    // 格式化时间
    formatTime(timestamp) {
      return new Date(timestamp).toLocaleString()
    }
  },
  
  // 组件挂载时获取设备列表
  async mounted() {
    try {
      const response = await this.$axios.get('/devices')
      this.devices = response.data.devices
    } catch (error) {
      console.error('获取设备列表失败:', error)
    }
  }
}
</script>

<style scoped>
.device-list {
  max-width: 800px;
  margin: 0 auto;
}

.add-device {
  margin-bottom: 20px;
  display: flex;
  gap: 10px;
}

.device-card {
  border: 1px solid #ddd;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.device-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

.status {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 14px;
}

.status.connected {
  background-color: #4CAF50;
  color: white;
}

.assets {
  margin: 15px 0;
  padding: 10px;
  background: #f5f5f5;
  border-radius: 4px;
}

.error {
  color: #f44336;
}

.actions {
  display: flex;
  gap: 10px;
  margin-top: 15px;
}

button {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
}

.scan-btn {
  background-color: #2196F3;
  color: white;
}

.disconnect-btn {
  background-color: #f44336;
  color: white;
}

input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  flex: 1;
}

button:hover {
  opacity: 0.9;
}

button:active {
  transform: translateY(1px);
}
</style>