# MY-OSS
개인과제 저장소

use studydb;

-- 주소록(이름, 전화번호, 주소, 생일)

DROP TABLE 주소록;

-- 주소록 테이블 생성
CREATE TABLE 주소록(
    번호    int auto_increment,
    이름        char(10)           NOT NULL ,
    전화번호  char(13) ,
    주소        varchar(10) ,
    생일        varchar(11) ,
    PRIMARY KEY(번호)
);

-- 데이터 입력
-- 주소록(이름, 전화번호, 주소, 생일)

INSERT INTO 주소록
VALUES('홍길동','010-1234-5678','서울','3월 15일');

INSERT INTO 주소록
VALUES('이몽룡','010-3354-5643','부산','12월 14일');

INSERT INTO 주소록
VALUES('최용만','321-2345','대전','5월 8일');

INSERT INTO 주소록(이름,전화번호)
VALUES('이건우','010-2132-2345');

-- 데이터 조회
select * from 주소록;

