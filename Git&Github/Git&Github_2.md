## Memo

포인터는 현재 내가 위치한 공간(ex. master → chat)

`git switch` 포인터 변경

별표(*)가 있는 공간(헤드(head))이 현재 위치한 포인터

`git log —oneline —all` 로그의 모든 것을 보여주는 명령어

`git log —oneline —all —graph` 그래프까지 보여주는 명령어

브랜치(branch)는 원본을 보존한 상태에서 새로운 변화들을 시도하기 위한 공간이라고 보면 됨

`git merge ~` 자동으로 브랜치를 master에 합쳐주는 명령어

`git branch -d` 특정 브랜치 제거해주는 명령어

※ merge 하려면 브랜치에서 바로 안 되고 master로 이동한뒤에 가능!!

`git branch -D` merge되지 않은 브랜치를 삭제하는 명령어

`git switch -c ~` 스위치하고 헤드(head)도 바꾸는 명령어

※ 커밋 메세지 변경하면 커밋 해쉬값 자체가 바뀌기 때문에 전체 충돌 발생함 (가능은 하되 왠만하면 협업 상황에선 바꾸지 말 것)

tip) log의 옵션 순서는 상관없음

터미널 오류 발생시 엔터 쭉 누르거나 'q' 누르면 빠져나옴