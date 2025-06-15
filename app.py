import streamlit as st
import os
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="LolaLand - 英语学习平台",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #FF6B6B;
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        letter-spacing: 2px;
    }
    
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.3rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .copyright {
        position: fixed;
        bottom: 10px;
        right: 20px;
        color: #999;
        font-size: 0.9rem;
        background: rgba(255,255,255,0.8);
        padding: 5px 10px;
        border-radius: 10px;
        backdrop-filter: blur(5px);
    }
    
    .level-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .level-card:hover {
        transform: translateY(-5px);
    }
    
    .level-title {
        color: white;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .level-description {
        color: rgba(255,255,255,0.9);
        font-size: 1.2rem;
    }
    
    .alphabet-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        padding: 2rem 0;
    }
    
    .alphabet-card {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .alphabet-card:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    
    .alphabet-letter {
        font-size: 3rem;
        font-weight: bold;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .back-button {
        background: linear-gradient(135deg, #ff7b7b 0%, #ff6b9d 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        cursor: pointer;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .video-container {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    
    .letter-title {
        text-align: center;
        color: #4facfe;
        font-size: 4rem;
        font-weight: bold;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# 初始化session state
if 'selected_letter' not in st.session_state:
    st.session_state.selected_letter = None
if 'phonics_page' not in st.session_state:
    st.session_state.phonics_page = 'levels'

def show_phonics_tab():
    """显示Phonics课程标签页"""
    if st.session_state.phonics_page == 'letter_detail':
        show_letter_detail_page()
    else:
        # 显示Level选择和Level 1字母学习
        st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">🔤 Phonics 课程</h2>', unsafe_allow_html=True)
        
        # Level选择区域
        st.markdown('<h3 style="color: #667eea; margin-bottom: 1rem;">📚 选择学习等级</h3>', unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            if st.button("Level 1", key="phonics_level1", use_container_width=True):
                st.success("Level 1 已选中 - 请向下滚动学习26个字母")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">26个字母</div>', unsafe_allow_html=True)
        
        with col2:
            st.button("Level 2", key="phonics_level2", use_container_width=True, disabled=True)
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #999; font-size: 0.9rem;">即将开放</div>', unsafe_allow_html=True)
        
        with col3:
            st.button("Level 3", key="phonics_level3", use_container_width=True, disabled=True)
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #999; font-size: 0.9rem;">即将开放</div>', unsafe_allow_html=True)
        
        with col4:
            st.button("Level 4", key="phonics_level4", use_container_width=True, disabled=True)
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #999; font-size: 0.9rem;">即将开放</div>', unsafe_allow_html=True)
        
        with col5:
            st.button("Level 5", key="phonics_level5", use_container_width=True, disabled=True)
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #999; font-size: 0.9rem;">即将开放</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Level 1 字母学习区域
        st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🌟 Level 1 - 字母学习</h3>', unsafe_allow_html=True)
        
        # 创建字母网格
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        # 每行显示6个字母
        rows = [letters[i:i+6] for i in range(0, len(letters), 6)]
        
        for row in rows:
            cols = st.columns(6)
            for i, letter in enumerate(row):
                with cols[i]:
                    if st.button(f"🔤 {letter}", key=f"letter_{letter}", use_container_width=True):
                        st.session_state.selected_letter = letter
                        st.session_state.phonics_page = 'letter_detail'
                        st.rerun()

def show_hmh_tab():
    """显示HMH Into Reading课程标签页"""
    st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">📖 HMH Into Reading</h2>', unsafe_allow_html=True)
    
    st.info("🚧 HMH Into Reading 课程正在开发中，敬请期待！")
    
    # 预览功能
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>📚 阅读理解</h4>
            <p>提升阅读技能</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>🎯 词汇建设</h4>
            <p>扩展词汇量</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: #333;">
            <h4>✍️ 写作练习</h4>
            <p>提高写作能力</p>
        </div>
        """, unsafe_allow_html=True)

def show_grammar_tab():
    """显示Grammar and Writing课程标签页"""
    st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">✍️ Grammar and Writing</h2>', unsafe_allow_html=True)
    
    st.info("🚧 Grammar and Writing 课程正在开发中，敬请期待！")
    
    # 预览功能
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff7b7b 0%, #ff6b9d 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>📝 语法基础</h4>
            <p>掌握英语语法规则</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>句子结构</li>
                <li>时态运用</li>
                <li>词性识别</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>✏️ 写作训练</h4>
            <p>提升写作技巧</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>段落写作</li>
                <li>作文结构</li>
                <li>创意表达</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_picture_book_tab():
    """显示Picture Book Reading课程标签页"""
    st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">📚 Picture Book Reading</h2>', unsafe_allow_html=True)
    
    st.info("🚧 Picture Book Reading 课程正在开发中，敬请期待！")
    
    # 预览功能
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: #333;">
            <h4>🎨 经典绘本</h4>
            <p>精选优质绘本故事</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>🎭 互动阅读</h4>
            <p>声音与画面结合</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>🤔 理解练习</h4>
            <p>培养阅读理解能力</p>
        </div>
        """, unsafe_allow_html=True)

def show_letter_detail_page():
    """显示单个字母详情页面"""
    letter = st.session_state.selected_letter
    
    if st.button("← 返回字母列表", key="back_level1"):
        st.session_state.phonics_page = 'levels'
        st.rerun()
    
    st.markdown(f'<h1 class="letter-title">{letter}</h1>', unsafe_allow_html=True)
    
    # 创建视频容器
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    
    # 检查视频文件是否存在
    video_path = f"videos/{letter.lower()}.mp4"
    
    if os.path.exists(video_path):
        st.video(video_path)
    else:
        st.info(f"请将字母 {letter} 的视频文件上传到 `videos/{letter.lower()}.mp4`")
        
        # 提供文件上传功能
        uploaded_file = st.file_uploader(
            f"上传字母 {letter} 的视频",
            type=['mp4', 'mov', 'avi'],
            key=f"upload_{letter}"
        )
        
        if uploaded_file is not None:
            # 创建videos目录（如果不存在）
            os.makedirs("videos", exist_ok=True)
            
            # 保存上传的文件
            with open(video_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            st.success(f"视频已成功上传！")
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示字母相关信息
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; margin-top: 2rem;">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem;">
            学习字母 {letter}
        </h3>
        <p style="color: rgba(255,255,255,0.9); text-align: center; font-size: 1.2rem;">
            观看视频，跟着老师一起学习字母 {letter} 的发音和写法！
        </p>
    </div>
    """, unsafe_allow_html=True)

# 主程序逻辑
def main():
    # 主标题和副标题
    st.markdown('<h1 class="main-title">🌟 LolaLand</h1>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">专业英语学习平台 - 让孩子爱上英语</div>', unsafe_allow_html=True)
    
    # 创建标签页
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔤 Phonics", 
        "📖 HMH Into Reading", 
        "✍️ Grammar & Writing", 
        "📚 Picture Book Reading"
    ])
    
    with tab1:
        show_phonics_tab()
    
    with tab2:
        show_hmh_tab()
    
    with tab3:
        show_grammar_tab()
    
    with tab4:
        show_picture_book_tab()
    
    # 版权信息
    st.markdown(
        '<div class="copyright">© 2024 LolaLand English Learning Platform. All rights reserved.</div>', 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 