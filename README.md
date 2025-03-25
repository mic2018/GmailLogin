###**1. Install Dependencies**<BR>  
Make sure you have Python installed (3.8 or later).<BR>  
Clone the repository and install dependencies:<BR>  
```bash
pip install -r requirements.txt
playwright install

###**2. Set Environment Variables (Optional)<BR>
Create a .env file in the root folder:<BR>
To follow best practices, you should avoid hardcoding credentials. Instead, supply them using environment variables:<BR>
GMAIL_USERNAME=your-email@gmail.com<BR>  
GMAIL_PASSWORD=your-password<BR>  
BROWSER_TYPE=chromium<BR>
**If you won't perform the step, the project will use a default automation test user credentials
**<BR>

###**3. Run Tests<BR>
You can run the tests using Pytest and specify the browser:<BR>
python -m pytest  --browser=chromium tests




