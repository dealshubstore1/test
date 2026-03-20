import requests
from bs4 import BeautifulSoup
import time
import antigravity

# Configuration
# Note: In a real scenario, you'd use a dedicated Cricket API, 
# but for a simple agent, we scrape a live-score summary page.
URL = "https://www.espncricinfo.com/live-cricket-score" 

def fetch_live_score():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding the specific match container for SA vs NZ
        # This logic looks for the team names in the live feed
        matches = soup.find_all(class_='ci-team-score')
        
        score_text = "Match not found or not live yet."
        
        for match in matches:
            if "South Africa" in match.text or "New Zealand" in match.text:
                score_text = match.get_text(separator=" ")
                break
        
        return score_text
    except Exception as e:
        return f"Error fetching score: {e}"

def main():
    for i in range(3):
        score = fetch_live_score()
        timestamp = time.strftime("%H:%M:%S")
        
        log_entry = f"[{timestamp}] SA vs NZ: {score}\n"
        
        with open("score.txt", "a") as f:
            f.write(log_entry)
            
        print(f"Iteration {i+1} saved: {score}")
        
        if i < 2:
            time.sleep(10)

if __name__ == "__main__":
    main()
