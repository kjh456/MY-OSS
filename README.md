# MY-OSS
개인과제 
전달방식>

1. post

 - 헤더파일에 담겨져서 서버로 전송

 - get방식보다 보안이 강하다.

 - 전달 량도 get방식에 비해 많은 양 전달

  -post방식 한글처리 setCharacterEncoding(euc-kr)


2. get

-  주소입력줄에 표시되어 전달되어 보안에 미흡

- 주소입력줄에 표현할 수 있는 전달 량만 서버로 전송

  하기 때문에 post방식에 비해 전달량이 작다


-get방식의 한글처리방법

  server.xml 파일내에 대략 66번째 줄(위치 C:\Program Files\apache-tomcat-9.0.37\conf

     이클립스는 sercers 폴더 밑에 톰갯폴더 아래 있음.)


  <Connector port="8080".......

        URIEncoding="euc-kr"> </Connector>


