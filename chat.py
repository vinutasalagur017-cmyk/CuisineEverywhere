import os
import random
from dotenv import load_dotenv
from groq import Groq

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

# Chatbot personality
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

# Creative greetings
greetings = [
    "🌍🍽️ Welcome to Cuisine Everywhere — where every dish has a story!",
    "👋 Hello, food explorer! Ready to take your taste buds on a journey?",
    "🍕🌮🍜 Namaste, foodie! What delicious adventure shall we explore today?",
    "✨ Welcome to Cuisine Everywhere! From street food to fine dining, let's explore it all!",
    "🌎🥘 Your virtual culinary journey starts here. Where shall we eat today?",
    "👨‍🍳🔥 Welcome, Chef! Let's cook, discover and explore flavors from around the world!",
    "🍜🌶️ Hey foodie! Got a craving? Let's turn it into something delicious!",
    "✈️🍴 No passport needed — today we're travelling through food!",
    "🥗🍛🍰 Hello! Tell me what you're craving and I'll help you discover something amazing.",
    "🌍❤️ Welcome to Cuisine Everywhere — connecting cultures, one plate at a time!"
]

# Farewell messages
farewells = [
    "🍽️ Until our next culinary adventure! Keep exploring flavors! 🌍",
    "👋 Bon appétit and happy cooking! 🍳✨",
    "🌎🍴 Until next time, foodie! May your next meal be unforgettable!",
    "🥘✨ Keep cooking, keep discovering, and keep enjoying!",
    "👨‍🍳❤️ Goodbye! See you on our next food journey!"
]


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


def main():

    print("\n" + "=" * 65)
    print("              🌍 CUISINE EVERYWHERE 🍽️")
    print("=" * 65)

    print("\n" + random.choice(greetings))

    print("\n✨ Your culinary companion for:")
    print("   🌎 World Cuisines")
    print("   🍳 Recipes & Cooking")
    print("   🥘 Dish Recommendations")
    print("   🌶️ Ingredients & Flavors")
    print("   🍰 Desserts")
    print("   ☕ Food Culture & Stories")

    print("\n💬 Ask me anything about food!")
    print("💡 Try: 'Suggest an Italian dinner for 2'")
    print("💡 Try: 'I have rice, eggs and vegetables. What can I cook?'")
    print("💡 Try: 'Tell me about famous foods in Japan'")
    print("💡 Type 'exit' or 'quit' to leave.\n")

    print("-" * 65)

    while True:

        user_message = input("\n👤 You: ").strip()

        if not user_message:
            continue

        if user_message.lower() in ["exit", "quit"]:

            print("\n🍽️ Cuisine Everywhere:")
            print(random.choice(farewells))
            print()

            break

        try:

            print("\n👨‍🍳 Cuisine Everywhere is thinking...")

            answer = chat(user_message)

            print(f"\n🌍 Cuisine Everywhere: {answer}")

        except Exception as e:

            print(f"\n⚠️ Something went wrong: {e}")


if __name__ == "__main__":
    main()
