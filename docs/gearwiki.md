# 🛡️ GearWiki: 데이터베이스 설계 명세서 (Database Design Specification)

## 1. 개요 (Overview)
본 문서는 게임 아이템 정보 제공 및 유저별 기어 스코어(Gear Score) 계산을 위한 **GearWiki** 서비스의 데이터베이스 구조를 정의합니다. 대규모 조회 성능과 데이터 무결성 보장을 핵심 목표로 설계되었습니다.

---

## 2. 핵심 테이블 설계 (Core Tables)
![](2026-01-22-10-47-57.png)




### 👤 users (사용자)
유저의 기본 정보와 실시간 합산 점수를 관리하는 역정규화 테이블입니다.
| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| `user_id` | BIGINT UNSIGNED (PK) | 고유 식별자. 대규모 확장을 위해 8바이트 사용. |
| `user_name` | VARCHAR(50) (Unique) | 유저 닉네임. |
| `user_pw` | VARCHAR(255) | 해시 암호화된 비밀번호. |
| **`total_gear_score`** | INT UNSIGNED | **[역정규화]** 장착 아이템 효과의 최종 합산치. 조회 성능 향상 목적. |

### 📦 items (아이템 도감)
게임 내 모든 아이템의 정적인 마스터 데이터를 관리합니다.
| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| `item_id` | INT UNSIGNED (PK) | 아이템 고유 코드. |
| `item_name` | VARCHAR(100) | 아이템 명칭. |
| `category` | ENUM('W', 'A') | 무기(Weapon), 방어구(Armor) 등 타입 제한. |
| `required_level` | TINYINT UNSIGNED | 착용 제한 레벨 (1바이트 최적화). |

### 📊 item_stats (아이템 효과 상세)
아이템별 추가 효과(예: 공격력 15% 증가)를 정의하는 테이블입니다.
| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| `stat_id` | INT UNSIGNED (PK) | 효과 고유 식별자. |
| `item_id` | INT UNSIGNED (FK) | 도감 아이템 번호 연동. |
| `effect_type` | VARCHAR(50) | 효과 구분 (예: ATK_PER, DEF_FLAT, CRIT_CHANCE). |
| **`effect_value`** | DECIMAL(10, 2) | **[정밀도]** 부동 소수점 오차 방지를 위한 고정 소수점 타입. |

### 🎒 user_inventory (보유 아이템)
유저가 실제로 획득한 아이템 인스턴스를 관리합니다.
| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| `inventory_id` | BIGINT UNSIGNED (PK) | 인벤토리 아이템 고유 번호. |
| `user_id` | BIGINT UNSIGNED (FK) | 소유 유저 ID. |
| `item_id` | INT UNSIGNED (FK) | 도감 정보 연결. |
| `enhanced` | TINYINT UNSIGNED | 강화 수치 (0~255). |
| **`is_equipped`** | TINYINT(1) |장착 여부 플래그. 인벤토리 조회 시 성능 최적화. |

### ⚔️ user_equipment (장착 관리)
유저의 슬롯별 현재 장착 정보를 관리합니다.
| 컬럼명 | 타입 | 설명 |
| :--- | :--- | :--- |
| `equipment_id` | BIGINT UNSIGNED (PK) | 장착 정보 식별자. |
| `user_id` | BIGINT UNSIGNED (FK) | 장착 유저 ID. |
| `slot_type` | ENUM('H', 'C', 'W') | 장착 슬롯(Head, Chest, Weapon). |
| **`inventory_id`** | BIGINT UNSIGNED (FK, Unique) | 특정 인벤토리 아이템 연결. 중복 장착 방지. |

---

## 3. 핵심 설계 전략 (Technical Highlights)

### 🚀 성능 최적화 (Performance)
* **B-Tree 인덱스**: `items` 테이블의 `category`에 인덱스를 적용하여 필터링 검색 속도를 $O(\log n)$으로 유지합니다.
* **전략적 역정규화**: `total_gear_score`와 `is_equipped` 컬럼을 통해 가장 빈번한 요청인 '내 정보 보기'와 '인벤토리 보기' 시 JOIN 연산을 최소화했습니다.

### 🛡️ 데이터 무결성 및 동시성 (Integrity & Concurrency)
* **ACID 트랜잭션**: 아이템 장착 시 `is_equipped` 상태 변경과 `total_gear_score` 갱신을 하나의 원자적 단위로 묶어 데이터 오차를 방지합니다.
* **복합 유니크 제약**: `user_equipment` 테이블에서 `(user_id, slot_type)`을 유니크하게 설정하여 물리적으로 불가능한 중복 장착 버그를 DB 레벨에서 차단합니다.
* **낙관적 락(Optimistic Lock)**: `version` 컬럼(필요 시 추가)을 활용하여 다중 접속 환경에서의 데이터 덮어쓰기 문제를 해결합니다.

### ⚙️ 유연한 비즈니스 로직 (Scalability)
* **효과 타입 분리**: 스탯 수치를 컬럼이 아닌 행(Row)으로 관리(`effect_type`)하여, 새로운 장비 옵션이 추가되어도 테이블 스키마 변경 없이 유연하게 대응합니다.
* **정밀한 타입 선택**: `UNSIGNED` 속성을 통해 음수 데이터를 원천 차단하고, `TINYINT`와 `DECIMAL`을 적재적소에 배치하여 저장 공간과 계산 정확도를 모두 잡았습니다.

---

## 4. 테이블 관계도 (ER-Relationships)
1.  **Users ↔ Inventory (1:N)**: 유저별 보유 아이템 목록 관리.
2.  **Items ↔ Stats (1:N)**: 아이템별 다중 효과(공격+방어 등) 관리.
3.  **Inventory ↔ Equipment (1:1)**: 특정 아이템 인스턴스의 슬롯 장착 여부 관리.
4.  **Users ↔ Equipment (1:N)**: 유저별 현재 장착 세트 정보 관리.