# ai-next-tutor-agent

AI옆자리과외 Agent 강의용 실습 저장소입니다.

## #27 Agent란? — 질문하는 AI에서 일하는 AI로

이번 예제의 목표는 복잡한 Agent 프레임워크를 먼저 사용하는 것이 아니라, Agent의 가장 작은 동작을 코드로 직접 확인하는 것입니다.

사용자 요청:

> 다음 주 부산 출장 준비해줘.

단순한 LLM 답변에서 끝내지 않고 다음 흐름을 단계적으로 구현합니다.

```text
Goal
  ↓
Current State
  ↓
Available Actions
  ↓
Decide
  ↓
Action 실행
  ↓
Result
  ↓
State 갱신
  ↓
다시 Decide
```

### 실행 순서

```bash
python agent27/01_state.py
python agent27/02_decide.py
python agent27/03_calendar.py
python agent27/04_agent_v02.py
```

### 01_state.py

Agent가 판단하기 전에 무엇을 알고 있는지 확인합니다.

```text
[Goal]
다음 주 부산 출장 준비

[Current State]
정확한 출장 날짜: 알 수 없음

[Available Actions]
- check_calendar
- search_transport
- search_hotel
```

### 02_decide.py — v0.1

현재 상태에서 다음 행동 하나를 선택합니다.

```text
Selected Action:
check_calendar

Reason:
교통편과 숙소를 확인하려면
먼저 정확한 출장 날짜가 필요함
```

여기까지의 핵심은 Agent가 모든 일을 한 번에 처리하는 것이 아니라, **현재 상태를 보고 다음 행동을 선택한다**는 점입니다.

### 03_calendar.py — Action 실행

`check_calendar`를 선택하는 것에서 끝내지 않고 실제 Tool이 실행되면 어떤 결과가 돌아오는지 확인합니다.

강의 예제에서는 별도 계정이나 API Key 없이 실행할 수 있도록 Mock Calendar Tool을 사용합니다.

```text
Action: check_calendar
       ↓
Calendar Tool 실행
       ↓
출장 날짜 / 장소 반환
```

### 04_agent_v02.py — v0.2

v0.2에서는 Agent가 Action 결과를 다시 상태에 넣습니다.

```text
출장 날짜 모름
   ↓
check_calendar 선택
   ↓
Calendar 실행
   ↓
2026-10-08 ~ 2026-10-09 / 부산
   ↓
State 갱신
   ↓
다시 판단
   ↓
search_transport
```

즉 v0.1의

```text
판단 → Action 선택
```

에서 v0.2의

```text
판단 → 실행 → 결과 확인 → 상태 갱신 → 다시 판단
```

으로 발전합니다.

이 작은 반복 구조가 이후 Agent Loop, Tool 사용, Planner를 이해하기 위한 출발점입니다.
