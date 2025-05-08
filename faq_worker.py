# faq_worker.py

from faq_chatbot import run_faq_bot
import time

# Optional: simulate background task queue
example_inputs = [
    ("What is your refund policy?", "session_1"),
    ("How can I contact support?", "session_2"),
    ("Is my data secure?", "session_1")
]

if __name__ == "__main__":
    print("✅ Background worker started!")

    for question, session in example_inputs:
        answer = run_faq_bot(question, session)
        print(f"\n🧠 Q: {question}\n💬 A: {answer}\n")
        time.sleep(2)  # simulate delay

    print("✅ All test questions processed.")
