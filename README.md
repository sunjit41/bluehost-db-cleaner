# BlueHost MySQL Automated Table Cleaner

A lightweight, secure Python automation script designed to run as a 24-hour Cron Job on BlueHost hosting servers to clear out temporary database logs or tables automatically.

## 🚀 Features
- **Secure Credentials:** Utilizes `python-dotenv` to decouple sensitive database passwords from code logic.
- **Production-Ready:** Optimized to run seamlessly on native hosting server cron subsystems (`/usr/bin/python3`).
- **Resource Efficient:** Closes connections explicitly to prevent dangling database threads.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sunjit41/bluehost-db-cleaner.git
   cd bluehost-db-cleaner
   ```

2. **Configure your Environment:**
   Duplicate the template file and fill in your BlueHost MySQL details:
   ```bash
   cp .env.example .env
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📅 BlueHost cPanel Deployment

1. Upload `clear_table.py` and your configured `.env` file to your BlueHost root directory (e.g., `/home/username/scripts/`).
2. Log into **BlueHost cPanel** and navigate to **Cron Jobs**.
3. Under **Common Settings**, select **Once per day (0 0 * * *)**.
4. Set the command to invoke your script:
   ```bash
   /usr/bin/python3 /home/your_cpanel_username/scripts/clear_table.py
   ```
