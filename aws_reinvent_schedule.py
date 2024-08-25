import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging

class AWSReinventSchedule:
    def __init__(self, year=2024):
        self.year = year
        self.base_url = f"https://reinvent.awsevents.com/{year}/"
        self.schedule = []
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)

    def fetch_schedule(self):
        self.logger.info(f"Fetching AWS re:Invent {self.year} schedule...")
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            self.parse_schedule(response.text)
        except requests.RequestException as e:
            self.logger.error(f"Error fetching schedule: {e}")

    def parse_schedule(self, raw_data):
        self.logger.info("Parsing schedule data...")
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
            self.logger.info(f"Parsed session: {title}")

    def save_schedule(self, filename=None):
        if not filename:
            filename = f"aws_reinvent_{self.year}_schedule.json"
        with open(filename, 'w') as f:
            json.dump(self.schedule, f, indent=2)
        self.logger.info(f"Schedule saved to {filename}")
        self.logger.info(f"Total sessions downloaded: {len(self.schedule)}")

def main():
    downloader = AWSReinventSchedule(2024)
    downloader.fetch_schedule()
    downloader.save_schedule()

if __name__ == "__main__":
    main()
