A simple Proof of Concept (PoC) chatbot built using Google Gemini API that can answer system-related questions such as CPU usage, memory status, battery level, and network information.


## Features
- Get real-time CPU usage,speed, and core count
- Check memory usage and available RAM
- View battery percentage, charging status, and estimated backup
- Monitor network speed (download & upload)


## Installation

1. Clone the repository
   
- git clone https://github.com/chandra-kumar-raja/system-chatbot.git
- cd system-chatbot

2. Create and activate a virtual environment
- python3 -m venv venv
- source venv/bin/activate 

3. Install dependencies
- pip install -r requirements.txt

4. Set up Gemini API Key
- Add your Gemini API Key in .env file
- GEMINI_API_KEY=your_api_key_here

5. Run the Chatbot
- python3 main.py



