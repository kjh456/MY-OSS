# MY-OSS
개인과제 

-- 인공_데이터베이스(QC) (담당: 김희숙)  10주차 실습(stu)

-- (MySQL) safe mode 해제
SET SQL_SAFE_UPDATES = 0;

-- 테이블 구조 확인
DESC 테이블명;
==============================
/*------- 제약조건 확인(MySQL) ------ */
-- (MySQL) 제약조건 확인

-- 제약조건(부서, 사원)
SELECT * 
FROM  information_schema.table_constraints
WHERE table_name IN ('부서','사원');
/* -------------------------------------- */
==============================
10주차 (실습)

(w10)
[실습 1] SELECT (customer)
[실습 2] 집계함수, 그룹화 (성적, 성적2)
==============================
# (MySQL)
1단계: 데이터베이스 생성  studydb
    사용할 데이터베이스 선택
USE studydb;

2단계: 테이블 생성         customer,
                                   성적, 성적2
3단계: 데이터 입력

4단계: 데이터 조회
select * from customer;
--------------------------------------------------
[요약] SELECT 문법

# 연산자 우선순위
1. ( )
2. 논리 연산자: NOT > AND > OR
3. 관계 연산자:
         > ,  >= , = ,  != ,  <=  ,  <
                         <>
4. 산술 연산자: *,  /
                   +. -


-- 관계 연산자
초과  이상   같다   같지않다  이하  미만
>      >=    =       <> !=     <=     <

-- 논리 연산자: NOT,    AND,     OR
                                이고      이거나

-- 패턴 문자열: LIKE
%   0개 이상의 문자
_    1개 문자

LIKE ~와 같은, ~와 유사한

-- 정렬: ORDER BY 
     순서: 오름차순(ascending)    ASC
             내림차순(descending)  DESC
--------------------------------------------------

--------------------------------------------------
[실습 1] 데이터 조회(customer)

SELECT
FROM       customer
WHERE                ;

--------------------------------------------------
[실습 1] (SELECT 기초, NULL, LIKE, Order by)

-- customer(cno, cname, city, point)
-- 고객(고객번호, 고객명, 거주지, 포인트)

-- 1-1) 테이블의 모든 열을 검색하라

SELECT *
FROM       customer

-- 1-2) 테이블의 모든 열을 검색(필드명 사용)

SELECT     cno, cname, city, point
FROM       customer

-- 1-3) 고객의 고객명, 거주지를 검색하라(테이블의 특정 열을 검색)

SELECT    cname, city
FROM       customer

-- customer(cno, cname, city, point)
*-- 1-4) cname 은 성명, city는 거주지로 출력하라(화면에 표시되는 열 이름 변경하여 검색) 

SELECT    cname 성명, city 거주지
FROM       customer

-- 1-5) customer 테이블에서 거주지를 검색하라

SELECT    city
FROM       customer

*-- 1-6) 거주지를 검색하는데 중복 행을 제거하여 한 번씩만 검색하라
-- (DISTINCT 사용)

SELECT  DISTINCT city 
FROM       customer

-- customer(cno, cname, city, point)
-- 2-1) 고객번호가 c101 인 고객의 모든 정보를 검색하라

SELECT   *
FROM       customer
WHERE    cno = 'c101'  ;

-- 2-2) 포인트가 400 이하인 고객의 모든 정보를 검색하라

SELECT      *
FROM       customer
WHERE      point <= 400 ;

-- 2-3) 거주지가 서울 이면서 포인트가 500 이상인 고객의 이름, 거주지, 포인트를 검색하라

SELECT      cname, city, point
FROM       customer
WHERE      city = '서울'  AND  point >= 500 ;

-- 2-4) 거주지가 서울 이거나 포인트가 500 이상인 고객의 이름, 거주지, 포인트를 검색하라

SELECT      cname, city, point
FROM       customer
WHERE      city = '서울'  OR  point >= 500 ; 


-- customer(cno, cname, city, point)
--고객(고객번호, 고객명, 거주지, 포인트)

-- 2-5) 포인트가 350 부터 500 사이인 고객이름, 거주지, 포인트를 검색하라
-- 부등호 사용

SELECT      cname, city, point
FROM       customer
WHERE      point >= 350  AND  point <= 500 ;


