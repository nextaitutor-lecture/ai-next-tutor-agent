# AI옆자리과외 #27 - Agent v0.1
# 현재 상태를 보고 '다음 행동 하나'를 결정하는 가장 작은 Agent 예제입니다.

state = {
    "goal": "다음 주 부산 출장 준비",
    "current_state": {
        "trip_date": None
    },
    "available_actions": [
        "check_calendar",
        "search_transport",
        "search_hotel",
    ],
}


def decide_next_action(state):
    if state["current_state"]["trip_date"] is None:
        return {
            "action": "check_calendar",
            "reason": "교통편과 숙소를 확인하려면 먼저 정확한 출장 날짜가 필요함",
        }

    return {
        "action": "search_transport",
        "reason": "출장 날짜를 확인했으므로 다음으로 교통편을 확인할 수 있음",
    }


decision = decide_next_action(state)

print("Selected Action:")
print(decision["action"])

print("\nReason:")
print(decision["reason"])
