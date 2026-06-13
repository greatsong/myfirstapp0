import streamlit as st

# =========================
# 페이지 기본 설정
# =========================
st.set_page_config(
    page_title="MBTI 포켓몬 추천소",
    page_icon="✨",
    layout="centered"
)

# =========================
# 스타일
# =========================
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fff7d6 0%, #ffe3ec 45%, #e3f2ff 100%);
    }

    .title-box {
        text-align: center;
        padding: 25px;
        border-radius: 25px;
        background: rgba(255, 255, 255, 0.75);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
        margin-bottom: 25px;
    }

    .big-title {
        font-size: 42px;
        font-weight: 900;
        color: #ff5c8a;
        margin-bottom: 8px;
    }

    .sub-title {
        font-size: 18px;
        color: #555;
    }

    .pokemon-card {
        padding: 28px;
        border-radius: 28px;
        background: white;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.12);
        text-align: center;
        margin-top: 20px;
        border: 4px solid #ffe082;
    }

    .pokemon-name {
        font-size: 38px;
        font-weight: 900;
        color: #ff7043;
    }

    .pokemon-type {
        display: inline-block;
        padding: 8px 16px;
        margin: 8px;
        border-radius: 999px;
        background: #fff3cd;
        color: #7a4b00;
        font-weight: 700;
    }

    .section-box {
        padding: 20px;
        border-radius: 20px;
        background: rgba(255,255,255,0.8);
        margin-top: 18px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.06);
    }

    .small-text {
        color: #666;
        font-size: 15px;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# MBTI별 포켓몬 데이터
# =========================
pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "emoji": "🧠⚡",
        "type": "에스퍼 타입",
        "tagline": "계획은 조용히, 결과는 압도적으로!",
        "description": "INTJ는 큰 그림을 보고 전략적으로 움직이는 성향이 강합니다. 감정보다는 구조와 논리를 중시하고, 혼자 깊게 생각하며 완성도 높은 결과를 만들어내는 타입입니다.",
        "strengths": ["전략적 사고", "독립성", "문제 해결력"],
        "mission": "오늘의 미션: 머릿속에만 있던 계획 하나를 종이에 정리해보기 📘",
        "score": 96
    },
    "INTP": {
        "pokemon": "메타몽",
        "emoji": "🔬🌀",
        "type": "노말 타입",
        "tagline": "세상의 모든 가능성을 실험하는 탐구자!",
        "description": "INTP는 호기심이 많고, 새로운 아이디어를 분석하는 것을 좋아합니다. 정답을 외우기보다 원리를 이해하려는 성향이 강합니다.",
        "strengths": ["분석력", "창의적 사고", "지적 호기심"],
        "mission": "오늘의 미션: 평소 당연하게 생각한 것에 '왜?'를 세 번 붙여보기 🤔",
        "score": 94
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "emoji": "🔥👑",
        "type": "불꽃·비행 타입",
        "tagline": "목표를 정하면 하늘까지 날아가는 리더!",
        "description": "ENTJ는 추진력과 리더십이 강한 타입입니다. 목표를 빠르게 정하고, 사람과 자원을 조직해 결과를 만들어내는 데 능합니다.",
        "strengths": ["리더십", "결단력", "목표 지향성"],
        "mission": "오늘의 미션: 팀에서 미뤄진 일을 하나 정리하고 방향 제시하기 🚀",
        "score": 97
    },
    "ENTP": {
        "pokemon": "로토무",
        "emoji": "⚡📱",
        "type": "전기·고스트 타입",
        "tagline": "아이디어가 번쩍! 어디든 들어가는 장난꾸러기 발명가!",
        "description": "ENTP는 새로운 가능성을 빠르게 떠올리고 토론을 즐기는 타입입니다. 틀에 박힌 방식보다 색다른 접근을 좋아합니다.",
        "strengths": ["발상력", "순발력", "토론 능력"],
        "mission": "오늘의 미션: 익숙한 물건 하나를 완전히 다른 용도로 상상해보기 💡",
        "score": 95
    },
    "INFJ": {
        "pokemon": "뮤",
        "emoji": "🌙✨",
        "type": "에스퍼 타입",
        "tagline": "조용하지만 깊은 마음을 가진 이상주의자!",
        "description": "INFJ는 사람의 마음과 의미를 깊이 생각하는 타입입니다. 겉으로는 차분하지만 내면에는 강한 신념과 따뜻함이 있습니다.",
        "strengths": ["통찰력", "공감 능력", "깊은 신념"],
        "mission": "오늘의 미션: 누군가에게 진심 어린 응원 한마디 보내기 💌",
        "score": 96
    },
    "INFP": {
        "pokemon": "이브이",
        "emoji": "🌈🦊",
        "type": "노말 타입",
        "tagline": "가능성이 무한한 감성 모험가!",
        "description": "INFP는 자신만의 가치와 감성을 중요하게 여깁니다. 조용해 보여도 마음속에는 풍부한 상상력과 따뜻한 세계가 있습니다.",
        "strengths": ["상상력", "진정성", "공감 능력"],
        "mission": "오늘의 미션: 지금 감정을 색깔 하나로 표현해보기 🎨",
        "score": 98
    },
    "ENFJ": {
        "pokemon": "루카리오",
        "emoji": "💙🌟",
        "type": "격투·강철 타입",
        "tagline": "사람의 마음을 읽고 함께 성장하는 따뜻한 리더!",
        "description": "ENFJ는 주변 사람의 감정을 잘 살피고, 함께 성장하는 분위기를 만드는 데 능합니다. 말과 행동으로 사람을 움직이는 힘이 있습니다.",
        "strengths": ["공감 리더십", "소통 능력", "책임감"],
        "mission": "오늘의 미션: 주변 사람 한 명의 장점을 구체적으로 말해주기 🫶",
        "score": 97
    },
    "ENFP": {
        "pokemon": "피카츄",
        "emoji": "⚡😆",
        "type": "전기 타입",
        "tagline": "어디서든 분위기를 밝히는 에너지 폭발 친구!",
        "description": "ENFP는 밝고 호기심이 많으며 새로운 사람과 경험을 좋아합니다. 재미있는 아이디어를 빠르게 떠올리고 주변에 활력을 줍니다.",
        "strengths": ["활력", "창의성", "친화력"],
        "mission": "오늘의 미션: 오늘 떠오른 엉뚱한 아이디어 하나를 메모하기 ⚡",
        "score": 99
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "emoji": "🛡️💧",
        "type": "물 타입",
        "tagline": "차분하고 든든한 원칙의 수호자!",
        "description": "ISTJ는 책임감이 강하고 체계적인 타입입니다. 약속과 기준을 중요하게 여기며, 맡은 일을 끝까지 완성하려는 힘이 있습니다.",
        "strengths": ["책임감", "성실함", "체계성"],
        "mission": "오늘의 미션: 할 일을 중요도 순서대로 3개만 정리하기 ✅",
        "score": 95
    },
    "ISFJ": {
        "pokemon": "라프라스",
        "emoji": "🌊🤍",
        "type": "물·얼음 타입",
        "tagline": "조용히 곁을 지켜주는 다정한 동반자!",
        "description": "ISFJ는 배려심이 깊고 안정적인 관계를 중요하게 여깁니다. 티 내지 않아도 주변을 세심하게 챙기는 따뜻한 타입입니다.",
        "strengths": ["배려심", "성실함", "안정감"],
        "mission": "오늘의 미션: 나 자신에게도 친절한 말 한마디 해주기 🌷",
        "score": 97
    },
    "ESTJ": {
        "pokemon": "괴력몬",
        "emoji": "💪📋",
        "type": "격투 타입",
        "tagline": "계획하고 실행하는 현실형 캡틴!",
        "description": "ESTJ는 현실적이고 실행력이 뛰어난 타입입니다. 기준을 세우고 일을 효율적으로 진행하는 데 강점이 있습니다.",
        "strengths": ["실행력", "관리 능력", "현실 감각"],
        "mission": "오늘의 미션: 복잡한 일을 단계별 체크리스트로 바꿔보기 📝",
        "score": 96
    },
    "ESFJ": {
        "pokemon": "럭키",
        "emoji": "🍀💖",
        "type": "노말 타입",
        "tagline": "모두를 챙기는 행복 충전소!",
        "description": "ESFJ는 사람들과의 관계를 소중히 여기고 분위기를 따뜻하게 만드는 타입입니다. 주변을 살피고 필요한 도움을 주는 데 능합니다.",
        "strengths": ["친화력", "배려", "협력성"],
        "mission": "오늘의 미션: 고마운 사람에게 짧은 감사 메시지 보내기 💬",
        "score": 98
    },
    "ISTP": {
        "pokemon": "개굴닌자",
        "emoji": "🥷💦",
        "type": "물·악 타입",
        "tagline": "말보다 행동! 조용한 실전 해결사!",
        "description": "ISTP는 상황을 빠르게 파악하고 직접 해결하는 능력이 뛰어납니다. 불필요한 말보다 정확한 행동을 선호하는 타입입니다.",
        "strengths": ["문제 해결력", "침착함", "실용성"],
        "mission": "오늘의 미션: 고장 나거나 불편한 것 하나를 직접 개선해보기 🛠️",
        "score": 95
    },
    "ISFP": {
        "pokemon": "나인테일",
        "emoji": "🎨🦊",
        "type": "불꽃 타입",
        "tagline": "감성과 분위기를 섬세하게 느끼는 예술가!",
        "description": "ISFP는 자유롭고 감각적인 타입입니다. 말로 설명하기 어려운 분위기, 색감, 감정을 잘 느끼며 자기만의 방식으로 표현합니다.",
        "strengths": ["감수성", "미적 감각", "유연함"],
        "mission": "오늘의 미션: 마음에 드는 장면 하나를 사진이나 그림으로 남기기 📷",
        "score": 97
    },
    "ESTP": {
        "pokemon": "에이스번",
        "emoji": "⚽🔥",
        "type": "불꽃 타입",
        "tagline": "지금 이 순간을 즐기는 스피드 스타!",
        "description": "ESTP는 활동적이고 도전을 즐기는 타입입니다. 생각만 하기보다 직접 부딪히며 배우는 것을 좋아합니다.",
        "strengths": ["순발력", "도전 정신", "현장 감각"],
        "mission": "오늘의 미션: 망설이던 작은 일 하나를 바로 실행하기 🏃",
        "score": 98
    },
    "ESFP": {
        "pokemon": "푸린",
        "emoji": "🎤✨",
        "type": "노말·페어리 타입",
        "tagline": "무대를 밝히는 사랑스러운 분위기 메이커!",
        "description": "ESFP는 즐거움과 표현을 좋아하는 타입입니다. 사람들과 함께 있을 때 에너지가 살아나고, 분위기를 밝게 만드는 힘이 있습니다.",
        "strengths": ["표현력", "사교성", "긍정 에너지"],
        "mission": "오늘의 미션: 오늘 하루를 한 줄 공연 제목처럼 붙여보기 🎭",
        "score": 99
    },
}

