# 👩🏻‍⚖️ SK Networks AI CAMP 9기 - 4th 1Team: LawQuick

- **주제:** AI 활용 애플리케이션 개발  
- **개발 기간:** 2025.04.21 ~ 2025.04.22  

---

## 📌 목차

<details>
<summary>목차 내용</summary>

### 01. 팀 소개  
### 02. 프로젝트 개요  
### 03. 기술 스택  
### 04. 시스템 구성도  
### 05. 요구사항 정의서 (캡처)  
### 06. 화면설계서 (캡처)  
### 07. WBS  
### 08. 테스트 계획 및 결과 보고서 (캡처)  
### 09. 수행결과(테스트/시연 페이지)  
### 10. 한 줄 회고  

</details>

---

## 01. 팀 소개

### ✅ 팀명: LawQuick  
가족법 문제 해결의 가장 빠른 길

### ✅ 팀원 소개

| [@김하늘](https://github.com/nini12091) | [@박유진](https://github.com/YUJINDL01) | [@박주은](https://github.com/pprain1999) | [@유지은](https://github.com/yujitaeng) |
|-----------------------------------------|----------------------------------------|------------------------------------------|------------------------------------------|
| <img src="https://github.com/user-attachments/assets/e7dd2863-b577-4385-a46c-7163efb0bfe4" width="200" height="200"> | <img src="https://github.com/user-attachments/assets/c8ce1260-d6ca-4659-89c3-5d9f06847812" width="200" height="200" /> | <img src="https://github.com/user-attachments/assets/c80b5b8d-4a42-4ed1-950f-b0ea5b078f51" width="200" height="200"> | <img src="https://github.com/user-attachments/assets/7fdacbe3-b568-4c42-8758-d189ec522bc3" width="200" height="200" /> |

---

## 02. 프로젝트 개요

### ✅ 프로젝트 명: LawQuick  
### ✅ 프로젝트 소개: 이혼 특화 AI 법률 상담 챗봇  

**LawQuick**은 이혼 분쟁을 겪는 사용자들이 법률 정보를 통해 자신의 상황을 이해하고 조언을 얻을 수 있도록 돕는 **AI 기반 가족법 상담 챗봇**입니다.

---

### ✅ 프로젝트 필요성

#### 📈 나홀로 소송 증가
![image (5)](https://github.com/user-attachments/assets/9278a929-ee80-4aa8-b479-7b1c45dd8b75)  
![image (6)](https://github.com/user-attachments/assets/5c91008a-dcb5-4d09-a6f6-0404a3573b4f)

출처: [https://www.mk.co.kr/news/society/9878764](https://www.mk.co.kr/news/society/9878764)

- 제대로 된 법률 서비스를 이용하려면 **높은 비용 부담**이 존재함  
- 비용 문제로 법률 전문가의 도움 없이 소송을 진행하는 **'나홀로 소송'** 사례 증가

#### 📚 법률 해석의 어려움

- 정보는 많지만, **자신의 사례에 어떤 법이 적용되는지 알기 어려움**  
- 판례나 조항의 해석이 어려워 **일반인의 이해에는 한계**

---

### ✅ 프로젝트 목표

#### 📈 법률 정보의 접근성 향상  
- 복잡한 법률 용어를 **쉽고 간결한 Q&A 형식의 정보 제공**

#### 👤 개인화된 법률 조언 제공  
- 단순 정보 나열이 아닌, **사용자 상황을 반영한 맞춤형 상담 응답**

#### 💸 법률 서비스 진입장벽 완화  
- **비용 부담 없이 초기 상담을 제공**하고, 사용자의 법적 고민을 가볍게 나눌 수 있는 창구 제공

---

## 03. 기술 스택

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **LLM** | ![OpenChat](https://img.shields.io/badge/OpenChat-FFB000?style=for-the-badge&logo=OpenAI&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-005F73?style=for-the-badge&logo=Chainlink&logoColor=white) |
| **벡터 데이터베이스** | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge&logo=Apache&logoColor=white) |
| **임베딩 모델** | ![OpenAI Embeddings](https://img.shields.io/badge/OpenAI%20Embeddings-8C9E90?style=for-the-badge&logo=OpenAI&logoColor=white) |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) |
| **모델 튜닝/학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **인터페이스(UI)** | ![Gradio](https://img.shields.io/badge/Gradio-20B673?style=for-the-badge&logo=Gradio&logoColor=white) |
| **형상 관리 및 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=Google%20Drive&logoColor=white) |

---

## 04. 시스템 구성도

![시스템 아키텍처](https://github.com/user-attachments/assets/fcbd8bc8-1102-4568-8008-39fc45cf8b51)
---

## 05. 요구사항 정의서

![스크린샷 2025-04-18 162131](https://github.com/user-attachments/assets/2f377616-1702-4b08-8822-6842181c3cf2)

### ✅ 사용자 관련 요구사항

| **구분** | **요구사항 ID** | **요구사항 내용 요약** |
|----------|------------------|--------------------------|
| 로그인 | `REQ-LOGIN` | - 이메일과 비밀번호로 로그인 가능<br>- 비회원도 로그인 없이 서비스 사용 가능<br>- 이메일을 통해 비밀번호 찾기 기능 제공 |
| 회원가입 | `REQ-JOIN` | - 회원가입 기능 제공<br>- 필수 약관 동의 후 가입 가능<br>- 약관별 상세보기 및 전체 동의 기능<br>- 이메일 입력 및 도메인 선택 기능<br>- 이메일 인증 후 가입 완료<br>- 비밀번호는 영문/숫자/특수문자 포함 8~16자 제한<br>- 가입 확인 시 개인정보 입력 화면으로 이동<br>- 확인/취소 버튼에 시각 피드백<br>- 가입 취소 시 기존 입력 정보 초기화 |
| 개인정보 입력 | `REQ-PIIN` | - 혼인/자녀/재산/기타 이혼 관련 정보 입력 가능<br>- 상세 고민 입력 가능<br>- 각 항목별 설명 제공<br>- 확인 시 질의응답 화면으로 이동<br>- 취소 시 입력 초기화 및 이전 화면 이동<br>- 확인/취소 버튼 시각 피드백<br>- 항목별 건너뛰기 버튼 제공 |
| 개인정보 수정 | `REQ-PIED` | - 정보 미입력 시 신규 입력 가능<br>- 기존 입력된 정보 수정 가능 |


### ✅ 채팅 관련 요구사항

| **구분** | **요구사항 ID** | **요구사항 내용 요약** |
|----------|------------------|--------------------------|
| 질의응답 | `REQ-CHAT` | - 질문 입력 기능<br>- 질문 입력란 자동 확장 및 스크롤 처리<br>- 질문은 말풍선 + 시각 정보로 출력<br>- 답변 전 로딩 애니메이션 제공<br>- 답변은 말풍선 + 응답 시각 및 소요 시간 함께 출력 |
| 히스토리 | `REQ-HIST` | - 사이드바를 통해 이전 채팅 확인<br>- 새 채팅 시작 및 채팅 제목 수정 기능 제공<br>- 채팅 목록은 최근 7일/30일 기준으로 정렬 |

---

## 06. 화면설계서

<details>
<summary>전체 화면 설계서</summary>
<br>
  
![화면설계서 pptx (1)](https://github.com/user-attachments/assets/ae932702-bf79-49fe-b69d-57a7c3f6eabd)
<br>
![화면설계서 pptx (2)](https://github.com/user-attachments/assets/8d0957c2-1618-46d9-b8a5-3a57d3dffb4f)
<br>
![화면설계서 pptx (3)](https://github.com/user-attachments/assets/1234adbf-53dc-4825-a1d5-5d64492bfc81)
<br>
![화면설계서 pptx (4)](https://github.com/user-attachments/assets/7c8b780a-b731-4b83-9a1d-f1316bc8297e)
<br>
![화면설계서 pptx (5)](https://github.com/user-attachments/assets/96583ecc-c6f7-4152-9b8c-dd531787220c)
<br>
![화면설계서 pptx (6)](https://github.com/user-attachments/assets/7094ab7d-ae94-4e92-b7c3-958310135c29)
<br>
![화면설계서 pptx (7)](https://github.com/user-attachments/assets/8f000a9f-3adb-4a03-bdb5-86038c7e54f7)
<br>
![화면설계서 pptx (8)](https://github.com/user-attachments/assets/ec89c16f-4e9b-4706-830c-f42d5ac9fc39)
<br>
![화면설계서 pptx (9)](https://github.com/user-attachments/assets/3d5e3c13-f727-4dbd-80dc-02a5da43267c)
<br>
![화면설계서 pptx (10)](https://github.com/user-attachments/assets/7abd34cc-528b-4df0-9baa-c1bc3f9ec738)
<br>
![화면설계서 pptx (11)](https://github.com/user-attachments/assets/b606a547-f8a7-48bd-8653-4d8c79ab41f1)
<br>
![화면설계서 pptx (12)](https://github.com/user-attachments/assets/69cef03c-07ca-441b-afd3-4f4e7c68bce9)
<br>
![화면설계서 pptx (13)](https://github.com/user-attachments/assets/3f0894a3-b5e7-4f84-beb6-9b6ddc9ddc7d)
<br>
![화면설계서 pptx (14)](https://github.com/user-attachments/assets/c543cd51-837c-4957-9693-15b971558a5a)
<br>
![화면설계서 pptx (15)](https://github.com/user-attachments/assets/944d2ded-92bd-4ccd-b365-740a026e6991)
<br>
![화면설계서 pptx (16)](https://github.com/user-attachments/assets/cbdb516d-a1d9-404e-8f49-15e2fe825431)
<br>
![화면설계서 pptx (17)](https://github.com/user-attachments/assets/fe43ac6e-d02e-4838-a1ad-ef33fa63d242)
<br>
![화면설계서 pptx (18)](https://github.com/user-attachments/assets/151fb4ff-3c5c-496b-b7a4-eda3439b3d7d)
<br>
</details>

---

## 07. WBS (작업 분배표)

![스크린샷 2025-04-21 094425](https://github.com/user-attachments/assets/62cb8525-24d5-4e90-9654-cb7dc5f02f94)

---

## 08. 테스트 계획 및 결과

- 주요 기능별 테스트 시나리오 작성  
- 정상 입력/비정상 입력 대응 여부 확인  

### ✅ 비정상 입력
![스크린샷 2025-04-21 112223](https://github.com/user-attachments/assets/39e9ab28-07ab-4c90-8f4d-ed3d7bd18aa1)

  - 입력하지 않은 요소에 대한 안내문구 반환

---

## 09. 수행 결과
### ✅ 홈 
* 홈 및 로그인
![127 0 0 1_8080_](https://github.com/user-attachments/assets/8ffd8a12-fedb-4db1-a1e2-2167b6763d40)

<br>

### ✅ 회원가입
* 회원 가입
![screencapture-127-0-0-1-8080-join-2025-04-21-11_08_03](https://github.com/user-attachments/assets/73126b48-ac79-4dc1-b95d-d7c1c54061cb)

<br>

* 이메일 인증
![screencapture-127-0-0-1-8080-join-2025-04-21-11_08_22](https://github.com/user-attachments/assets/097584b5-bcf3-45a4-a9b8-c0161226068f)

<br>

* 비밀번호 찾기
![screencapture-127-0-0-1-8080-password-2025-04-21-11_12_23](https://github.com/user-attachments/assets/5b273710-2743-4c9e-b4c2-eb163637b360)

<br>

### ✅ 사용자 정보 입력 
* 사용자 정보 입력 및 수정
![screencapture-127-0-0-1-8080-info-2025-04-21-11_07_35](https://github.com/user-attachments/assets/27f81708-f55e-4722-82b8-8b274b01357b)

<br>

### ✅ 채팅 
* 비회원 채팅

<br>

* 회원 채팅
<br>
---

## 10. 한 줄 회고

- ❤ **김하늘**  
  - 처음엔 막막했지만, 우리만의 결과물을 만든 경험이 소중했습니다.

- 💜 **박유진**  
  - 기획부터 배포까지 전 과정을 경험하며,  **서비스가 왜 필요한지, 누구에게 어떤 가치를 줄 수 있는지를 이해하는 것이 가장 핵심**적임을 깨달았습니다. 이를 위해 **사용자 입장에서 문제를 정의하고 해결책**을 고민해보며, 결과적으로 기획·설계·개발·배포가 어떻게 **유기적으로 맞물리는지 실감**할 수 있었습니다.

- 💙 **박주은**  
  - AI가 법률 서비스를 돕는 방법을 직접 구현하며 자신감이 생겼어요.

- 💚 **유지은**  
  - 팀원들과 협업하며 빠르게 MVP를 만드는 경험이 뜻깊었어요.

---