--BETWEEN.....AND 사용

SELECT      cname, city, point
FROM       customer
WHERE      point BETWEEN 350 AND 500 ;

-- 2-6) 거주지가 서울 이거나 안양인 고객번호, 이름, 거주지를 검색하라
-- 부등호 사용

SELECT      cname, city, point
FROM       customer
WHERE      city = '서울'  OR  city = '안양' ;
        AND

*************-- IN 사용

SELECT      cname, city, point
FROM       customer
WHERE      city IN ('서울', '안양') ;


-- 2-7) 거주지가 서울이 아니거나 안양이 아닌 고객번호, 이름, 거주지를 검색하라
-- 부등호 사용

SELECT      cname, city, point
FROM       customer
WHERE      city <> '서울' AND city <> '안양’;
       

-- NOT IN 사용

SELECT      cname, city, point
FROM       customer
WHERE      city not in ('서울','안양') ;


-- 3-1) 정씨 성을 가진 고객의 모든 열을 검색하라

SELECT      *
FROM       customer
WHERE     cname LIKE '박%';

-- 정으로 끝나는 
SELECT      *
FROM       customer
WHERE     cname LIKE '%박';

--정 이라는 글자가 아무데나
SELECT      *
FROM       customer
WHERE     cname LIKE '%박%';

--두번째 글자가 두번째롤 끝나는것

SELECT      *
FROM       customer
WHERE     cname LIKE '_박';


***-- 3-2) 이름에 '동' 자가 들어가는 고객의 모든 열을 검색하라

SELECT      *
FROM       customer
WHERE      cname LIKE '%동%';

-- 3-3) 이름의 세번째 글자가 '우' 자가 들어가는 고객의 모든 열을 검색하라

SELECT      *
FROM       customer
WHERE      cname LIKE '__우';

-- 3-4) 성이 홍씨, 박씨, 정씨인 고객을 검색하라	

SELECT      *
FROM       customer
WHERE     cname LIKE '홍%' or cname LIKE '박%' or cname LIKE '정%';

-- 성이 홍씨, 박씨, 정씨가 아닌 고객을 검색하라

SELECT      *
FROM       customer
WHERE      cname LIKE '홍%' AND cname NOT LIKE '박%' AND cname NOT LIKE '정%';     

-- 3-5) 포인트가 없는 고객의 번호, 이름, 포인트를 검색하라

SELECT      *
FROM       customer
WHERE      point IS NULL;
     
-- 포인트가 있는 고객의 번호, 이름, 포인트를 검색하라

SELECT      *
FROM       customer
WHERE      point IS NOT NULL;
     
-- 4-1) 고객 테이블에서 이름을 오름차순 정렬하라

정렬: order by

1.오름차순(ascending):

가나다 / 123/ abc

2.내림차순(descending): DESC

SELECT      *
FROM       customer
ORDER BY cname ASC;
	
***-- 4-2) 거주지가 서울인 고객의 모든 데이터를 검색하는데, 이름의 오름차순 정렬하여 출력하라

SELECT      *
FROM       customer
ORDER BY cname ASC ;

-- 4-3) 거주지의 오름차순으로 정렬하고, 거주지가 같으면 포인트의 내림차순으로 정렬하라

SELECT      *
FROM       customer
ORDER BY city ASC, point DESC;

-- 4-4) 포인트가 많은 순으로(내림차순) 먼저 정렬하고, 같은 포인트는 이름의 오름차순으로 정렬하고
-- 이름이 같으면 거주지의 오름차순으로 정렬하여 검색하라 

SELECT      *
FROM       customer
ORDER BY point DESC, came ASC, city ASC;    

-- 4-5) 다음의 의미는?
SELECT      cno,  cname,  city,  point  
FROM        customer  
ORDER  BY  3;
--------------------------------------------------

/* --------------------------------------------- */
/* --- customer 스키마 --------------------- */
CREATE  TABLE   customer (
      cno     char(4)          NOT  NULL  ,
      cname  varchar(10)   NOT  NULL  ,
      city     varchar(20)  ,
      point    int  ,
      PRIMARY  KEY(cno)
);
insert into customer values('c101','홍길동','서울',500);
insert into customer values('c102','임꺽정','인천',300);
insert into customer values('c103','박찬호','안양',800);
insert into customer values('c204','신동엽','과천',350);
insert into customer values('c205','정진우','고양',400);

