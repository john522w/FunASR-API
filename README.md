# FunASR-API

my-asr/  
 ├── app.py                # 主入口（API/命令行入口）  
 ├── config.yaml           # 配置文件（模型路径、参数）  
 ├── models/               # 自己的模型文件或缓存路径  
 ├── audio/                # 测试音频或流式输入目录  
 ├── asr/                  # 核心 ASR 功能模块  
 │    ├── __init__.py  
 │    ├── preprocessor.py  # 特征提取、降噪  
 │    ├── inference.py     # 调用 FunASR 模型做推理  
 │    └── postprocessor.py # 后处理、标点、时间戳  
 ├── api/                  # 对外接口模块  
 │    ├── __init__.py  
 │    └── fastapi_server.py  
 ├── utils/                # 工具函数模块  
 │    ├── logger.py  
 │    ├── metrics.py       # WER/CER 等评测  
 │    └── audio_io.py      # 音频读写工具  
 └── tests/                # 测试代码  
      ├── test_inference.py  
      └── test_api.py  

### 运行FunASR-API
```
 gunicorn -w 4 -b 0.0.0.0:8000 app:app
```