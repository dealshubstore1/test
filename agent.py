import time
import datetime
import pytz
import requests
import antigravity # The "magic" requirement

# Configuration
OPENROUTER_API_KEY = "your_api_key_here"
MODEL = "google/gemini-2.0-flash-lite-preview-02-05:free"

def ask_agent_to_log(current_time):
    # This sends the time to the AI to get a 'reaction' or confirmation
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer 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"},
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": f"The current time in Pakistan is {current_time}. Acknowledge this for the log."}]
        }
    )
    return response.json()['choices'][0]['message']['content']

def main():
    pakistan_tz = pytz.timezone('Asia/Karachi')
    
    for i in range(3):
        # 1. Fetch Time
        now = datetime.datetime.now(pakistan_tz)
        time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # 2. Get AI Commentary (Optional Agentic Step)
        print(f"Iteration {i+1}: Fetching time...")
        
        # 3. Save to File
        with open("log.txt", "a") as f:
            f.write(f"Timestamp: {time_str}\n")
        
        print(f"Saved: {time_str}")
        
        if i < 2: # Don't sleep after the last run
            time.sleep(10)

    print("Task complete. 3 logs saved.")

if __name__ == "__main__":
    main()
