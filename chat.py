import os
import random
from dotenv import load_dotenv
from groq import Groq

# ============================================================
#                 CUISINE EVERYWHERE 🌍🍽️
#              Your AI World Cuisine Companion
# ============================================================

# Load environment variables
load_dotenv()

# Configuration
API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "llama-3.3-70b-versatile")
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

if not API_KEY:
    raise ValueError("GROQ_API_KEY is missing in the .env file.")

# Groq client
client = Groq(api_key=API_KEY)


# ============================================================
#                    AI PERSONALITY
# ============================================================

SYSTEM_PROMPT = """
You are Cuisine Everywhere 🌍🍽️, a creative, friendly and intelligent
AI chatbot dedicated to food and cuisines from around the world.

Your goals:
- Help users discover cuisines from different countries.
- Recommend dishes based on their preferences.
- Provide recipes and cooking instructions.
- Suggest meals using available ingredients.
- Explain ingredients and cooking techniques.
- Share interesting facts about food and cultures.
- Help users explore traditional and modern dishes.
- Answer food-related questions clearly and creatively.
- Be conversational, warm and enthusiastic.

When giving recipes, include:
1. Ingredients
2. Preparation
3. Cooking steps
4. Serving suggestions

Always make the conversation feel like a fun culinary journey.

If the user asks something unrelated to food, you can still help,
but keep your personality friendly and conversational.

Do not make up information.
If you are unsure about something, clearly say so.
"""

# Conversation history
conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


# ============================================================
#                       GREETINGS
# ============================================================

greetings = [
    "Welcome to Cuisine Everywhere — where every dish has a story! 🌍🍽️",
    "Hello, food explorer! Ready to take your taste buds on a journey? 👋🌎",
    "Namaste, foodie! 🍕🌮🍜 What delicious adventure shall we explore today?",
    "Welcome to Cuisine Everywhere! ✨ From street food to fine dining, let's explore it all!",
    "Your virtual culinary journey starts here. 🌎🥘 Where shall we eat today?",
    "Welcome, Chef! 👨‍🍳🔥 Let's cook, discover and explore flavors from around the world!",
    "Hey foodie! 🍜🌶️ Got a craving? Let's turn it into something delicious!",
    "No passport needed! ✈️🍴 Today we're travelling through food.",
    "Hello! 🥗🍛🍰 Tell me what you're craving and I'll help you discover something amazing.",
    "Welcome to Cuisine Everywhere — connecting cultures, one plate at a time. 🌍❤️"
]


# ============================================================
#                    GREETING RESPONSES
# ============================================================

greeting_responses = {
    "hi": [
        "Hello, foodie! 👋 What are we cooking or discovering today? 🍳",
        "Hi there! 🌍🍽️ Ready for a delicious adventure?",
        "Hey! 👨‍🍳 Tell me what you're craving and let's begin!"
    ],

    "hello": [
        "Hello! 👋 Welcome to your world of flavors! 🌍🍽️",
        "Hello, food explorer! 🌎 What would you like to discover today?",
        "Hey there! 👨‍🍳 I'm ready to help with your next delicious idea!"
    ],

    "hey": [
        "Hey foodie! 👋 What's on today's menu? 🍴",
        "Hey there! 🌮🍜 What delicious adventure shall we start?",
        "Hello, Chef! 👨‍🍳 What are we creating today?"
    ],

    "hii": [
        "Hii! 👋✨ Welcome to Cuisine Everywhere!",
        "Hii foodie! 🍕 What are you craving today?"
    ],

    "hiii": [
        "Hiii! 👋🍽️ Let's make something delicious!",
        "Hiii, food explorer! 🌍 What's cooking?"
    ],

    "good morning": [
        "Good morning, foodie! ☀️🍳 Ready for a delicious start to the day?",
        "Good morning! 🌅👨‍🍳 How about a tasty breakfast idea?"
    ],

    "good afternoon": [
        "Good afternoon, foodie! ☀️🍽️ What are we having for lunch?",
        "Good afternoon! 👋 Ready to explore some amazing flavors?"
    ],

    "good evening": [
        "Good evening, foodie! 🌆🍴 Shall we plan something delicious for dinner?",
        "Good evening! 👨‍🍳✨ What should be on tonight's menu?"
    ]
}


# ============================================================
#                       FAREWELLS
# ============================================================

