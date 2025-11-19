import streamlit as st
import random

st.title("📚 문장 만들기 연습")

# 첫 번째 카테고리: 머리/얼굴 특징
category1 = [
    "long curly hair",
    "short curly hair",
    "long straight hair",
    "short straight hair",
    "black hair",
    "brown hair",
    "red hair",
    "wavy hair",
    "big eyes",
    "small eyes",
    "blue eyes",
    "brown eyes",
    "green eyes",
    "round face",
    "small nose",
    "big nose",
    "thin lips",
    "thick eyebrows"
]

# 두 번째 카테고리: 의류/신발/악세사리
category2 = [
    "glasses",
    "a blue shirt",
    "a red shirt",
    "a yellow shirt",
    "a green shirt",
    "white pants",
    "black pants",
    "red pants",
    "blue pants",
    "a skirt",
    "a dress",
    "a jacket",
    "a coat",
    "a hat",
    "a scarf",
    "gloves",
    "sandals",
    
]

# 세 번째 카테고리: 성별
category3 = ["She", "He"]

if st.button("🎯 시작"):
    word1 = random.choice(category1)
    word2 = random.choice(category2)
    word3 = random.choice(category3)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"**성별:** {word3}")
    
    with col2:
        st.warning(f"**외모:** {word1}")
    
    with col3:
        st.success(f"**옷차림:** {word2}")
    
    st.divider()
    
    st.subheader("📝 문장 만들기")
    st.write("**_______ has _______.**")
    st.write("**_______ is wearing _______.**")
