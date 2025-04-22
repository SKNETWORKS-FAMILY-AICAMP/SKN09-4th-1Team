# SK Networks AI CAMP 9기 - 4th 1Team: LawQuick

- **주제:** AI 활용 애플리케이션 개발  
- **개발 기간:** 2025.04.21 ~ 2025.04.22  

---

## 📌 목차

- [01. 팀 소개](#01-팀-소개)
- [02. 프로젝트 개요](#02-프로젝트-개요)
- [03. 기술 스택](#03-기술-스택)
- [04. WBS](#04-wbs)
- [05. 요구사항 정의서](#05-요구사항-정의서)
- [06. 화면설계서](#06-화면설계서)
- [07. 시스템 구성도](#07-시스템-구성도)
- [08. 테스트 계획 및 결과](#08-테스트-계획-및-결과)
- [09. 수행 결과](#09-수행-결과)
- [10. 결론](#10-결론)
- [11. 한 줄 회고](#11-한-줄-회고)

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
### ✅ 프로젝트 소개: 이혼 특화 AI 법률 상담 웹 서비스  

LawQuick은 자신의 상황에 맞는 법률 정보를 보다 쉽게 이해하고 활용할 수 있도록 지원하는  
이혼 특화 맞춤형 초기 법률 상담 웹 서비스입니다.  
**변호사를 만나기 전, 누구나 쉽게 시작할 수 있는 법률 상담의 출발점이 되는 것을 목표로 합니다.**

### ✅ 프로젝트 필요성

![image (5)](https://github.com/user-attachments/assets/9278a929-ee80-4aa8-b479-7b1c45dd8b75)  
![image (6)](https://github.com/user-attachments/assets/5c91008a-dcb5-4d09-a6f6-0404a3573b4f)  

출처: [https://www.mk.co.kr/news/society/9878764](https://www.mk.co.kr/news/society/9878764)

- 나홀로 소송은 늘고 있지만, 법률 정보는 전문 용어와 구조로 인해 일반인이 해석하기 어려움  
- 초기 상담은 높은 비용, 정보 노출에 대한 부담, 접근 방법의 어려움으로 이어지기 어려운 구조  

➡️ 단순한 정보 제공을 넘어, **개인 상황을 반영한 맞춤형 초기 상담 서비스의 필요성 대두**  


### ✅ 프로젝트 목표: 맞춤형 초기 법률 상담을 누구나, 쉽게

- 사용자 정보 기반 상담 흐름 구성  
- 상황에 맞는 법률 조항 및 판례 제공  
- 웹 기반 접근 환경 구현 (Django + Docker + AWS EC2)  

<br>

---

## 03. 기술 스택

| 카테고리 | 기술 스택 |
|----------|-------------------------------------------|
| **사용 언어** | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **프레임워크** | ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white) |
| **LLM 연동** | ![OpenChat](https://img.shields.io/badge/OpenChat-FFB000?style=for-the-badge&logo=OpenAI&logoColor=white) ![LangChain](https://img.shields.io/badge/LangChain-005F73?style=for-the-badge&logo=Chainlink&logoColor=white) |
| **벡터 데이터베이스** | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge&logo=Apache&logoColor=white) |
| **임베딩 모델** | ![OpenAI Embeddings](https://img.shields.io/badge/OpenAI%20Embeddings-8C9E90?style=for-the-badge&logo=OpenAI&logoColor=white) |
| **모델 튜닝/학습 프레임워크** | ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white) ![Transformers](https://img.shields.io/badge/Transformers-FFCC00?style=for-the-badge&logo=HuggingFace&logoColor=black) ![LoRA](https://img.shields.io/badge/LoRA-F76D57?style=for-the-badge&logo=HuggingFace&logoColor=white) |
| **UI/프론트엔드** | <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> |
| **실행 환경** | ![RunPod](https://img.shields.io/badge/RunPod-FF4500?style=for-the-badge&logo=Render&logoColor=white) ![AWS EC2](https://img.shields.io/badge/AWS%20EC2-FF9900?style=for-the-badge&logo=Amazon%20AWS&logoColor=white) |
| **배포 및 컨테이너** | ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker--Compose-1488C6?style=for-the-badge&logo=Docker&logoColor=white)  |
| **DB 및 기타** | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=white) ![python-decouple](https://img.shields.io/badge/python--decouple-3776AB?style=for-the-badge&logo=Python&logoColor=white) |
| **형상 관리 및 협업** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white) ![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=for-the-badge&logo=Google%20Drive&logoColor=white) |
| **테스트** | ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3) |

---
## 04. WBS 

![WBS](https://github.com/user-attachments/assets/06075e8d-6e51-4b4d-9785-3c9b66e2fe26)


---

## 05. 요구사항 정의서

![요구사항명세서](https://github.com/user-attachments/assets/111238bb-4b6e-4931-a03d-cd3aa1270de9)


**✅ 사용자 관련 요구사항:**
사용자는 로그인, 회원가입, 개인정보 입력, 개인정보 수정을 할 수 있어야 한다.

**✅ 채팅 관련 요구사항:**
사용자는 lawquick 시스템을 통해 질의응답 채팅을 할 수 있어야 한다.

**✅ 히스토리 관련 요구사항:**
사용자의 채팅 기록은 저장, 접근가능해야한다.


---


## 06. 화면설계서

[✅ 화면 설계서 바로가기](https://docs.google.com/presentation/d/15zIH85hUu1HvVMs0SRh4gG68GQS3g5Tn/edit?usp=sharing)

<details>
<summary>전체 화면 설계서</summary>
<br>
  
**- 메인 홈 화면**
![화면설계서 pptx(0)](https://github.com/user-attachments/assets/00706779-513f-43b0-a752-57a5d471dedf)
<br>


**- 비밀번호 찾기**
![화면설계서 pptx (1)](https://github.com/user-attachments/assets/430c263e-c086-4c54-95a3-93a6bac7d601)
![화면설계서 pptx (2)](https://github.com/user-attachments/assets/d88cbcb9-6b36-4831-a976-731faf2bfac5)
![화면설계서 pptx (3)](https://github.com/user-attachments/assets/69a868eb-13c7-4c93-893f-5cc36264a98b)
<br>


**- 회원가입**
![화면설계서 pptx (4)](https://github.com/user-attachments/assets/e8332b08-c219-4dbb-b973-5fceae8eb5cf)
![화면설계서 pptx (5)](https://github.com/user-attachments/assets/b9675601-927b-476e-ab01-ee6665b0a765)
![화면설계서 pptx (6)](https://github.com/user-attachments/assets/881564bb-08e8-4fd4-8d04-a3c1d2beb89f)
![화면설계서 pptx (7)](https://github.com/user-attachments/assets/a26d6c9f-3656-4dd0-9fc4-d2ee1fd45aea)
![화면설계서 pptx (8)](https://github.com/user-attachments/assets/9c47c3d7-b7da-43d5-a342-45d6c7b748f5)
<br>


**- 비회원 채팅**
![화면설계서 pptx (9)](https://github.com/user-attachments/assets/a99f9e9e-7946-4c0a-8115-913194646644)
![화면설계서 pptx (14)](https://github.com/user-attachments/assets/d7c7218d-8d5d-4095-be75-4241405ae766)
![화면설계서 pptx (15)](https://github.com/user-attachments/assets/dc0caf12-a059-43bd-ab7a-f4c223045d7c)
<br>


**- 회원 채팅**
![화면설계서 pptx (10)](https://github.com/user-attachments/assets/d963cb88-c871-4b78-b5e0-7c57d61b1fc6)
![화면설계서 pptx (12)](https://github.com/user-attachments/assets/a26b2a49-80e2-4159-b72f-ea4c3fc35bfe)
![화면설계서 pptx (13)](https://github.com/user-attachments/assets/52a53ad7-a0e9-40c3-82f7-a7e226d7ae6f)
<br>


**- 개인정보 입력**
![화면설계서 pptx (16)](https://github.com/user-attachments/assets/185f2f3a-275c-40b8-be8a-3d947e87af47)
![화면설계서 pptx (17)](https://github.com/user-attachments/assets/2ee1972f-084d-42a3-af81-228b59b39eb6)
![화면설계서 pptx (18)](https://github.com/user-attachments/assets/b158180b-adb9-4c5a-b024-37ba6579d3a2)
<br>




<br>
</details>


<details>
<summary>서비스 플로우</summary>
<br>

User Flow
![USER-flow](https://github.com/user-attachments/assets/d21862a6-06b3-4a89-b0bd-18879b4b9806)


Wire Flow
![wire_flow](https://github.com/user-attachments/assets/fae1fd03-b7d5-4e5b-86f7-b3b6d48c87ef)
</details>

---
## 07. 시스템 구성도

![시스템 아키텍처](https://github.com/user-attachments/assets/5f4d87ca-7085-40b8-b788-5b2af3c50959)

### ✅ ERD
![ERD_white](https://github.com/user-attachments/assets/57eb2498-c140-402f-8297-00b559ab0530)


<details>
<summary><strong>ERD 상세</strong></summary>

#### User 테이블

| 필드명       | 타입     | 설명                             |
|--------------|----------|----------------------------------|
| `id`         | UUID     | 사용자 식별자 (Primary Key)       |
| `email`      | varchar  | 사용자 이메일                     |
| `password`   | varchar  | 사용자 비밀번호                   |
| `is_verified`| boolean  | 이메일 인증 여부                  |
| `created_at` | datetime | 생성 일시                         |


#### UserInfo 테이블

| 필드명             | 타입     | 설명                                       |
|--------------------|----------|--------------------------------------------|
| `user_id`          | UUID     | User와 1:1 관계 (Foreign Key)               |
| `created_at`       | datetime | 생성 일시                                   |
| `marital_skipped`  | boolean  | 혼인 정보 건너뛰기 여부                     |
| `marital_status`   | varchar  | 혼인 상태                                   |
| `marriage_duration`| varchar  | 혼인 기간                                   |
| `divorce_status`   | varchar  | 이혼 의사 여부                              |
| `children_skipped` | boolean  | 자녀 정보 건너뛰기 여부                     |
| `has_children`     | boolean  | 자녀 유무                                   |
| `children_ages`    | text     | 자녀 나이 정보                              |
| `other_skipped`    | boolean  | 기타 정보 건너뛰기 여부                     |
| `property_range`   | varchar  | 재산 범위                                   |
| `experience`       | varchar  | 가정폭력 등 경험 여부                       |
| `detail_skipped`   | boolean  | 상세 고민 건너뛰기 여부                     |
| `detail_info`      | text     | 상세 고민 내용                              |


#### Chat 테이블

| 필드명       | 타입     | 설명                               |
|--------------|----------|------------------------------------|
| `id`         | int      | 채팅 식별자 (Primary Key)           |
| `user_id`    | UUID     | User와 N:1 관계 (Foreign Key)       |
| `chat_title` | text     | 채팅 제목                           |
| `created_at` | datetime | 생성 일시                           |



#### Message 테이블

| 필드명       | 타입     | 설명                               |
|--------------|----------|------------------------------------|
| `id`         | int      | 메시지 식별자 (Primary Key)         |
| `chat_id`    | int      | Chat과 N:1 관계 (Foreign Key)       |
| `sender`     | varchar  | 보낸 사람 (user 또는 bot)           |
| `message`    | text     | 메시지 내용                         |
| `created_at` | datetime | 생성 일시                           |
| `duration`   | float    | 응답까지 걸린 시간 (초 단위)       |


#### 테이블 간 관계

| 관계       | 설명                                                |
|------------|-----------------------------------------------------|
| `User` 1 : 1 `UserInfo` | 한 명의 사용자는 하나의 사용자 정보만 가짐     |
| `User` 1 : N `Chat`     | 한 명의 사용자는 여러 개의 채팅 가능           |
| `Chat` 1 : N `Message`  | 하나의 채팅은 여러 메시지를 포함 가능           |

</details>


---




## 08. 테스트 계획 및 결과
  
### ✅ 테스트 계획 및 대상
**User 관련 기능**
- 로그인 기능을 테스트한다.
- 로그아웃 기능을 테스트한다.
- 이메일 인증 기능을 테스트한다.
- 비밀번호 찾기 기능을 테스트한다.
- 회원가입 절차를 테스트한다.
- 약관 동의 흐름을 테스트한다.
- 비밀번호 유효성 검사를 테스트한다.
- 개인정보 입력 기능을 테스트한다.
  
**Chat 관련 기능**
- 질문/답변 채팅 기능을 테스트한다.
- 채팅 이력 조회 및 제목 수정, 삭제 기능을 테스트한다.

### ✅ 테스트 결과
![스크린샷 2025-04-21 163346](https://github.com/user-attachments/assets/1ae7eff6-d92c-4a6c-a6f1-0316c0dc9725)

### ✅ 비정상 입력 케이스 테스트 결과

* 로그인 
![스크린샷 2025-04-21 1249040](https://github.com/user-attachments/assets/537b96e7-71fd-44d9-8685-b2a8710a3bef)
  - 로그인 불가 이유에 대한 안내문구 출력

* 회원가입
![screencapture-127-0-0-1-8080-join-2025-04-21-12_49_17](https://github.com/user-attachments/assets/821aa24b-b11b-432b-9fe4-3ad7e7221042)
  - 아이디, 비밀번호 조건에 대한 안내문구 출력
  
* 사용자 정보 입력
![스크린샷 2025-04-21 112223](https://github.com/user-attachments/assets/39e9ab28-07ab-4c90-8f4d-ed3d7bd18aa1)
  - 입력하지 않은 요소에 대한 안내문구 반환

---

## 09. 수행 결과

### ✅ [LawQuick 바로가기](http://13.124.112.16:8080/)
### ✅ [시연 영상 바로가기](https://drive.google.com/file/d/1dyJHXgsPC0OkCOy3LDAB9vCKWf1qrwtA/view?usp=drive_link)

<br>

### ✅ 홈 
**홈 및 로그인**
![screencapture-127-0-0-1-8080-2025-04-21-14_22_49](https://github.com/user-attachments/assets/850ab2a3-5627-4dc3-ac4d-20bdceb52b5a)

<br>

### ✅ 회원가입
**회원 가입**
![회원가입](https://github.com/user-attachments/assets/4e77c5a4-5e75-4dc7-af7f-f84831572bfd)

<br>

**이메일 인증**
![이메일 인증](https://github.com/user-attachments/assets/52fbaebb-535b-4fed-9b10-5f661d8dcebc)

<br>

**비밀번호 찾기**
![screencapture-127-0-0-1-8080-password-2025-04-21-11_12_23](https://github.com/user-attachments/assets/5b273710-2743-4c9e-b4c2-eb163637b360)

<br>

### ✅ 사용자 정보 입력 
**사용자 정보 입력 및 수정**
![screencapture-127-0-0-1-8080-info-2025-04-21-11_07_35](https://github.com/user-attachments/assets/27f81708-f55e-4722-82b8-8b274b01357b)

<br>

### ✅ 채팅 
**비회원 채팅**
![비회원_채팅_첫화면](https://github.com/user-attachments/assets/4cd307d8-626d-4935-9523-30a2d0d08be6)
<br>

**비회원 사이드바**
![비회원_채팅](https://github.com/user-attachments/assets/ed0f1ece-0dc8-4ca7-a268-fb99329f2938)

<br>

**회원 채팅**
![회원_채팅](https://github.com/user-attachments/assets/7f24ad26-fe90-4602-a1b1-997104e27e42)
<br>

**회원 사이드바**
![회원채팅_히스토리](https://github.com/user-attachments/assets/df402ee4-7a92-4d49-9f83-363f1f8af2c6)

<br>

---

## 10. 결론

**✅ 프로젝트 요약**  
이혼에 특화된 AI 상담 챗봇 **LawQuick**을 개발하여, 정보 입력부터 상담, 히스토리 저장까지 가능한 웹 기반 초기 법률 상담 서비스를 완성함.

**✅ 프로젝트 기대효과**
- **상담 접근성 향상:** 변호사 상담 전, 누구나 쉽게 초기 상담 가능
- **비용 부담 완화:** 맞춤형 상담 제공으로 소송 전 정보 격차 해소
- **맞춤형 정보 제공:** 사용자 상황에 맞는 법률 조항 및 판례 안내
- **서비스 확장 가능성 확보:** 유연한 구조로 다른 법률 분야 적용 가능

**✅ 프로젝트 개선 방향**
- **사용자 피드백 기반 고도화** 
- **모델 응답 속도 최적화**  
- **모듈 분리 및 유지보수성 강화**  
 
<br>

---

## 11. 한 줄 회고

- ❤ **김하늘**  
  - Django 기반 이혼 법률 AI 챗봇을 Docker 및 RunPod 환경에서 설계·배포하고, EC2–RDS 연동하면서 실 서비스 수준의 백엔드 개발 및 배포 기술을 종합적으로 다루고 체득한 경험이었습니다.

- 💜 **박유진**  
  - 기획부터 배포까지 전 과정을 경험하며,  **서비스가 왜 필요한지, 누구에게 어떤 가치를 줄 수 있는지를 이해하는 것이 가장 핵심**적임을 깨달았습니다. 이를 위해 **사용자 입장에서 문제를 정의하고 해결책**을 고민해보며, 결과적으로 기획·설계·개발·배포가 어떻게 **유기적으로 맞물리는지 실감**할 수 있었습니다.

- 💙 **박주은**  
  - Docker를 이용해 FastAPI 모델 서버를 컨테이너화하면서, 환경 일관성 확보의 중요성과 Docker의 유용성을 알게 되었습니다. 이 경험을 통해 Django와 FastAPI 서버를 분리해도 안정적으로 배포 및 실행이 가능함을 직접 확인할 수 있었습니다.

- 💚 **유지은**  
  - 실제 이혼 상담 흐름을 구현하기 위해 프론트와 백엔드를 유기적으로 연결하며 실무형 챗봇을 완성해가는 과정이 인상 깊었습니다. 사용자 중심의 UX 설계와 법률 도메인 특화 AI 개발이 함께 성장한 값진 경험이었습니다.

---
