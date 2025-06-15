# LolaLand - 英语学习平台

LolaLand是专业的儿童英语学习平台，采用Streamlit构建，界面美观简洁，为孩子提供全面的英语学习体验。

## 功能特点

- 🌟 **四大课程体系**：Phonics、HMH Into Reading、Grammar & Writing、Picture Book Reading
- 🔤 **Phonics课程**：五个学习等级，从26个字母开始，循序渐进
- 📚 **Level 1 - 字母学习**：26个英文字母集中展示，每个字母配有教学视频
- 🎨 **美观界面**：适合儿童的色彩搭配和卡片式设计
- 📹 **视频上传**：支持直接上传视频文件
- 🎯 **简单操作**：Tab切换课程，点击即可学习

## 安装和运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 运行应用
```bash
streamlit run app.py
```

### 3. 访问应用
应用启动后，在浏览器中访问 `http://localhost:8501`

## 使用方法

### 主页面
- LolaLand品牌标题和专业副标题
- 四个课程标签页：Phonics、HMH Into Reading、Grammar & Writing、Picture Book Reading
- 版权信息显示

### Phonics 课程（Tab 1）
- 五个学习等级选择：Level 1-5
- Level 1字母学习直接展示在页面上
- 26个英文字母网格布局（每行6个）
- 点击任意字母进入详情页面

### 其他课程（Tab 2-4）
- HMH Into Reading: 阅读理解、词汇建设、写作练习
- Grammar & Writing: 语法基础、写作训练
- Picture Book Reading: 经典绘本、互动阅读、理解练习
- 目前显示预览界面，课程开发中

### 字母详情页面
- 大字体显示当前学习字母
- 视频播放区域
- 如果视频不存在，显示上传界面
- 支持上传MP4、MOV、AVI格式的视频文件
- 返回按钮回到字母列表

## 文件结构

```
project/
├── app.py              # 主应用文件
├── requirements.txt    # 依赖包列表
├── README.md          # 说明文档
└── videos/            # 视频文件目录（自动创建）
    ├── a.mp4         # 字母A的视频
    ├── b.mp4         # 字母B的视频
    └── ...           # 其他字母的视频
```

## 视频文件命名规则

- 视频文件需要放在 `videos/` 目录下
- 文件名格式：`{字母小写}.mp4`
- 例如：
  - 字母A的视频：`a.mp4`
  - 字母B的视频：`b.mp4`
  - 字母Z的视频：`z.mp4`

## 自定义和扩展

### 添加新的Level
在 `app.py` 中添加新的页面函数和路由逻辑。

### 修改样式
在 `app.py` 的CSS部分修改颜色、字体、布局等样式。

### 添加更多功能
- 添加学习进度跟踪
- 添加测验功能
- 添加音频播放
- 添加互动游戏

## 技术栈

- **Streamlit**: Web应用框架
- **Python**: 后端逻辑
- **HTML/CSS**: 界面样式
- **JavaScript**: 交互效果（通过Streamlit组件）

## 注意事项

- 确保视频文件大小适中，避免加载过慢
- 建议视频格式为MP4，兼容性最好
- 应用会自动创建 `videos/` 目录
- 上传的视频文件会保存在本地 `videos/` 目录中 