/* 새 레코드를 추가하고 SELECT문 예제 실습하시오 */
insert into customer values('c307','정동우','서울', NULL);
/* --------------------------------------------- */

-----------------------------------------
# [요약] 집계함수 (sungjuk_group.sql)

-- 집계함수 : 여러 개 행의 값들을 계산하여 하나의 결과를 산출하는 함수
(aggregate function)

-- COUNT(*)     : NULL 포함하여 계산
-- COUNT(필드) : NULL 제외하여 계산

-- Group by(그룹화): 테이블로 부터 어떤 열을 기준해서
                   그룹으로 묶어 
                   합계 계산하거나 평균산출하여 검색
-----------------------------------------
# [요약]  /* SELECT 문법 순서 */
SELECT
FROM
WHERE
GROUP  BY
HAVING
ORDER  BY
-----------------------------------------

[실습 2] SELECT (집계함수)
-- 성적(이름, 점수)
-- 성적2(이름, 과목, 점수)


/* --------------------------------------------- */
/* -------- 집계함수, 그룹화 ---------------- */
drop table 성적;
drop table 성적2;

-- 집계함수
CREATE TABLE 성적(
     이름 varchar(9) NOT NULL primary key, 
     점수 int 
);

INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '홍길동', 87 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '임꺽정', 60 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '박찬호', 75 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '선동열', 70 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '홍명보', 90 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '차범근', 75 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '강성범', 68 );
INSERT INTO 성적 ( 이름, 점수 ) VALUES ( '신동엽', null);

-- 그룹화
-- GROUP BY, HAVING

CREATE TABLE 성적2 (
    이름 varchar(9) NOT NULL primary key , 
    과목 varchar(8), 
    점수 int
);

INSERT INTO 성적2 VALUES ('홍길동', '영어',87 );
INSERT INTO 성적2 VALUES ('임꺽정', '수학',60 );
INSERT INTO 성적2 VALUES ('박찬호', '국어',75 );
INSERT INTO 성적2 VALUES ('선동열', '영어',70 );
INSERT INTO 성적2 VALUES ('홍명보', '수학',90 );
INSERT INTO 성적2 VALUES ('차범근', '수학',75 );
INSERT INTO 성적2 VALUES ('강성범', '수학',68 );
INSERT INTO 성적2 VALUES ('신동엽', '영어',null);

SELECT * FROM 성적;
SELECT * FROM 성적2;
/* --------------------------------------------- */

[실습 2-1]  SELECT (집계함수) (성적)

-- 성적(이름, 점수)
-- 1-1) 최고 점수를 검색하라 
-- 1-2) 최저 점수를 검색하라
-- 1-3) 점수합계를 검색하라 
-- 1-4) 평균점수를 검색하라
-- 1-5) 학생수는 모두 몇 명인지 검색하라
-- 1-6) 시험에 응시한 학생수는 모두 몇 명인지 검색하라
-----------------------------------------
[실습 2-02] SELECT (그룹화) (성적2)

-- 성적2(이름, 과목, 점수)
-- 2-1) 각 과목수는 몇 개인지 검색하라(DISTINCT 사용)
-- 2-2) 과목별 수강생은 몇 명인지 검색하라(GROUP BY)
-- 2-3) 과목별 평균점수를 검색하라(GROUP BY)
-- 2-4) 과목별 평균점수 75 보다 높은 학생의 과목별 평균점수를 검색하라(HAVING)

-- ROUND() 함수

select 과목, ROUND(AVG(점수))
from 성적2
group by 과목;

--2-5) 점수가 70 이상인 과목이름, 과목 평균점수를 과목의 과목별 평균점수가 75 이상인 것만
--과목별 평균점수가 높은 순으로 검색하라(ORDER  BY)

============================
[요약] SELECT 문법
# 연산자 우선순위
1. ( )
2. 논리 연산자: NOT > AND > OR
3. 관계 연산자:
         > ,  >= , = ,  != ,  <=  ,  <
                         <>
4. 산술 연산자: *,  /
                   +. -

-- 관계 연산자
초과 이상 
