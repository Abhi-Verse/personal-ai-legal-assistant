    # main.py

from dotenv import load_dotenv
from crew import legal_assistant_crew

# Load environment variables
load_dotenv()

# 🔁 DEMO MODE TOGGLE
# False = real AI execution
# True  = demo / offline output
DEMO_MODE = False


def run(user_input: str):

    # 1️⃣ DEMO MODE (No API call)
    if DEMO_MODE:
        print("\n--- AI LEGAL ASSISTANT OUTPUT (DEMO MODE) ---")
        print("Relevant IPC Section: Section 378 - Theft")
        print("Punishment: Imprisonment up to 3 years or fine or both.")
        print("Explanation: Theft involves dishonest removal of movable property.")
        return

    # 2️⃣ REAL AI EXECUTION
    try:
        result = legal_assistant_crew.kickoff(
            inputs={"user_input": user_input}
        )

        print("-" * 50)
        print(result)
        print("-" * 50)

    # 3️⃣ FALLBACK MODE (If API fails)
    except Exception as e:
        print("\n--- AI LEGAL ASSISTANT OUTPUT (FALLBACK MODE) ---")
        print("Relevant IPC Section: Section 378 - Theft")
        print("Punishment: Imprisonment up to 3 years or fine or both.")
        print("Explanation: Theft involves dishonest removal of movable property.")
        print("\n[Note: External AI API unavailable during execution]")


if __name__ == "__main__":
    user_input = (
        "A man broke into my house at night while my family was sleeping. "
        "He stole jewelry and cash from our bedroom. When I confronted him, "
        "he threatened me with a knife and ran away. We reported it to the police, "
        "but I'm not sure which legal charges should be filed under IPC."
    )

    run(user_input)

