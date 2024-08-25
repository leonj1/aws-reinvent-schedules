import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class AWSReinventSchedule:
    def __init__(self, year=2024):
        self.year = year
        self.base_url = f"https://reinvent.awsevents.com/{year}/"
        self.schedule = []

    def fetch_schedule(self):
        print(f"Fetching AWS re:Invent {self.year} schedule...")
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            self.parse_schedule(response.text)
        except requests.RequestException as e:
            print(f"Error fetching schedule: {e}")

    def parse_schedule(self, raw_data):
        print("Parsing schedule data...")
        soup = BeautifulSoup(raw_data, 'html.parser')
        
        # This is a hypothetical structure. Adjust based on actual HTML structure
        sessions = soup.find_all('div', class_='session')
        
        for session in sessions:
            title = session.find('h2', class_='session-title').text.strip()
            time = session.find('span', class_='session-time').text.strip()
            speaker = session.find('span', class_='session-speaker').text.strip()
            description = session.find('p', class_='session-description').text.strip()
            
            self.schedule.append({
                'title': title,
                'time': time,
                'speaker': speaker,
                'description': description
            })

    def save_schedule(self, filename=None):
        if not filename:
            filename = f"aws_reinvent_{self.year}_schedule.json"
        with open(filename, 'w') as f:
            json.dump(self.schedule, f, indent=2)
        print(f"Schedule saved to {filename}")

def main():
    downloader = AWSReinventSchedule(2024)
    downloader.fetch_schedule()
    downloader.save_schedule()

if __name__ == "__main__":
    main()
