import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import logging
import time
from urllib.parse import urljoin

class AWSReinventSchedule:
    def __init__(self, year=2024):
        self.year = year
        self.base_url = "https://registration.awsevents.com/flow/awsevents/reinvent24/public/page/catalog"
        self.schedule = []
        self.session = requests.Session()
        
        # Set up logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)

    def get_url(self, page=1):
        return f"{self.base_url}?search.topic=1707430256139001EhRR&trk=www.google.com&page={page}"

    def fetch_schedule(self):
        self.logger.info(f"Fetching AWS re:Invent {self.year} schedule...")
        page = 1
        while True:
            url = self.get_url(page)
            try:
                response = self.session.get(url)
                response.raise_for_status()
                new_sessions = self.parse_schedule(response.text)
                if not new_sessions:
                    break
                self.schedule.extend(new_sessions)
                page += 1
                time.sleep(1)  # Be nice to the server
            except requests.RequestException as e:
                self.logger.error(f"Error fetching schedule page {page}: {e}")
                if page > 1:
                    break
                else:
                    raise

    def parse_schedule(self, raw_data):
        self.logger.info("Parsing schedule data...")
        soup = BeautifulSoup(raw_data, 'html.parser')
        sessions = []
        
        for session in soup.find_all('div', class_='session-item'):
            title = session.find('h3', class_='session-title').text.strip()
            session_id = session.get('id', '').replace('session-', '')
            
            details = session.find('div', class_='session-details')
            time = details.find('p', class_='session-time').text.strip()
            location = details.find('p', class_='session-location').text.strip()
            
            description = session.find('div', class_='session-description').text.strip()
            
            speakers = [speaker.text.strip() for speaker in session.find_all('p', class_='speaker-name')]
            
            session_data = {
                'title': title,
                'session_id': session_id,
                'time': time,
                'location': location,
                'description': description,
                'speakers': speakers
            }
            
            sessions.append(session_data)
            self.logger.info(f"Parsed session: {title}")
        
        return sessions

    def save_schedule(self, filename=None):
        if not filename:
            filename = f"aws_reinvent_{self.year}_schedule.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.schedule, f, indent=2, ensure_ascii=False)
        self.logger.info(f"Schedule saved to {filename}")
        self.logger.info(f"Total sessions downloaded: {len(self.schedule)}")

def main():
    downloader = AWSReinventSchedule(2024)
    downloader.fetch_schedule()
    downloader.save_schedule()

if __name__ == "__main__":
    main()
