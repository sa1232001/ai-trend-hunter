class TwitterCollector:
    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        
    def collect_ai_content(self, days_back=7):
        # Simple placeholder - returns sample data for now
        return [
            {
                'platform': 'twitter',
                'id': 'sample_tweet_1',
                'title': 'Just discovered this amazing AI tool for content creation!',
                'content': 'Just discovered this amazing AI tool that automates content creation! Game-changer for creators. #AI #ContentCreation #Productivity',
                'url': 'https://twitter.com/sample/status/123',
                'creator': 'AI Enthusiast',
                'published_at': '2025-07-08T12:00:00Z',
                'stats': {'likes': 250, 'retweets': 45, 'replies': 20, 'quotes': 8}
            },
            {
                'platform': 'twitter',
                'id': 'sample_tweet_2', 
                'title': 'OpenAI just announced something incredible...',
                'content': 'OpenAI just announced something incredible. The future of AI is happening faster than we thought! 🚀 #OpenAI #AI #Innovation',
                'url': 'https://twitter.com/sample/status/124',
                'creator': 'Tech Reporter',
                'published_at': '2025-07-08T10:30:00Z',
                'stats': {'likes': 1200, 'retweets': 340, 'replies': 156, 'quotes': 89}
            }
        ]