farewells = [
    "Until our next culinary adventure! Keep exploring flavors! 🌍🍽️",
    "Bon appétit and happy cooking! 👋🍳✨",
    "Until next time, foodie! May your next meal be unforgettable! 🌎🍴",
    "Keep cooking, keep discovering, and keep enjoying! 🥘✨",
    "Goodbye, Chef! 👨‍🍳❤️ See you on our next food journey!",
    "Kitchen's closing for now — take care and keep those taste buds happy! 🍴😊"
]


# ============================================================
#                    HELPER FUNCTIONS
# ============================================================

def normalize_message(message):
    """Clean user input for command/greeting detection."""
    return message.lower().strip()


def handle_greeting(message):
    """Return a friendly response if the user sends a greeting."""
    message = normalize_message(message)

    if message in greeting_responses:
        return random.choice(greeting_responses[message])

    return None


def show_help():
    """Display chatbot commands and examples."""
    print("\n" + "=" * 65)
    print("                 🍽️ CUISINE EVERYWHERE")
    print("                       HELP MENU")
    print("=" * 65)

    print("\n👨‍🍳 I can help you with:")
    print("   🌍 Explore cuisines from around the world")
    print("   🍳 Get recipes and cooking instructions")
    print("   🥘 Find meals using available ingredients")
    print("   🌶️ Understand ingredients and flavors")
    print("   🍰 Discover desserts and sweet dishes")
    print("   ☕ Learn food facts and culinary culture")

    print("\n💡 Try asking:")
    print("   • Suggest an Italian dinner for 2")
    print("   • I have rice, eggs and vegetables. What can I cook?")
    print("   • Give me a simple chocolate cake recipe")
    print("   • Tell me about famous foods in Japan")
    print("   • What can I substitute for butter?")

    print("\n⚙️ Commands:")
    print("   /help  → Show this help menu")
    print("   /exit  → Exit Cuisine Everywhere")
    print("=" * 65)


# ============================================================
#                         AI CHAT
# ============================================================

def chat(user_message):

    conversation.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation,
        temperature=TEMPERATURE
    )

    assistant_message = response.choices[0].message.content

    conversation.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


# ============================================================
#                          MAIN
# ============================================================

def main():

    # Welcome screen
    print("\n")
    print("=" * 65)
    print("              🌍 CUISINE EVERYWHERE 🍽️")
    print("             YOUR AI WORLD CUISINE COMPANION")
    print("=" * 65)

    print("\n👋 " + random.choice(greetings))

    print("\n✨ I can help you explore:")

    print("   🌎  World Cuisines")
    print("   🍳  Recipes & Cooking")
    print("   🥘  Dish Recommendations")
    print("   🌶️  Ingredients & Flavors")
    print("   🍰  Desserts")
    print("   ☕  Food Culture & Stories")

    print("\n💬 Ask me anything about food!")

    print("\n💡 Example:")
    print("   \"I have rice, eggs and vegetables. What can I cook?\"")

    print("\n📌 Type /help for commands.")
    print("📌 Type /exit to leave.")

    print("\n" + "-" * 65)

    # Chat loop
    while True:

        try:
            user_message = input("\n👤 You: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\n\n🍽️ Cuisine Everywhere:")
            print(random.choice(farewells))
            break

        if not user_message:
            continue

        message = normalize_message(user_message)

        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        if message in ["exit", "quit", "/exit", "/quit"]:

            print("\n🍽️ Cuisine Everywhere:")
            print(random.choice(farewells))
            print()

            break

        # ----------------------------------------------------
        # HELP
        # ----------------------------------------------------

        if message in ["/help", "help"]:

            show_help()
            continue

        # ----------------------------------------------------
        # GREETING
        # ----------------------------------------------------

        greeting_response = handle_greeting(message)

        if greeting_response:

            print("\n👨‍🍳 Chef Nova:")
            print(greeting_response)
            continue

        # ----------------------------------------------------
        # AI RESPONSE
        # ----------------------------------------------------

        try:

            print("\n👨‍🍳 Chef Nova is thinking...")

            answer = chat(user_message)

            print("\n🌍 Chef Nova:")
            print(answer)

        except Exception as e:

            print("\n⚠️ Something went wrong.")
            print("Please check your internet connection or Groq API configuration.")
            print(f"Technical details: {e}")


# ============================================================
#                      START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()
    
