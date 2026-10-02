# AI옆자리과외 #27 - Agent v0.2
# v0.1: 상태를 보고 다음 행동을 선택
# v0.2: 행동을 실제로 실행하고 결과를 상태에 반영
#
# 이번 예제에서는 캘린더 확인 후 교통편까지 검색합니다.
# 단, 원하는 시간대의 KTX 좌석이 없는 상황에서 멈춥니다.
# '그럼 Agent는 다음에 무엇을 해야 할까?'라는 다음 문제를 남기기 위한 예제입니다.

state = {
    "goal": "다음 주 부산 출장 준비",
    "current_state": {
        "trip_date": None,
        "location": None,
        "transport": None,
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

    if current["transport"] is None:
        return "search_transport"

    return "search_hotel"


def check_calendar():
    # 실제 프로젝트에서는 Google Calendar 같은 외부 Tool/API가 이 역할을 합니다.
    return {
        "trip_date": "2026-10-08 ~ 2026-10-09",
        "location": "부산",
    }


def search_transport():
    # 실제 프로젝트에서는 철도/교통편 검색 Tool/API가 이 역할을 합니다.
    # 강의에서는 예상과 다른 실행 결과를 보여주기 위해 Mock 결과를 사용합니다.
    return {
        "route": "서울 → 부산",
        "preferred_time": "오전 9시 전후",
        "available": False,
        "message": "원하는 시간대 KTX 좌석 없음",
    }


def execute_action(action):
    if action == "check_calendar":
        return check_calendar()

    if action == "search_transport":
        return search_transport()

    return {}


print("=== Agent v0.2 ===")

print("\n[1] Current State")
print("출장 날짜: 알 수 없음")
print("교통편: 미확보")

# 1차 판단: 날짜가 없으므로 캘린더 확인
first_action = decide_next_action(state)
print("\n[2] Selected Action")
print(first_action)

calendar_result = execute_action(first_action)
print("\n[3] Action Result")
print(f"출장 일정: {calendar_result['trip_date']}")
print(f"장소: {calendar_result['location']}")

# 캘린더 결과를 상태에 반영
state["current_state"].update(calendar_result)

print("\n[4] Updated State")
print(f"출장 날짜: {state['current_state']['trip_date']}")
print(f"장소: {state['current_state']['location']}")
print("교통편: 미확보")

# 2차 판단: 날짜를 알게 되었으므로 교통편 검색
second_action = decide_next_action(state)
print("\n[5] Next Action")
print(second_action)

transport_result = execute_action(second_action)
print("\n[6] Action Result")
print(f"구간: {transport_result['route']}")
print(f"희망 시간: {transport_result['preferred_time']}")
print(f"검색 결과: {transport_result['message']}")

# 검색은 했지만 좌석을 확보하지 못했으므로 transport는 미확보 상태로 유지
if transport_result["available"]:
    state["current_state"]["transport"] = transport_result

print("\n[Current State]")
print("출장 날짜: 확인")
print("교통편: 미확보")

print("\n[Problem]")
print("원하는 시간대 차표가 없습니다.")
print("Agent는 이제 무엇을 해야 할까요?")
