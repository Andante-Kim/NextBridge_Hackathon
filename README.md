# Next Bridge

지방 소멸 문제를 해결하기 위해, 외국인 노동자의 안정적인 정착을 돕는 구인구직 및 커뮤니티 플랫폼입니다.

## 소개
한국의 지방 소멸 문제는 인구 유출과 낮은 경제적 기회에서 비롯됩니다. 저희 팀은 지방의 주요 노동력인 외국인 노동자들이 한국 사회에 더 안정적으로 정착할 수 있도록 돕기 위해 Next Bridge를 개발했습니다.

## 주요 기능
1. **🔑 로그인 및 회원가입**
   - 사용자 친화적인 계정 생성 및 로그인 기능.

2. **💬 커뮤니티 게시판**
   - 한국 생활 정보 및 노하우를 공유하는 공간.
   - 비자 연장, 의료 서비스 등 실질적인 정보 제공.
   - 프로필 관리 기능.

3. **📄 구인구직 공고**
   - 지방 일자리를 쉽게 찾을 수 있는 채용 공고 검색 기능.
   - 지역 및 업종별 필터링.

4. **⭐ 후기 공유 시스템**
   - 기업 및 직장 환경에 대한 후기 작성 및 공유.
   - 투명성을 높이고 더 나은 선택을 돕는 시스템.

## 기대 효과
- ** 사회적 효과**: 지방 활성화 및 외국인 노동자의 안정적인 정착 지원.
- ** 경제적 효과**: 지방 인력 문제 해결 및 지역 경제 강화.
- ** 정책적 활용성**: 정부 및 지방 자치 단체와 협력 가능성 증대.

## 스크린샷

### 홈 페이지/ 커뮤니티 게시판
<img src="https://github.com/user-attachments/assets/8428678e-f34e-4808-9ebb-84863cc0a39b"  width="80%" height="80%">

### 구인구직 페이지
<img src="https://github.com/user-attachments/assets/c8ebdfd6-c6f2-4c6e-99f5-722d3a305381"  width="80%" height="80%">

### 커뮤니티 게시판
<img src="https://github.com/user-attachments/assets/2bd928a4-c1b4-4368-bfc2-dc8834e4c15e" width="80%" height="80%">
<img src="https://github.com/user-attachments/assets/3bd03019-82de-4b4b-a7ae-d64adfbbd7d0" width="80%" height="80%">

## 기술 스택
- **Frontend**: HTML, CSS, JavaScript (+Bootstrap)
- **Backend**: Python Django (+Kakao Maps API)
- **Database**: SQLite (+Selenium, BeautifulSoup)
- **Design**: Figma
- **Version Control**: GitHub

## 팀 소개
- **팀명**: Next Bridge
- **성과**: 덕성여자대학교 디지털소프트웨어학과 해커톤 2등 수상
- **역할 분담**: 기획, 디자인, 프론트엔드 및 백엔드 개발

## 설치 방법
다음 단계를 따라 로컬 환경에 이 프로젝트를 설치하세요:

1. **저장소 클론**:
   ```bash
   git clone https://github.com/Andante-Kim/NextBridge_Hackathon.git
   ```

2. **프로젝트 디렉토리로 이동**:
   ```bash
   cd NextBridge_Hackathon
   ```

3. **가상 환경 생성 및 활성화** (선택 사항):
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate   # Windows
   ```

4. **필수 패키지 설치**:
   ```bash
   pip install -r requirements.txt
   ```

5. **마이그레이션 적용**:
   ```bash
   python manage.py migrate
   ```

6. **개발 서버 실행**:
   ```bash
   python manage.py runserver
   ```

7. 브라우저에서 `http://127.0.0.1:8000`을 열어 웹사이트를 확인합니다.

## 기여 방법
1. 저장소를 **포크**합니다.
2. 새로운 **브랜치**를 생성합니다. (`git checkout -b feature/AmazingFeature`)
3. 변경 사항을 **커밋**합니다. (`git commit -m 'feat: AmazingFeature 추가'`)
4. 브랜치에 **푸시**합니다. (`git push origin feature/AmazingFeature`)
5. **풀 리퀘스트**를 생성합니다.
6. 리뷰 후 피드백에 따라 수정합니다.

---

## 라이선스
이 프로젝트는 [MIT 라이선스](./LICENSE)를 따릅니다.

---

# Next Bridge

A recruitment and community platform to support the stable settlement of foreign workers and address the issue of regional depopulation in South Korea.

## Introduction
The regional depopulation problem in South Korea stems from population outflows and limited economic opportunities. Our team developed Next Bridge to assist foreign workers, a key labor force in regional areas, in settling more stably in South Korean society.

## Key Features
1. **🔑 Login and Registration**
   - User-friendly account creation and login functionality.

2. **💬 Community Board**
   - A space to share life tips and know-how about living in Korea.
   - Provides practical information like visa extensions and healthcare services.
   - Profile management feature.

3. **📄 Job Postings**
   - Job search functionality for regional employment opportunities.
   - Filtering by location and industry.

4. **⭐ Review Sharing System**
   - Allows users to leave and share reviews about companies and work environments.
   - Enhances transparency and supports better decision-making.

## Expected Impact
- ** Social Impact**: Promotes regional revitalization and supports the stable settlement of foreign workers.
- ** Economic Impact**: Addresses manpower shortages in rural areas and strengthens the local economy.
- ** Policy Application**: Increases collaboration potential with government and local authorities.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript (+Bootstrap)
- **Backend**: Python Django (+Kakao Maps API)
- **Database**: SQLite (+Selenium, BeautifulSoup)
- **Design**: Figma
- **Version Control**: GitHub

## Team Introduction
- **Team Name**: Next Bridge
- **Achievement**: 2nd place at the Hackathon hosted by Duksung Women’s University Department of Digital Software.
- **Roles**: Planning, design, frontend, and backend development.

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Andante-Kim/NextBridge_Hackathon.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd NextBridge_Hackathon
   ```

3. **Create and activate a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # MacOS/Linux
   venv\Scripts\activate   # Windows
   ```

4. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

7. Open `http://127.0.0.1:8000` in your browser to view the website.

## How to Contribute
1. **Fork** the repository.
2. Create a new **branch**. (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes. (`git commit -m 'feat: Add AmazingFeature'`)
4. **Push** the branch. (`git push origin feature/AmazingFeature`)
5. Create a **Pull Request**.
6. Address feedback and make necessary changes.

---

## 📜 License
This project is licensed under the [MIT License](./LICENSE).
