# AI옆자리과외 #27 - Agent v0.1
# 목표와 현재 상태, 가능한 행동을 정의합니다.

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

print("[Goal]")
print(state["goal"])

print("\n[Current State]")
print("정확한 출장 날짜: 알 수 없음")

print("\n[Available Actions]")
for action in state["available_actions"]:
    print(f"- {action}")
