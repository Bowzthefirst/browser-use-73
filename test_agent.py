from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig, BrowserContextConfig
from dotenv import load_dotenv
import asyncio

# Load environment variables
load_dotenv()

async def main():
    # Configure browser to use your Chrome instance
    browser = Browser(
        config=BrowserConfig(
            chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',  # macOS path
            headless=False,
            disable_security=True,
            extra_chromium_args=[
                '--no-first-run',
                '--no-default-browser-check',
                '--restore-last-session'
            ],
            new_context_config=BrowserContextConfig(
                browser_window_size={'width': 1280, 'height': 720},
                disable_security=True
            )
        )
    )

    agent = Agent(
        task="Go to https://www.canva.com/ directly, search for 'memes', download the first 10 images.",
        llm=ChatOpenAI(model="gpt-4o-mini"),
        browser=browser,
        browser_context=await browser.new_context()  # Create a persistent context
    )
    
    result = await agent.run()
    print("Result:", result)
    
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())