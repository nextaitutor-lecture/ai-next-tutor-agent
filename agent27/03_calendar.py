# AI옆자리과외 #27 - Agent v0.1
# 선택한 Action을 실제로 실행하면 어떤 결과가 돌아오는지 보여주는 예제입니다.
# 강의에서는 외부 캘린더 연결 없이 이해할 수 있도록 Mock Tool을 사용합니다.


def check_calendar():
    return {
        "title": "부산 고객사 미팅",
        "start_date": "2026-10-08",
        "end_date": "2026-10-09",
        "location": "부산",
    }


selected_action = "check_calendar"

if selected_action == "check_calendar":
    result = check_calendar()

    print("[Action]")
    print(selected_action)

    print("\n[Action Result]")
    print(f"일정: {result['title']}")
    print(f"날짜: {result['start_date']} ~ {result['end_date']}")
    print(f"장소: {result['location']}")
