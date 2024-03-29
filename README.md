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

#### 이미지 업로드 api 중 어려움
* 처음으로 이미지 업로드 기능을 맡았는데, 아직 문제 해결을 어떻게 해야하는지 전혀 알지 못하던 때라 힘들었습니다. 
* 검색 실력도 부족했는데 어떻게든 이 기능만큼은 민폐 끼치지 말고 내가 해결하고 싶다는 마음에 [stackoverflow에 게시글](https://stackoverflow.com/questions/72134647/how-to-send-form-data-to-mongodb-using-flask)을 올리기까지 했습니다. 
* 결과적으로 5일이라는 긴 시간이 걸렸습니다만, 깔끔하게 이미지를 프론트에서 백으로 보내고 시간을 파일명에 넣어 서버에 저장하는 과정을 성공해냈습니다.


#### 게시글 타임스탬프 로직
* 제가 처음으로 짠 로직입니다.
* 발표 전날 밤을 샜고 아침 6시에 완성했습니다.
![code768](https://user-images.githubusercontent.com/104334219/186160627-c9addc0d-4611-4521-b2d5-5ed01e7beea8.png)



## 6. 성장 & 회고
처음으로 내 손으로 검색을 하고 내 머리로 로직을 짜고 코드를 짜면서, 진심으로 코딩이 즐겁다 짜릿하다는 감각을 느꼈습니다. <br>
이후 본격적으로 백엔드를 잘하고 싶다는 생각을 하게 되었고,<br> 
그 마음으로 매일 쉬는 시간을 최소화하면서 공부에 매진할 수 있었던 것 같습니다.<br> 
가장 기초적인 기술이 구현된 프로젝트이지만 앞으로 개발자의 길을 걸으면서 항상 떠오를 것 같은 프로젝트입니다.
