import streamlit as str

# 1. 페이지 기본 설정 및 디자인 (아이콘 및 타이틀)
str.set_page_config(
    page_title="MBTI 포켓몬 매칭소",
    page_icon="🔮",
    layout="centered"
)

# 자체 CSS 스타일링으로 UI를 더 예쁘고 아기자기하게 꾸밉니다.
str.markdown("""
    <style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        text-align: center;
        color: #FFCB05;
        text-shadow: 3px 3px 0px #3B4CCA, -1px -1px 0px #3B4CCA, 1px -1px 0px #3B4CCA, -1px 1px 0px #3B4CCA;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.2rem;
        text-align: center;
        color: #555555;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #f0f2f6;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #FF3334;
        margin-top: 20px;
    }
    .pokemon-name {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2a2a2a;
    }
    </style>
""", unsafe_allow_html=True)

# 2. 메인 타이틀 영역
str.markdown('<div class="main-title">🔮 MBTI 포켓몬 매칭소</div>', unsafe_allow_html=True)
str.markdown('<div class="sub-title">내 성향과 딱 맞는 소울 포켓몬은 누구일까요?</div>', unsafe_allow_html=True)

# 3. MBTI 데이터베이스 구성 (추가 라이브러리 없이 딕셔너리로 구현)
mbti_pokemon = {
    "ISTJ": {"name": "철구의 정석, 무장조 🛡️", "desc": "철저하고 규칙을 잘 지키는 당신! 묵묵히 자신의 자리를 지키는 강철 성벽 같은 무장조와 똑 닮았네요."},
    "ISFJ": {"name": "다정한 치유사, 해피너스 🥚", "desc": "주변 사람들을 챙기는 따뜻한 마음씨를 가진 당신! 모두에게 행복과 힐링을 주는 해피너스 그 자체입니다."},
    "INFJ": {"name": "신비로운 통찰가, 가디안 👑", "desc": "깊은 내면과 직관을 가진 신비로운 당신! 트레이너의 마음을 민감하게 읽고 교감하는 가디안과 결이 맞아요."},
    "INTJ": {"name": "냉철한 전략가, 뮤츠 👁️‍🗨️", "desc": "논리적이고 독립적이며 완벽을 추구하는 당신! 압도적인 지능과 카리스마로 전장을 지배하는 뮤츠와 닮았습니다."},
    "ISTP": {"name": "만능 재주꾼, 루카리오 🥋", "desc": "상황 적응력이 뛰어나고 과묵한 실력파인 당신! 파동을 다루며 냉철하게 상황을 판단하는 루카리오가 제격입니다."},
    "ISFP": {"name": "평화로운 예술가, 메타몽 🧬", "desc": "예술적 감각이 있고 유연한 사고를 가진 당신! 어디든 자연스럽게 녹아들고 무엇으로든 변신할 수 있는 메타몽 유형이군요."},
    "INFP": {"name": "꿈꾸는 이상주의자, 이브이 🦊", "desc": "무한한 가능성과 순수한 감성을 품고 있는 당신! 어떤 모습으로든 아름답게 진화할 수 있는 잠재력을 가진 이브이입니다."},
    "INTP": {"name": "괴짜 천재 연구원, 후딘 🧠", "desc": "호기심이 많고 분석적인 생각을 즐기는 당신! IQ 5000을 자랑하며 끊임없이 사색하는 후딘과 영혼의 단짝입니다."},
    "ESTP": {"name": "에너지 넘치는 모험가, 에레키블 ⚡", "desc": "스릴을 즐기고 행동파인 당신! 지치지 않는 강력한 전류를 뿜어내며 현장을 주도하는 에레키블과 어울려요."},
    "ESFP": {"name": "우주의 슈퍼스타, 푸린 🎤", "desc": "어디서나 분위기 메이커 역할을 톡톡히 하는 당신! 사람들의 시선을 사로잡고 즐거움을 주는 푸린과 싱크로율 100%!"},
    "ENFP": {"name": "따스한 햇살, 피카츄 ⚡🐹", "desc": "긍정 에너지가 넘치고 호기심 많은 사랑둥이 당신! 백만볼트급 매력으로 주변을 언제나 밝게 만드는 피카츄입니다."},
    "ENTP": {"name": "재기발랄한 장난꾸러기, 팬텀 👻", "desc": "기발한 아이디어로 가득 차고 토론을 즐기는 당신! 유쾌한 장난으로 모두를 깜짝 놀라게 하는 팬텀과 찰떡궁합!"},
    "ESTJ": {"name": "위풍당당 리더, 윈디 🦁🦁", "desc": "체계적이고 책임감이 강하며 추진력이 엄청난 당신! 무리를 이끄는 전설의 포켓몬이자 든든한 리더인 윈디 스타일입니다."},
    "ESFJ": {"name": "다정다감 마당발, 망나뇽 🐉", "desc": "사교성이 좋고 타인을 돕는 데 앞장서는 당신! 넓은 바다를 날아다니며 조난당한 사람을 구해주는 친절한 망나뇽입니다."},
    "ENFJ": {"name": "열정적인 인도자, 토게키스 🕊️", "desc": "타인의 성장을 돕고 평화를 사랑하는 당신! 세상의 분쟁을 없애고 축복을 나누어주는 토게키스와 닮았습니다."},
    "ENTJ": {"name": "전장을 지배하는 대장, 리자몽 🔥", "desc": "비전이 명확하고 결단력 있게 무리를 이끄는 당신! 뜨거운 열정과 압도적인 리더십으로 목표를 향해 날아오르는 리자몽입니다."}
}

# 4. 사용자 입력 UI
str.write("")
user_mbti = str.selectbox(
    "👉 당신의 MBTI를 선택해 주세요!",
    options=list(mbti_pokemon.keys()),
    index=0
)

# 5. 결과 출력 버튼 및 이벤트
str.write("")
if str.button("✨ 내 소울 포켓몬 확인하기 ✨", use_container_width=True):
    # 센스 있는 풍선 효과 연출 🎈
    str.balloons()
    
    # 선택한 MBTI 데이터 가져오기
    pokemon_info = mbti_pokemon[user_mbti]
    
    # 깔끔하고 예쁜 카드 형태로 결과 출력
    str.markdown(f"""
        <div class="result-box">
            <small style="color: #666; font-weight: bold;">{user_mbti} 유형의 당신에게 딱 맞는 포켓몬은?</small>
            <div class="pokemon-name">{pokemon_info['name']}</div>
            <hr style="margin: 15px 0; border: 0; border-top: 1px solid #ccc;">
            <p style="color: #333; line-height: 1.6; font-size: 1.1rem;">{pokemon_info['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 하단 성공 메시지 배너
    str.success(f"🎉 {user_mbti}와(과) {pokemon_info['name'].split(',')[1].strip()}의 완벽한 매칭을 축하합니다! 🎉")
