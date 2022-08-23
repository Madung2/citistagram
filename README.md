# 📌Citistagram

![citi](https://user-images.githubusercontent.com/104334219/186140240-bba26bbc-77a3-475c-bbba-fb2d6bfd9ede.gif)


- 인스타그램 클론 코딩 프로젝트

## 1. 제작 기간 & 참여 인원
- 2022.05.03 ~ 2022.05.11
- 팀 프로젝트(4명)

## 2. 사용 기술

![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f48544d4c352d4533344632363f7374796c653d666c61742d737175617265266c6f676f3d48544d4c35266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452723-565e4f8e-8ed5-40c7-b41e-e71a7fd636cf.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f435353332d3135373242363f7374796c653d666c61742d737175617265266c6f676f3d43535333266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452778-6bf21e33-989f-4759-93ef-dbb0862fffee.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a6176617363726970742d4637444631453f7374796c653d666c61742d737175617265266c6f676f3d4a617661736372697074266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452783-bb2e89d4-fb58-48fe-86c5-d639d495602f.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4a51756572792d3037363941443f7374796c653d666c61742d737175617265266c6f676f3d4a5175657279266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452788-1665e841-a475-4170-97b8-374d2f88f1d3.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466c61736b2d3030303030303f7374796c653d666c61742d737175617265266c6f676f3d466c61736b266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452818-ab80154e-ed6e-421b-97b9-feccb48dbff7.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d6f6e676f44422d3437413234383f7374796c653d666c61742d737175617265266c6f676f3d4d6f6e676f4442266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452826-c3351d4e-167c-4a76-b308-86addc8ca5b8.svg)
![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f416d617a6f6e204157532d3233324633453f7374796c653d666c61742d737175617265266c6f676f3d416d617a6f6e20415753266c6f676f436f6c6f723d7768697465](https://user-images.githubusercontent.com/100769423/166452833-ebd8d65a-adcc-44c0-9ced-45d1856df862.svg)

## 3. 아키텍쳐 및 ERD 설계

![image](https://user-images.githubusercontent.com/100769423/167077920-e6ff091a-7b7d-4ce8-b167-aa81824fa37d.png)

## 4. 핵심 기능
<details close>
  <summary>📌 메인페이지 </summary>
  * 게시물, 댓글 CRUD <br>
  * 좋아요<br>
  * 업로드 시간 표시
  * 랜덤 추천 친구 기능
</details>
<details close>
  <summary>📌마이 페이지</summary>
  * 팔로우 / 취소
  * 신고 기능
</details>
<details close>
  <summary>📌회원가입, 로그인</summary>
</details>


## 5. 핵심 트러블 슈팅

#### 검색창에 active 상태가 true면서, 게시 만료일이 지나지 않은 게시물 sorting 하는 방법 

* 검색창에서 쿼리를 날릴때, 3가지 조건, 검색어가 제목이나 작정자에 해당하면서도, active 상태가 true, 게시물 만료일이 지나지 않은 것을 검색할 필요가 있었습니다.

* 하지만 처음의 전 각각 따로 sorting 하는 방법밖에 떠오르지 않았고, 불필요한 쿼리를 줄이고 싶다고 생각하게 되었습니다.<br> 

* 이 시점쯤에 stackoverflow와 장고 도큐먼트를 좀 더 편하게 사용할 수 있게 되었는데,<br>
검색어로 'django filter', 'django queries'등을 검색한 결과 Q()를 사용해 3가지 조건을 연결을 할 수 있는 식을 세우게 되었습니다. 


![code1](https://user-images.githubusercontent.com/104334219/186073479-6e66c1c2-4770-4afb-b4df-692c4164fe7f.png)


## 6. 기타 트러블 슈팅

<details close>
  <summary>📌 Assertion Error</summary>
  assertion의 뜻은 '역설'이라는 말인데 개발자가 생각을 못한 문제가 에러가 생겼을때 뜨는 에러입니다.
  'AssertionError: Expected a Response, HttpResponse or HttpStreamingResponse to be returned from the view, but received a <class 'NoneType'>'이란 에러문구가 떴는데,
  Response를 원한다고 해서 백에서의 문제일거라 생각하고 하나하나 체크를 해봤는데 큰 문제가 없었습니다.
  다시 print를 찍어가며 차근차근 에러가 난 곳을 되짚어 가보니 back이 아닌 front 단에서 유저명이 겹치는 문제가 있었습니다.
</details>
    
<details close>
  <summary>📌 AI 적용시 시간 소요 문제 </summary>
    처음에는 'Dall-E'모델을 사용해서 text-to-image를 구현하려고 했습니다만, 모델이 많이 무거워서 우리같은 초보자들이 구현하기에는 어렵겠다 싶었고 조금 더 정확도가 떨어지더라도 실용 가능한 속도를 가진 <a href='https://colab.research.google.com/drive/1TBo4saFn1BCSfgXsmREFrUl3zSQFg6CC'>'diffusion'</a>모델을 사용하게 되었습니다. 
    pytorch를 사용할때 그래픽카드에 맞는 쿠다 버전을 다운받아 사용하는 것도 시간 단축에 큰 도움이 되었습니다.

</details>



## 7. 성장 & 회고
* 요즘 가장 핫한 ai 분야 중 하나인 'text to image'를 사용해 볼 수 있었던게 정말 즐거운 경험이 된것 같습니다. 
* 본격적으로 DRF를 사용한 첫 프로젝트 였는데 시리얼라이저를 쓰면서 좀더 클린한 코드를 쓰고 싶다는 욕심도 갖게 되었습니다. 이후 '파이썬 클린 코드'란 책을 읽으면서 조금씩 제 코드에 대입해 보고 있습니다. 

* 이 프로젝트를 하기 전까지 자바스크립트를 전혀 할 줄 몰랐습니다. 주변사람에 묻고 구글링을 하면서 하나의 프로젝트를 완성하고 나니 편안하게 기본적인 사이트 구성에 필요한 [자바스크립트](https://velog.io/@tasha_han_1234/exqg7cbz)를 쓸 수 있게 되었는데, 이 점도 스스로 뿌듯함을 느낄 수 있었던 부분 입니다.