valid_mbti = list(pokemon_data.keys())

# =========================
# 제목 영역
# =========================
st.markdown("""
<div class="title-box">
    <div class="big-title">✨ MBTI 포켓몬 추천소 ✨</div>
    <div class="sub-title">내 성격과 찰떡궁합인 포켓몬은 누구일까?</div>
</div>
""", unsafe_allow_html=True)

st.write("")

# =========================
# 입력 영역
# =========================
with st.form("mbti_form"):
    mbti_input = st.text_input(
        "MBTI를 입력해 주세요!",
        placeholder="예: ENFP, ISTJ, INTP ..."
    )

    submitted = st.form_submit_button("나의 포켓몬 찾기 🎁")

# =========================
# 결과 출력
# =========================
if submitted:
    mbti = mbti_input.strip().upper().replace(" ", "").replace("-", "")

    if mbti not in valid_mbti:
        st.warning("앗! MBTI는 ENFP, ISTJ처럼 4글자로 입력해 주세요. 🧐")
        st.info("가능한 MBTI: " + ", ".join(valid_mbti))

    else:
        result = pokemon_data[mbti]

        # 풍선 효과
        st.balloons()

        st.markdown(f"""
        <div class="pokemon-card">
            <div style="font-size: 70px;">{result["emoji"]}</div>
            <div class="pokemon-name">{result["pokemon"]}</div>
            <div class="pokemon-type">{result["type"]}</div>
            <h3>{mbti}에게 가장 잘 어울리는 포켓몬!</h3>
            <p style="font-size: 20px;"><b>{result["tagline"]}</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("### 💘 찰떡궁합 지수")
        st.progress(result["score"])
        st.write(f"**{result['score']}%** 만큼 잘 어울려요!")

        st.markdown("""
        <div class="section-box">
        """, unsafe_allow_html=True)

        st.markdown("### 🔍 성향 설명")
        st.write(result["description"])

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-box">
        """, unsafe_allow_html=True)

        st.markdown("### 🌟 대표 강점")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(result["strengths"][0])
        with col2:
            st.success(result["strengths"][1])
        with col3:
            st.success(result["strengths"][2])

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("""
        <div class="section-box">
        """, unsafe_allow_html=True)

        st.markdown("### 🎯 오늘의 포켓몬 미션")
        st.info(result["mission"])

        st.markdown("</div>", unsafe_allow_html=True)

        st.write("")
        st.caption("※ 이 앱은 재미와 교육용으로 만든 MBTI 기반 포켓몬 추천 웹앱입니다. 결과는 가볍게 즐겨주세요! 🎮")

else:
    st.markdown("""
    <div class="section-box">
        <h3>사용 방법 🎮</h3>
        <p>1. 자신의 MBTI를 입력한다.</p>
        <p>2. <b>나의 포켓몬 찾기</b> 버튼을 누른다.</p>
        <p>3. 풍선과 함께 추천 포켓몬을 확인한다!</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("### 입력 예시")
    example_cols = st.columns(4)

    examples = ["ENFP", "INTJ", "ISFJ", "ESTP"]

    for col, example in zip(example_cols, examples):
        with col:
            st.button(example, disabled=True)
