import streamlit
from utills import generate_script

streamlit.title("视频脚本生成器")

with streamlit.sidebar:
    MOONSHOT_API_KEY=streamlit.text_input("请输入MOONSHOT API秘钥：",type="password")
    streamlit.markdown("[获取MOONSHOT API秘钥] https://platform.moonshot.cn")

subject=streamlit.text_input("请输入视频的主题")
video_length=streamlit.number_input("请输入视频的大致时长（单位：分钟）",min_value=0.1,step=0.1)
creativity=streamlit.slider("请输入视频的脚本的创造力（数字小说明更严谨，数字大说明更多样）",min_value=0.0,max_value=1.0,value=0.2,step=0.1)

submit=streamlit.button("生成脚本")

if submit and not MOONSHOT_API_KEY:
    streamlit.info("请输入你的MOONSHOT API秘钥")
    streamlit.stop()
if submit and not subject:
    streamlit.info("请输入视频的主题")
    streamlit.stop()
if submit and not video_length>=0.1:
    streamlit.info("视频长度需大于或等于0.1")
    streamlit.stop()

if submit:
    with streamlit.spinner(("AI正在思考着，请稍等...")):
        search_result,title,script=generate_script(subject,video_length,creativity,MOONSHOT_API_KEY)
    streamlit.success("视频脚本已生成")
    streamlit.subheader("标题")
    streamlit.write(title)
    streamlit.subheader("视频脚本")
    streamlit.write(script)
    with streamlit.expander("维基百科搜索结果"):
        streamlit.info(search_result)
