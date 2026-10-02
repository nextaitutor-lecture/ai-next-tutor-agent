# AI옆자리과외 #27 - Agent v0.2
# v0.1: 상태를 보고 다음 행동을 선택
# v0.2: 선택한 행동을 실행하고, 결과로 상태를 갱신한 뒤 다시 판단

state = {
    "goal": "다음 주 부산 출장 준비",
    "current_state": {
        "trip_date": None,
        "location": None,
    },
    "available_actions": [
        "check_calendar",
        "search_transport",
        "search_hotel",
    ],
}


def decide_next_action(state):
    current = state["current_state"]

    if current["trip_date"] is None:
        return "check_calendar"

    return "search_transport"


def check_calendar():
    # 실제 프로젝트에서는 Google Calendar 같은 외부 Tool/API가 이 역할을 합니다.
    return {
        "trip_date": "2026-10-08 ~ 2026-10-09",
        "location": "부산",
    }


def execute_action(action):
    if action == "check_calendar":
        return check_calendar()

    # #27에서는 Tool 종류를 확장하기보다
    # '판단 → 실행 → 결과 → 상태 갱신 → 다시 판단' 흐름에 집중합니다.
    return {}


print("=== Agent v0.2 ===")

# 1. 현재 상태를 보고 다음 행동 선택
action = decide_next_action(state)
print(f"1) Selected Action: {action}")

# 2. 선택한 행동 실행
result = execute_action(action)
print(f"2) Action Result: {result}")

# 3. 실행 결과를 현재 상태에 반영
state["current_state"].update(result)
print(f"3) Updated State: {state['current_state']}")

# 4. 바뀐 상태를 보고 다시 다음 행동 판단
next_action = decide_next_action(state)
print(f"4) Next Action: {next_action}")
