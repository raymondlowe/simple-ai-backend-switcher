import os
import unittest
from simpleaiswitcher import SimpleAI
from simpleaiswitcher import AIBackEndType as BackEnd

class TestSimpleAI(unittest.TestCase):

    def test_simple_ai_with_openai(self):
        """Test creating a SimpleAI instance and getting a reply from the AI"""

        # Get the access token from an environment variable
        access_token = os.environ.get('OpenAIKey')
        self.assertIsNotNone(access_token, "OpenAIKey is not defined in the environment variables.")

        # Initialize the SimpleAI class with a backend and access token
        ai = SimpleAI(BackEnd.OpenAI, access_token)

        # Make sure the backend and access token were set correctly
        self.assertEqual(ai.backEnd, BackEnd.OpenAI)
        self.assertEqual(ai.AccessToken, access_token)

        # Test getting a response from the AI
        response = ai.reply("hello")
        self.assertIsInstance(response, str)
        print(response)


    def test_simple_ai_with_poe(self):
        """Test creating a SimpleAI instance and getting a reply from the AI"""

        # Get the access token from an environment variable
        access_token = os.environ.get('poekey')
        self.assertIsNotNone(access_token, "poekey is not defined in the environment variables.")

        # Initialize the SimpleAI class with a backend and access token
        ai = SimpleAI(BackEnd.Poe, access_token)

        # Make sure the backend and access token were set correctly
        self.assertEqual(ai.backEnd, BackEnd.Poe)
        self.assertEqual(ai.AccessToken, access_token)

        # Test getting a response from the AI
        response = ai.reply("hello")
        self.assertIsInstance(response, str)
        print(response)


if __name__ == '__main__':
    unittest.main()
