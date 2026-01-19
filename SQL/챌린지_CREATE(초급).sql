-- 1. employee 테이블을 생성해 주세요.
-- - `속성명 **id의** 자료형은 INT입니다. 추가로 자동으로 1씩 증가하도록 설정하고 기본키로 지정합니다.`
-- - `속성명 **name의** 자료형은 VARCHAR(100)입니다.`
-- - `속성명 **position의** 자료형은 VARCHAR(100)입니다.`
-- - `속성명 **salary의** 자료형은 DECIMAL(10, 2)입니다.`

CREATE TABLE employee(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

-- 2. **직원 데이터를 `employees`에 추가해주세요**
--     - 이름: 혜린, 직책: PM, 연봉: 90000
--     - 이름: 은우, 직책: Frontend, 연봉: 80000
--     - 이름: 가을, 직책: Backend, 연봉: 92000
--     - 이름: 지수, 직책: Frontend, 연봉: 7800
--     - 이름: 민혁, 직책: Frontend, 연봉: 96000
--     - 이름: 하온, 직책: Backend, 연봉: 130000

INSERT INTO employee (name, position, salary) VALUES 
('혜린', 'PM', 90000),
('은우', 'frontend', 80000),
('가을', 'backend', 92000),
('지수', 'frontend', 7800),
('민혁', 'frontend', 96000),
('하은', 'backend', 130000);
