## 전체 내용 복습

`git remote add origin [원격 URL]` 원격 주소의 길을 만드는 명령어

※ clone할 때 기존 경로에 .git이 있는지 확인해야 함 (git으로 관리하는 디렉토리는 문제가 됨)

tip) init으로 진행한 래포지토리 푸는 방법 (해당 디렉토리의 .git을 삭제하면 됨)
→ `rm -r .git/`

`ls -a`  숨김파일까지 표시하는 명령어

원격 저장소에서 데이터 가져올 때
- 추가로 커밋을 업데이트하는 건 `pull`
- 전체를 다 가져오는 것 `clone`

충돌 시 3가지 경우
1. 다른 파일 수정 - 자동 합쳐짐
2. 같은 파일 다른 라인 - 자동 합쳐짐
3. 같은 파일 같은 라인 - 충돌 발생해서 수정 후 저장해야 함

브랜치 필요성: 별도의 작업 공간으로 오류 발생했을 때 대응하기 쉬워짐 (master는 상용화 되어 있음)

터미널 ‘:’ 의미 - 더 아래까지 있음 (엔터 여러 번 누르거나 'q' 누르면 해결)

저장(Ctrl+S)-add-commit이 하나의 사이클 but add만 해놓고 의미있는 변화를 저장할 때에만 commit해주면 됨

merge 안된 branch 삭제려면 -D 활용

브랜치 만들고 바로 변경하는 방법은 gitch switch -c ~

풀리퀘스트 작성할때 마크다운 작성 가능, 보통 특정 리뷰어 지정함

코멘트 작성하고 close 하면 풀리퀘스트 거절 가능

소유권이 없는 상태의 작업흐름

원본으로부터 개인 깃허브에 클론 생성(fork)하고 로컬에서 내 저장소로부터 클론 생성

로컬에서 기능 구현 변경

PR(Pull Request) 날린 게 머지(merge)되면 컨트리뷰터(Contributor)가 됨

upstream하는 이유 : 나중에 변화된 내용을 pull로 업데이트하기 위해서

git clone {내 원격 저장소 주소}만 해도 origin이 생기기 때문에 따로 remote add해줄 필요 없음

`cp -r(폴더 안의 내용까지 돌아가면서 복사해라) 원본/ 새폴더이름`

복구하는방법

1. 리셋하는법

git reset (리셋 옵션-soft,mixed,hard) (커밋해쉬값)

git reset —soft

스테이징에어리어는 변화없이 커밋으로 돌아감(스테이징에어리어로 되돌아감)

커밋을 리셋한거까지 확인하는 명령어

`git reflog`

`git reset --mixed`

워킹디렉토리 상태로 되돌아감

`git reset —hard`

워킹디렉토리에서조차 사라짐

1. revert

리버트는 커밋을 한 칸 더 쌓아준다고 보면 됨(리셋처럼 커밋로그가 사라지지도 않음-협업상황에서 활용도 높음)

언두잉(되돌리기)

[이미 커밋이 있는 경우] add시켜 놓은 거 다시 워킹디렉토리로 되돌려주는 명령어

`git restore --staged <file>`

커밋이 없는 경우

`git rm —cached <file>`

(꿀팁)하지만 외울 필요없이 그 상황에서 git status해주면 뭐쓸지 알려줌

따라서 습관처럼 `git status` 찍어주자

직전 커밋메세지 등 커밋 수정방법

git commit —amend

빔이 뜨고 i 눌러서 끼워넣기 모드 실행-수정가능-esc로 끼워넣기모드 빠져나오기-’:’에wq해주면 커밋 자체가 바뀌게 됨

case 1) staging area에 파일 없는 경우

커밋만 바뀜

case 2) 스테이징에어리어에 잇는 파일도 같이 git에 관리됨

working directory

언트랙티드된 파일을(in working directory) 

커밋에 저장된 수정전으로 되돌리기

`git restore <file>`

(이또한 git status에 나옴)

커밋 컨벤션

[https://udacity.github.io/git-styleguide/](https://udacity.github.io/git-styleguide/) 우다시티 사이트 참고

협업을 위해 커밋 코멘트에 대한 가독성 높이는 방법

메세지 구조 중에서 Type:Subject정도는 잘 써줄 것

rebase는 한줄로 깔끔하게 나옴 (협업할 때는 금지됨)

프로깃(모든 깃에 대한 정보 파악 가능)