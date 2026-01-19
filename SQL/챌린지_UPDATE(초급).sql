-- **`PM` 직책을 가진 모든 직원의 연봉을 10% 인상한 후 그 결과를 확인하세요.**
SET SQL_SAFE_UPDATES = 0;
UPDATE employee
SET salary = salary * 1.1
WHERE position = 'PM';

SELECT * FROM employee WHERE position = 'PM';

-- **모든 `Backend`' 직책을 가진 직원의 연봉을 5% 인상하세요.**
UPDATE employee
SET salary = salary * 1.05
WHERE position = 'backend';

**모든 직원을 `position` 별로 그룹화하여 각 직책의 평균 연봉을 계산하세요.**
SELECT position, COUNT(*) as employee_count, AVG(salary) as average_salary, ROUND(AVG(salary), 2) as avg_salary_rounded
FROM employee
GROUP BY position
ORDER BY average_salary DESC;