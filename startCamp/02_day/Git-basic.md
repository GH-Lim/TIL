# Git

## 기본 명령어

1. Git 저장소 설정

   ```
   $ git init
   ```

   주의! 반드시 현재 디렉토리에 git을 사용하고 있는지, (master) 표기가 없는지 확인할 것!

2. git add

   `git add` 는 현재 working directory 에서 commit 할 목록에 파일들을 담아놓는 것이다.

   그리고 그 목록은 `Index(staging area)` 라고 한다.

   `$ git add <폴더이름 혹은 파일이름>` 최상위에서 `git add .` 하면 디렉토리 전체 add

3. git commit

   현재 소스코드 상태를 저장하는 것, **스냅샷**을 찍는 것과 동일하다.

   `staging area` (git add 로 추가한 파일들이 담기는 곳) 에 있는 내용을 이력으로 기록한다.

   ```
   $ git commit -m "커밋 메세지"
   ```

4. git status

   git의 현재 상태를 확인한다.

   커밋할 목록에 담겨있는지 혹은 untracked 인지, 커밋할 내역이 있는지 등등 다양한 정보를 제공한다.

   ```
   $ git status
   ```

5. git log

   현재까지 커밋된 모든 이력을 확인할 수 있다.

   ```
   $ git log
   ```

## 원격 저장소 활용하기

1. 원격 저장소 (remote repository) 등록하기

   ```
   $ git remote add origin __경로__
   ```

   원격 저장소 (remote) 를 등록한다. origin 이라는 이름으로!

   최초에 한 번만 등록하면 된다.

   아래의 명령어로 현재 등록된 원격 저장소를 확인할 수 있다.

   ```
   $ git remote -v
   origin  https://github.com/GH-Lim/TIL.git (fetch)
   origin  https://github.com/GH-Lim/TIL.git (push)
   ```

2.  원격 저장소에 올리기

   ```
   $ git push origin master
   ```

   origin 이라는 원격 저장소의 master 브랜치로 지금까지의 커밋 내역을 올려줘!

3. 원격 저장소에서 가져오기

   ```
   $ git pull origin master
   ```

4. 원격 저장소를 로컬에 복사하기

   ```
   $ git clone __경로__
   ```

   다운받기를 원하는 폴더에서 git bash 를 열고 위의 명령어를 입력한다.

   경로는 github 에서 우측에 있는 초로객 버튼을 누르면 나타난다.



ref. https://backlog.com/git-tutorial/kr/