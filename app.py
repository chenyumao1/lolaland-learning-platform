import streamlit as st
import os
import json
from pathlib import Path

# 课程权限配置
COURSES = {
    "phonics": {
        "name": "🔤 Phonics",
        "description": "26个字母基础学习"
    },
    "power_up": {
        "name": "⚡ Power up", 
        "description": "Pre/G1/G2 综合能力提升"
    },
    "journeys": {
        "name": "🚀 Journeys",
        "description": "GK/G1/G2 深度阅读理解"
    },
    "grammar_writing": {
        "name": "✍️ Grammar & Writing",
        "description": "18个精品语法写作课程"
    }
}

# 用户管理功能
def load_users_data():
    """加载用户数据"""
    # 优先尝试从Streamlit Secrets加载用户数据
    try:
        if hasattr(st, 'secrets') and 'users' in st.secrets:
            users_data = {}
            for username, user_json in st.secrets['users'].items():
                users_data[username] = json.loads(user_json)
            return users_data
    except Exception as e:
        pass  # 如果Secrets不可用，继续尝试本地文件
    
    # 尝试从本地文件加载
    try:
        with open('users_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # 如果用户数据文件不存在，创建默认的guest用户
        default_users = {
            "guest": {
                "password": "guest",
                "name": "访客用户",
                "email": "guest@example.com",
                "purchased_courses": [],
                "purchase_date": "2024-06-21"
            }
        }
        # 创建默认的用户数据文件（仅本地开发时）
        try:
            with open('users_data.json', 'w', encoding='utf-8') as f:
                json.dump(default_users, f, ensure_ascii=False, indent=2)
        except:
            pass  # 在Streamlit Cloud上可能没有写权限
        return default_users

def authenticate_user(username, password):
    """用户认证"""
    users_data = load_users_data()
    # 将用户名转换为小写进行比较
    username_lower = username.lower()
    for user_key, user_data in users_data.items():
        if user_key.lower() == username_lower:
            if user_data['password'] == password:
                return user_data
    return None

def show_login_page():
    """显示登录页面"""
    # 可爱的背景和装饰
    st.markdown("""
    <style>
        .cute-background {
            background: linear-gradient(135deg, #ffeef8 0%, #f0e6ff 50%, #e6f3ff 100%);
            padding: 2rem;
            border-radius: 30px;
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
            overflow: hidden;
        }
        .cute-title {
            color: #ff6b9d;
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(255,107,157,0.3);
            animation: bounce 2s infinite;
        }
        .cute-subtitle {
            color: #9c88ff;
            font-size: 1.4rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }
        .floating-hearts {
            position: absolute;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            pointer-events: none;
        }
        .heart {
            position: absolute;
            color: #ffb3d9;
            font-size: 1.2rem;
            animation: float 3s ease-in-out infinite;
        }
        .heart:nth-child(1) { left: 10%; animation-delay: 0s; }
        .heart:nth-child(2) { left: 20%; animation-delay: 0.5s; }
        .heart:nth-child(3) { left: 80%; animation-delay: 1s; }
        .heart:nth-child(4) { left: 90%; animation-delay: 1.5s; }
        
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(10deg); }
        }
                 
        .cute-input {
            border-radius: 25px !important;
            border: 2px solid #ffb3d9 !important;
            padding: 12px 20px !important;
            font-size: 1.1rem !important;
        }
        .cute-input:focus {
            border-color: #ff6b9d !important;
            box-shadow: 0 0 10px rgba(255,107,157,0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # 可爱的标题区域
    st.markdown("""
    <div class="cute-background">
        <div class="floating-hearts">
            <div class="heart">💖</div>
            <div class="heart">🌸</div>
            <div class="heart">✨</div>
            <div class="heart">🦄</div>
        </div>
        <h1 class="cute-title">🌟 Lolaland 🌈</h1>
        <p class="cute-subtitle">💫 英语学习乐园 💫</p>
        <div style="font-size: 1.5rem; margin-top: 1rem;">
            🎀 🌸 🦋 🌺 🎈 🌙 ⭐ 🌟
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 居中的可爱登录表单
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # 可爱的登录标题
        st.markdown("""
        <div style="background: linear-gradient(135deg, #fff0f5 0%, #f0f8ff 100%);
                    padding: 3rem 2.5rem;
                    border-radius: 30px;
                    box-shadow: 0 15px 35px rgba(255,182,193,0.3);
                    border: 3px solid #ffb3d9;
                    text-align: center;
                    margin: 2rem 0;">
            <h3 style="color: #ff6b9d; margin-bottom: 1rem; font-size: 1.8rem;">
                🔐 欢迎登录 
            </h3>
            <div style="font-size: 1.2rem; margin-bottom: 2rem;">
                🌈 🎨 🎪 🎭 🎪 🎨 🌈
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 用户名输入
        st.markdown('<label style="color: #ff6b9d; font-weight: bold; margin-bottom: 0.5rem; display: block;">👤 用户名</label>', unsafe_allow_html=True)
        username = st.text_input("用户名", placeholder="🌟 请输入你的用户名 🌟", key="username_input", label_visibility="collapsed")
        
        # 密码输入
        st.markdown('<label style="color: #ff6b9d; font-weight: bold; margin-bottom: 0.5rem; display: block;">🔑 密码</label>', unsafe_allow_html=True)
        password = st.text_input("密码", type="password", placeholder="🎀 请输入你的密码 🎀", key="password_input", label_visibility="collapsed")
        
        # 登录按钮
        if st.button("🚀 开始学习之旅 ✨", use_container_width=True):
            if username and password:
                user_data = authenticate_user(username, password)
                if user_data:
                    st.session_state.current_user = username
                    st.session_state.user_data = user_data
                    st.session_state.logged_in = True
                    st.balloons()  # 添加气球动画
                    st.success(f"🎉 欢迎回来，{user_data['name']}！🎉")
                    st.rerun()
                else:
                    st.error("😅 用户名或密码不对哦！请再试试看 💕")
            else:
                st.warning("🙈 请填写用户名和密码哦～ 💖")
        
        # 底部装饰
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; color: #ff6b9d;">
            <div style="font-size: 1rem; margin-bottom: 0.5rem;">
                ✨ 让我们一起快乐学英语吧！✨
            </div>
            <div style="font-size: 1.3rem;">
                🌟 💖 🌈 🦄 🎀 🌸 💫 ⭐
            </div>
        </div>
        """, unsafe_allow_html=True)

# 初始化权限系统
def initialize_permissions():
    """初始化用户权限"""
    # 初始化登录状态
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None
    
    if 'user_permissions' not in st.session_state:
        st.session_state.user_permissions = {
            "phonics": False,
            "power_up": False, 
            "journeys": False,
            "grammar_writing": False
        }
    
    if 'show_admin_panel' not in st.session_state:
        st.session_state.show_admin_panel = False
    
    # 如果用户已登录，根据用户数据设置权限
    if st.session_state.logged_in and st.session_state.user_data:
        purchased_courses = st.session_state.user_data.get('purchased_courses', [])
        for course_key in st.session_state.user_permissions.keys():
            st.session_state.user_permissions[course_key] = course_key in purchased_courses

def check_course_permission(course_key):
    """检查用户是否有特定课程的权限"""
    return st.session_state.user_permissions.get(course_key, False)

def show_user_sidebar():
    """显示用户侧边栏"""
    with st.sidebar:
        # 显示当前登录用户信息
        if st.session_state.logged_in and st.session_state.user_data:
            st.markdown("### 👤 用户信息")
            user_data = st.session_state.user_data
            st.markdown(f"**用户:** {user_data['name']}")
            st.markdown(f"**邮箱:** {user_data['email']}")
            
            if st.button("退出登录", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.current_user = None
                st.session_state.user_data = None
                # 重置权限
                for key in st.session_state.user_permissions:
                    st.session_state.user_permissions[key] = False
                st.rerun()
        
        st.markdown("---")
        
        # 显示用户权限状态
        st.markdown("### 📚 我的课程")
        
        unlocked_courses = []
        locked_courses = []
        
        for course_key, course_info in COURSES.items():
            if st.session_state.user_permissions[course_key]:
                unlocked_courses.append(course_info['name'])
            else:
                locked_courses.append(course_info['name'])
        
        if unlocked_courses:
            st.markdown("**✅ 已解锁课程:**")
            for course in unlocked_courses:
                st.markdown(f"• {course}")
        else:
            st.markdown("**😔 暂无已解锁课程**")
        
        if locked_courses:
            st.markdown("**🔒 未解锁课程:**")
            for course in locked_courses:
                st.markdown(f"• {course}")

def show_course_purchase_info(course_key):
    """显示课程购买信息"""
    course_info = COURSES[course_key]
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%); 
                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                border: 2px solid #ff6b9d;">
        <h3 style="color: #d63384; margin-bottom: 1rem;">🔒 课程未解锁</h3>
        <h4 style="color: #6f42c1; margin-bottom: 1rem;">{course_info['name']}</h4>
        <p style="color: #495057; font-size: 1.1rem; margin-bottom: 1rem;">{course_info['description']}</p>
        <p style="color: #6c757d; font-size: 0.9rem;">请联系管理员获取此课程的访问权限</p>
    </div>
    """, unsafe_allow_html=True)

def show_locked_tab_content(course_key):
    """显示锁定状态的标签页内容"""
    course_info = COURSES[course_key]
    
    # 显示课程预览信息
    st.markdown(f'<h2 style="text-align: center; color: #6c757d; font-size: 2.5rem; margin-bottom: 2rem;">{course_info["name"]} 🔒</h2>', unsafe_allow_html=True)
    
    # 显示购买信息
    show_course_purchase_info(course_key)
    
    # 显示课程特色预览（但不可交互）
    st.markdown('<h3 style="color: #6c757d; margin-bottom: 2rem;">🔍 课程预览</h3>', unsafe_allow_html=True)
    
    if course_key == "power_up":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 2rem; border-radius: 20px; text-align: center; color: white;
                        opacity: 0.6;">
                <h4>💪 能力提升</h4>
                <p>全面提升英语综合能力</p>
                <p style="color: #ffd700;">🔒 需要解锁</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                        padding: 2rem; border-radius: 20px; text-align: center; color: white;
                        opacity: 0.6;">
                <h4>🎯 分级教学</h4>
                <p>针对不同年龄段设计</p>
                <p style="color: #ffd700;">🔒 需要解锁</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                        padding: 2rem; border-radius: 20px; text-align: center; color: #333;
                        opacity: 0.6;">
                <h4>⚡ 快速进步</h4>
                <p>科学的学习进度安排</p>
                <p style="color: #dc3545;">🔒 需要解锁</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif course_key == "journeys":
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ff7b7b 0%, #ff6b9d 100%); 
                        padding: 2rem; border-radius: 20px; text-align: center; color: white;
                        opacity: 0.6;">
                <h4>📖 阅读理解</h4>
                <p>培养深度阅读理解能力</p>
                <p style="color: #ffd700;">🔒 需要解锁</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                        padding: 2rem; border-radius: 20px; text-align: center; color: white;
                        opacity: 0.6;">
                <h4>🎭 文学欣赏</h4>
                <p>探索丰富的文学世界</p>
                <p style="color: #ffd700;">🔒 需要解锁</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif course_key == "grammar_writing":
        st.markdown("""
        <div style="background: linear-gradient(135deg, #e0e0e0 0%, #f5f5f5 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                    opacity: 0.7;">
            <h4 style="color: #6c757d;">📚 18个精品课程</h4>
            <p style="color: #6c757d;">系统性的语法教学和写作训练</p>
            <p style="color: #dc3545; font-weight: bold;">🔒 请购买课程以查看详细内容</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif course_key == "phonics":
        # Phonics 预览布局
        st.markdown('<h4 style="color: #6c757d; text-align: center; margin-bottom: 2rem;">🔍 Level 1 - 字母学习预览</h4>', unsafe_allow_html=True)
        
        # 显示部分字母（但不可点击）
        letters = 'ABCDEF'  # 只显示前6个字母作为预览
        cols = st.columns(6)
        for i, letter in enumerate(letters):
            with cols[i]:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                            padding: 1.5rem; border-radius: 15px; text-align: center; 
                            opacity: 0.6; margin-bottom: 1rem;">
                    <div style="font-size: 2rem; font-weight: bold; color: white;">
                        {letter}
                    </div>
                    <div style="color: #ffd700; font-size: 0.8rem;">🔒</div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="text-align: center; margin-top: 2rem; color: #6c757d;">
            <p>还有20个字母等待解锁...</p>
            <p style="color: #dc3545; font-weight: bold;">🔒 购买后可学习完整的26个字母</p>
        </div>
        """, unsafe_allow_html=True)

# 页面配置
st.set_page_config(
    page_title="Lolaland - 英语学习平台",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
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
    
    /* 可爱的按钮样式 */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b9d 0%, #ffa0c9 100%) !important;
        color: white !important;
        border: 2px solid #ff91c7 !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        padding: 0.8rem 1.5rem !important;
        box-shadow: 0 4px 15px rgba(255,107,157,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #ff4d8a 0%, #ff80b3 100%) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255,107,157,0.4) !important;
    }
    
    .stTextInput > div > div > input {
        border-radius: 20px !important;
        border: 2px solid #ffb3d9 !important;
        padding: 12px 20px !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff6b9d !important;
        box-shadow: 0 0 10px rgba(255,107,157,0.3) !important;
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
if 'selected_level' not in st.session_state:
    st.session_state.selected_level = 1
if 'selected_lesson' not in st.session_state:
    st.session_state.selected_lesson = None
if 'power_up_page' not in st.session_state:
    st.session_state.power_up_page = 'levels'
if 'selected_power_up_grade' not in st.session_state:
    st.session_state.selected_power_up_grade = None
if 'selected_power_up_lesson' not in st.session_state:
    st.session_state.selected_power_up_lesson = None
if 'selected_power_up_unit' not in st.session_state:
    st.session_state.selected_power_up_unit = None

def show_phonics_tab():
    """显示Phonics课程标签页"""
    # 检查权限
    if not check_course_permission("phonics"):
        show_locked_tab_content("phonics")
        return
    
    if st.session_state.phonics_page == 'letter_detail':
        show_letter_detail_page()
    elif st.session_state.phonics_page == 'lesson_detail':
        show_lesson_detail_page()
    else:
        # 显示Level选择和课程内容
        st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">🔤 Phonics 课程</h2>', unsafe_allow_html=True)
        
        # Level选择区域
        st.markdown('<h3 style="color: #667eea; margin-bottom: 1rem;">📚 选择学习等级</h3>', unsafe_allow_html=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            if st.button("Level 1", key="phonics_level1", use_container_width=True):
                st.session_state.selected_level = 1
                st.success("Level 1 已选中 - 请向下滚动学习26个字母")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">26个字母</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("Level 2", key="phonics_level2", use_container_width=True):
                st.session_state.selected_level = 2
                st.success("Level 2 已选中 - 请向下滚动学习20个课程")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">20个课程</div>', unsafe_allow_html=True)
        
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
        
        # 根据选择的Level显示不同内容
        if st.session_state.selected_level == 1:
            show_level1_content()
        elif st.session_state.selected_level == 2:
            show_level2_content()

def show_level1_content():
    """显示Level 1内容 - 26个字母"""
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

def show_level2_content():
    """显示Level 2内容 - 20个课程"""
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🎵 Level 2 - 音频课程</h3>', unsafe_allow_html=True)
    
    # 创建20个课程的网格布局
    lessons = [
        "Lesson 1: 单音节发音", "Lesson 2: 双音节发音", "Lesson 3: 元音组合", "Lesson 4: 辅音组合",
        "Lesson 5: 长元音练习", "Lesson 6: 短元音练习", "Lesson 7: 音节分割", "Lesson 8: 重音练习",
        "Lesson 9: 语音节奏", "Lesson 10: 连读技巧", "Lesson 11: 弱读练习", "Lesson 12: 语调变化",
        "Lesson 13: 句子重音", "Lesson 14: 问句语调", "Lesson 15: 感叹语调", "Lesson 16: 对话练习",
        "Lesson 17: 故事朗读", "Lesson 18: 诗歌韵律", "Lesson 19: 绕口令", "Lesson 20: 综合练习"
    ]
    
    # 每行显示4个课程
    rows = [lessons[i:i+4] for i in range(0, len(lessons), 4)]
    
    for row in rows:
        cols = st.columns(4)
        for i, lesson in enumerate(row):
            with cols[i]:
                lesson_num = int(lesson.split(":")[0].split(" ")[1])
                lesson_title = lesson.split(": ")[1]
                
                if st.button(f"🎵 {lesson_title}", key=f"lesson_{lesson_num}", use_container_width=True):
                    st.session_state.selected_lesson = lesson_num
                    st.session_state.phonics_page = 'lesson_detail'
                    st.rerun()
                
                st.markdown(f'<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">课程 {lesson_num}</div>', unsafe_allow_html=True)

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
        st.info(f"请将字母 {letter} 的视频文件放入 `videos/{letter.lower()}.mp4`")
    
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

def show_lesson_detail_page():
    """显示Level 2课程详情页面"""
    lesson_num = st.session_state.selected_lesson
    
    if st.button("← 返回课程列表", key="back_level2"):
        st.session_state.phonics_page = 'levels'
        st.rerun()
    
    st.markdown(f'<h1 style="text-align: center; color: #4facfe; font-size: 3rem; margin-bottom: 2rem;">🎵 课程 {lesson_num}</h1>', unsafe_allow_html=True)
    
    # 创建视频容器
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    
    # 检查音频/视频文件是否存在
    # 尝试多种格式和命名方式
    possible_files = [
        f"videos/lesson{lesson_num}.mp4",
        f"videos/lesson_{lesson_num}.mp4", 
        f"videos/level2_lesson{lesson_num}.mp4",
        f"videos/level2_lesson_{lesson_num}.mp4",
        f"videos/l2_{lesson_num}.mp4",
        f"videos/lesson{lesson_num}.mp3",
        f"videos/lesson_{lesson_num}.mp3"
    ]
    
    video_found = False
    for video_path in possible_files:
        if os.path.exists(video_path):
            if video_path.endswith('.mp3'):
                st.audio(video_path)
            else:
                st.video(video_path)
            video_found = True
            break
    
    if not video_found:
        st.info(f"""
        请将课程 {lesson_num} 的音频/视频文件放入 videos/ 目录，支持以下命名格式：
        - `lesson{lesson_num}.mp4` 或 `lesson{lesson_num}.mp3`
        - `lesson_{lesson_num}.mp4` 或 `lesson_{lesson_num}.mp3`
        - `level2_lesson{lesson_num}.mp4`
        - `l2_{lesson_num}.mp4`
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示课程相关信息
    lesson_descriptions = {
        1: "学习基本的单音节发音规则",
        2: "掌握双音节词汇的发音技巧",
        3: "练习元音字母组合的发音",
        4: "学习辅音字母组合的发音",
        5: "掌握长元音的正确发音",
        6: "练习短元音的发音区别",
        7: "学习如何正确分割音节",
        8: "掌握词汇重音的位置",
        9: "理解英语的语音节奏",
        10: "学习单词间的连读技巧",
        11: "练习功能词的弱读",
        12: "掌握不同语调的变化",
        13: "学习句子中的重音规律",
        14: "掌握疑问句的语调",
        15: "练习感叹句的语调",
        16: "进行实际对话练习",
        17: "练习故事的朗读技巧",
        18: "学习诗歌的韵律节拍",
        19: "通过绕口令练习发音",
        20: "综合运用所学发音技巧"
    }
    
    description = lesson_descriptions.get(lesson_num, "音频发音练习课程")
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; margin-top: 2rem;">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem;">
            课程 {lesson_num} 学习目标
        </h3>
        <p style="color: rgba(255,255,255,0.9); text-align: center; font-size: 1.2rem;">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)

def show_power_up_tab():
    """显示Power up课程标签页"""
    # 检查权限
    if not check_course_permission("power_up"):
        show_locked_tab_content("power_up")
        return
    
    if st.session_state.power_up_page == 'lesson_detail':
        show_power_up_lesson_detail_page()
    elif st.session_state.power_up_page == 'unit_detail':
        show_power_up_unit_detail_page()
    else:
        # 显示课程主页
        st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">⚡ Power up</h2>', unsafe_allow_html=True)
        
        # Level选择区域
        st.markdown('<h3 style="color: #667eea; margin-bottom: 1rem;">📚 选择学习等级</h3>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("Pre", key="power_up_pre", use_container_width=True):
                st.info("Pre 预备级课程即将开放")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">预备级</div>', unsafe_allow_html=True)
        
        with col2:
            if st.button("G1", key="power_up_g1", use_container_width=True):
                st.session_state.selected_power_up_grade = "G1"
                st.success("G1 一年级课程已选中 - 请向下滚动查看课程")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">一年级</div>', unsafe_allow_html=True)
        
        with col3:
            if st.button("G2", key="power_up_g2", use_container_width=True):
                st.session_state.selected_power_up_grade = "G2"
                st.success("G2 二年级课程已选中 - 请向下滚动查看课程")
            st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">二年级</div>', unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 根据选择的年级显示课程内容
        if st.session_state.selected_power_up_grade == "G1":
            show_power_up_g1_content()
        elif st.session_state.selected_power_up_grade == "G2":
            show_power_up_g2_content()
        else:
            # 课程特色展示
            st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🌟 课程特色</h3>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                            padding: 2rem; border-radius: 20px; text-align: center; color: white;">
                    <h4>💪 能力提升</h4>
                    <p>全面提升英语综合能力</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                            padding: 2rem; border-radius: 20px; text-align: center; color: white;">
                    <h4>🎯 分级教学</h4>
                    <p>针对不同年龄段设计</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                            padding: 2rem; border-radius: 20px; text-align: center; color: #333;">
                    <h4>⚡ 快速进步</h4>
                    <p>科学的学习进度安排</p>
                </div>
                """, unsafe_allow_html=True)

def show_journeys_tab():
    """显示Journeys课程标签页"""
    # 检查权限
    if not check_course_permission("journeys"):
        show_locked_tab_content("journeys")
        return
    
    st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">🚀 Journeys</h2>', unsafe_allow_html=True)
    
    # Level选择区域
    st.markdown('<h3 style="color: #667eea; margin-bottom: 1rem;">📚 选择学习等级</h3>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("GK", key="journeys_gk", use_container_width=True):
            st.info("正在进入 GK 幼儿园课程")
        st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">幼儿园</div>', unsafe_allow_html=True)
    
    with col2:
        if st.button("G1", key="journeys_g1", use_container_width=True):
            st.info("正在进入 G1 一年级课程")
        st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">一年级</div>', unsafe_allow_html=True)
    
    with col3:
        if st.button("G2", key="journeys_g2", use_container_width=True):
            st.info("正在进入 G2 二年级课程")
        st.markdown('<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">二年级</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 课程特色展示
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🌟 课程特色</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff7b7b 0%, #ff6b9d 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>📖 阅读理解</h4>
            <p>培养深度阅读理解能力</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>文本分析</li>
                <li>主题理解</li>
                <li>批判思维</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>🎭 文学欣赏</h4>
            <p>探索丰富的文学世界</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>经典故事</li>
                <li>诗歌韵律</li>
                <li>文化背景</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_grammar_writing_tab():
    """显示Grammar & Writing课程标签页"""
    # 检查权限
    if not check_course_permission("grammar_writing"):
        show_locked_tab_content("grammar_writing")
        return
    
    st.markdown('<h2 style="text-align: center; color: #4facfe; font-size: 2.5rem; margin-bottom: 2rem;">✍️ Grammar & Writing</h2>', unsafe_allow_html=True)
    
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">📚 18个精品课程</h3>', unsafe_allow_html=True)
    
    # 创建18个课程的网格布局
    lessons = [
        "Lesson 1: 句子基础", "Lesson 2: 名词单复数", "Lesson 3: 动词时态", 
        "Lesson 4: 形容词比较", "Lesson 5: 介词用法", "Lesson 6: 疑问句",
        "Lesson 7: 否定句", "Lesson 8: 连词使用", "Lesson 9: 段落写作",
        "Lesson 10: 描述文写作", "Lesson 11: 叙述文写作", "Lesson 12: 说明文写作",
        "Lesson 13: 对话写作", "Lesson 14: 日记写作", "Lesson 15: 信件写作",
        "Lesson 16: 故事创作", "Lesson 17: 诗歌欣赏", "Lesson 18: 综合练习"
    ]
    
    # 每行显示3个课程
    rows = [lessons[i:i+3] for i in range(0, len(lessons), 3)]
    
    for row in rows:
        cols = st.columns(3)
        for i, lesson in enumerate(row):
            with cols[i]:
                lesson_num = lesson.split(":")[0].split(" ")[1]
                lesson_title = lesson.split(": ")[1]
                
                if st.button(f"📝 {lesson_title}", key=f"grammar_lesson_{lesson_num}", use_container_width=True):
                    st.info(f"正在进入 {lesson}")
                
                st.markdown(f'<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">{lesson.split(":")[0]}</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 课程特色展示
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🌟 课程亮点</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #ff7b7b 0%, #ff6b9d 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>📝 语法精讲</h4>
            <p>系统掌握英语语法规则</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>基础语法概念</li>
                <li>实用语法规则</li>
                <li>语法综合运用</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 20px; text-align: center; color: white;">
            <h4>✏️ 写作训练</h4>
            <p>循序渐进提升写作能力</p>
            <ul style="text-align: left; margin-top: 1rem;">
                <li>多种文体练习</li>
                <li>创意表达培养</li>
                <li>写作技巧指导</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

def show_power_up_g1_content():
    """显示Power up G1课程内容"""
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🎵 G1 一年级课程</h3>', unsafe_allow_html=True)
    
    # 从文件夹读取Unit文件夹
    grade_folder = "videos/PowerUp/Grade 1 "
    units = []
    
    if os.path.exists(grade_folder):
        for item in os.listdir(grade_folder):
            if os.path.isdir(os.path.join(grade_folder, item)) and item.startswith('Unit'):
                units.append(item)
    
    units.sort()  # 排序Unit文件夹
    
    if not units:
        st.info("暂无G1课程Unit文件夹")
        return
    
    # 显示课程描述
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; text-align: center; color: white; margin-bottom: 2rem;">
        <h4>🌟 G1 一年级课程</h4>
        <p>适合一年级学生的英语综合能力提升课程</p>
        <p>目前已有 {0} 个Unit，总共9个Unit（更多内容即将上线）</p>
    </div>
    """.format(len(units)), unsafe_allow_html=True)
    
    # 创建Unit课程网格
    cols_per_row = 3
    rows = [units[i:i+cols_per_row] for i in range(0, len(units), cols_per_row)]
    
    for row_index, row in enumerate(rows):
        cols = st.columns(cols_per_row)
        for col_index, unit_folder in enumerate(row):
            with cols[col_index]:
                # 从文件夹名提取Unit信息
                unit_display = unit_folder.replace('Unit ', 'Unit ')
                
                # 统计该Unit下的音频文件数量
                unit_path = os.path.join(grade_folder, unit_folder)
                audio_count = 0
                if os.path.exists(unit_path):
                    for file in os.listdir(unit_path):
                        if file.endswith('.mp3') or file.endswith('.wav'):
                            audio_count += 1
                
                if st.button(f"🎵 {unit_display}", key=f"g1_{unit_folder}", use_container_width=True):
                    st.session_state.selected_power_up_unit = unit_folder
                    st.session_state.selected_power_up_grade = "G1"
                    st.session_state.power_up_page = 'unit_detail'
                    st.rerun()
                
                st.markdown(f'<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">{audio_count} 个课程</div>', unsafe_allow_html=True)

def show_power_up_g2_content():
    """显示Power up G2课程内容"""
    st.markdown('<h3 style="color: #667eea; margin-bottom: 2rem;">🎵 G2 二年级课程</h3>', unsafe_allow_html=True)
    
    # 从文件夹读取音频文件
    audio_folder = "videos/PowerUp/Grade 2"
    audio_files = []
    
    if os.path.exists(audio_folder):
        for file in os.listdir(audio_folder):
            if file.endswith('.mp3'):
                audio_files.append(file)
    
    audio_files.sort()  # 排序文件名
    
    if not audio_files:
        st.info("暂无G2课程音频文件")
        return
    
    # 显示课程描述
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                padding: 2rem; border-radius: 20px; text-align: center; color: white; margin-bottom: 2rem;">
        <h4>🌟 G2 二年级课程</h4>
        <p>适合二年级学生的英语综合能力提升课程</p>
        <p>共有 {0} 个音频课程</p>
    </div>
    """.format(len(audio_files)), unsafe_allow_html=True)
    
    # 创建音频课程网格
    cols_per_row = 3
    rows = [audio_files[i:i+cols_per_row] for i in range(0, len(audio_files), cols_per_row)]
    
    for row_index, row in enumerate(rows):
        cols = st.columns(cols_per_row)
        for col_index, audio_file in enumerate(row):
            with cols[col_index]:
                # 从文件名提取课程信息
                lesson_name = audio_file.replace('.wav', '').replace('.mp3', '')
                if 'PU1-U2-L1' in lesson_name:
                    lesson_display = 'Unit 1'
                elif 'PU1-U2-L2' in lesson_name:
                    lesson_display = 'Unit 2'
                else:
                    lesson_display = lesson_name.replace('PU1-U2-', 'Unit ')
                
                if st.button(f"🎵 {lesson_display}", key=f"g2_{audio_file}", use_container_width=True):
                    st.session_state.selected_power_up_lesson = audio_file
                    st.session_state.selected_power_up_grade = "G2"
                    st.session_state.power_up_page = 'lesson_detail'
                    st.rerun()
                
                st.markdown(f'<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">{lesson_name}</div>', unsafe_allow_html=True)

def show_power_up_lesson_detail_page():
    """显示Power up课程详情页面"""
    grade = st.session_state.selected_power_up_grade
    lesson_file = st.session_state.selected_power_up_lesson
    
    if st.button("← 返回课程列表", key="back_power_up"):
        st.session_state.power_up_page = 'levels'
        st.rerun()
    
    # 从文件名提取课程信息
    lesson_name = lesson_file.replace('.wav', '').replace('.mp3', '')
    if grade == "G1":
        if 'PU1-U1-L1' in lesson_name:
            lesson_display = 'Unit 1'
        elif 'PU1-U1-L2' in lesson_name:
            lesson_display = 'Unit 2'
        elif 'PU1-U1-L3' in lesson_name:
            lesson_display = 'Unit 3'
        else:
            lesson_display = lesson_name.replace('PU1-U1-', 'Unit ')
        grade_name = "一年级"
        grade_folder = "Grade 1"
    else:
        if 'PU1-U2-L1' in lesson_name:
            lesson_display = 'Unit 1'
        elif 'PU1-U2-L2' in lesson_name:
            lesson_display = 'Unit 2'
        else:
            lesson_display = lesson_name.replace('PU1-U2-', 'Unit ')
        grade_name = "二年级"
        grade_folder = "Grade 2"
    
    st.markdown(f'<h1 style="text-align: center; color: #4facfe; font-size: 3rem; margin-bottom: 2rem;">⚡ Power up {grade} - {lesson_display}</h1>', unsafe_allow_html=True)
    
    # 创建音频容器
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    
    # 音频文件路径 - 需要在Unit文件夹中查找
    audio_path = None
    unit_folder = st.session_state.selected_power_up_unit
    
    if unit_folder:
        # 新的文件结构：在Unit文件夹中
        audio_path = f"videos/PowerUp/{grade_folder}/{unit_folder}/{lesson_file}"
    else:
        # 旧的文件结构：直接在Grade文件夹中
        audio_path = f"videos/PowerUp/{grade_folder}/{lesson_file}"
    
    if audio_path and os.path.exists(audio_path):
        # 根据文件扩展名选择正确的格式
        if lesson_file.endswith('.mp3'):
            st.audio(audio_path, format="audio/mpeg")
        elif lesson_file.endswith('.wav'):
            st.audio(audio_path, format="audio/wav")
        else:
            st.audio(audio_path)
    else:
        st.error(f"音频文件未找到: {audio_path}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 显示课程相关信息
    lesson_descriptions = {
        "PU1-U1-L1": "基础英语听力训练 - 字母发音和简单单词",
        "PU1-U1-L2": "词汇扩展练习 - 常用生活用语和表达",
        "PU1-U1-L3": "语音语调练习 - 句子重音和语调变化",
        "PU1-U2-L1": "进阶听力理解 - 短句和对话练习",
        "PU1-U2-L2": "语法基础应用 - 简单句型和时态练习"
    }
    
    description = lesson_descriptions.get(lesson_name, f"Power up {grade_name}英语综合能力提升课程")
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; margin-top: 2rem;">
        <h3 style="color: white; text-align: center; margin-bottom: 1rem;">
            {lesson_display} 学习目标
        </h3>
        <p style="color: rgba(255,255,255,0.9); text-align: center; font-size: 1.2rem;">
            {description}
        </p>
        <div style="text-align: center; margin-top: 1rem;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 15px; color: white;">
                🎧 请佩戴耳机获得最佳学习体验
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

def show_power_up_unit_detail_page():
    """显示Power up Unit详情页面"""
    grade = st.session_state.selected_power_up_grade
    unit_folder = st.session_state.selected_power_up_unit
    
    if st.button("← 返回课程列表", key="back_power_up_unit"):
        st.session_state.power_up_page = 'levels'
        st.rerun()
    
    # 显示Unit标题
    unit_display = unit_folder.replace('Unit ', 'Unit ')
    grade_name = "一年级" if grade == "G1" else "二年级"
    
    st.markdown(f'<h1 style="text-align: center; color: #4facfe; font-size: 3rem; margin-bottom: 2rem;">⚡ Power up {grade} - {unit_display}</h1>', unsafe_allow_html=True)
    
    # 读取Unit文件夹中的音频文件
    unit_path = f"videos/PowerUp/Grade {grade[1]} /{unit_folder}"
    audio_files = []
    
    if os.path.exists(unit_path):
        for file in os.listdir(unit_path):
            if file.endswith('.mp3') or file.endswith('.wav'):
                audio_files.append(file)
    
    audio_files.sort()  # 排序文件名
    
    if not audio_files:
        st.info(f"暂无{unit_display}音频文件")
        return
    
    # 显示Unit描述
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 20px; text-align: center; color: white; margin-bottom: 2rem;">
        <h4>🌟 {unit_display} 课程</h4>
        <p>{grade_name}英语综合能力提升课程</p>
        <p>共有 {len(audio_files)} 个音频课程</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 创建音频课程网格
    cols_per_row = 3
    rows = [audio_files[i:i+cols_per_row] for i in range(0, len(audio_files), cols_per_row)]
    
    for row_index, row in enumerate(rows):
        cols = st.columns(cols_per_row)
        for col_index, audio_file in enumerate(row):
            with cols[col_index]:
                # 从文件名提取课程信息
                lesson_name = audio_file.replace('.wav', '').replace('.mp3', '')
                # 提取Lesson编号
                if 'L1' in lesson_name:
                    lesson_display = 'Lesson 1'
                elif 'L2' in lesson_name:
                    lesson_display = 'Lesson 2'
                elif 'L3' in lesson_name:
                    lesson_display = 'Lesson 3'
                else:
                    lesson_display = lesson_name
                
                if st.button(f"🎵 {lesson_display}", key=f"unit_{audio_file}", use_container_width=True):
                    st.session_state.selected_power_up_lesson = audio_file
                    st.session_state.power_up_page = 'lesson_detail'
                    st.rerun()
                
                st.markdown(f'<div style="text-align: center; margin-top: 0.5rem; color: #666; font-size: 0.9rem;">{lesson_name}</div>', unsafe_allow_html=True)

# 主程序逻辑
def main():
    # 初始化权限系统
    initialize_permissions()
    
    # 如果未登录，显示登录页面
    if not st.session_state.logged_in:
        show_login_page()
        return
    
    # 显示用户侧边栏
    show_user_sidebar()
    
    # 主标题和副标题
    st.markdown('<h1 class="main-title">🌟 Lolaland 🌈</h1>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">💫 英语学习乐园 - 让小朋友爱上英语 🎀</div>', unsafe_allow_html=True)
    
    # 欢迎用户
    if st.session_state.user_data:
        user_name = st.session_state.user_data['name']
        st.markdown(f'''
        <div style="text-align: center; margin: 1.5rem 0;">
            <div style="background: linear-gradient(135deg, #ffeef8 0%, #f0e6ff 100%); 
                        padding: 1.5rem; border-radius: 20px; border: 2px solid #ffb3d9; display: inline-block;">
                <span style="color: #ff6b9d; font-size: 1.5rem; font-weight: bold;">
                    🎉 欢迎回来，{user_name}！🎉
                </span>
                <div style="margin-top: 0.5rem; font-size: 1.2rem;">
                    🌸 ✨ 🦄 💖 🌟 ✨ 🌸
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # 显示权限提示
    unlocked_count = sum(1 for perm in st.session_state.user_permissions.values() if perm)
    total_courses = len(COURSES)
    
    if unlocked_count == 0:
        st.warning("🔒 您当前没有任何已购买的课程。请联系管理员获取课程权限。")
    elif unlocked_count < total_courses:
        st.info(f"📚 您已解锁 {unlocked_count}/{total_courses} 套课程。查看左侧边栏了解详情。")
    else:
        st.success(f"🎉 恭喜！您已解锁全部 {total_courses} 套课程！")
    
    # 创建标签页
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔤 Phonics", 
        "⚡ Power up", 
        "🚀 Journeys", 
        "✍️ Grammar & Writing"
    ])
    
    with tab1:
        show_phonics_tab()
    
    with tab2:
        show_power_up_tab()
    
    with tab3:
        show_journeys_tab()
    
    with tab4:
        show_grammar_writing_tab()
    
    # 版权信息
    st.markdown(
        '<div class="copyright">© 2024 Lolaland English Learning Platform. All rights reserved.</div>', 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main() 