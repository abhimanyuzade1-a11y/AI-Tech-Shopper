from ai_brain import understand_request

from agent_planner import create_plan


# =========================================================
# CUSTOMER REQUEST
# =========================================================

message = (
    "I need a laptop for AI and gaming "
    "under 80000"
)


# =========================================================
# UNDERSTAND REQUEST
# =========================================================

customer = understand_request(
    message
)


# =========================================================
# CREATE AGENT PLAN
# =========================================================

plan = create_plan(
    customer
)


# =========================================================
# DISPLAY PLAN
# =========================================================

print()

print(
    "======================================"
)

print(
    "          🤖 AGENT PLAN"
)

print(
    "======================================"
)


for number, action in enumerate(
    plan,
    start=1
):

    print(
        f"{number}. {action}"
    )