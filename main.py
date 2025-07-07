 
import requests
from datetime import datetime, timedelta
import os

class YouTubeCollector:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.googleapis.com/youtube/v3"
        self.ai_keywords = [
            "artificial intelligence", "machine learning", "ChatGPT", "GPT-4",
            "AI tools", "OpenAI", "Claude", "Midjourney", "Stable Diffusion",
            "AI tutorial", "prompt engineering", "AI automation", "LLM",
            "generative AI", "AI coding", "AI art", "voice AI"
        ]
        
    def collect_ai_content(self, days_back=7):
        """Collect AI content from YouTube"""
        if not self.api_key:
            print("⚠️  YouTube API key not found")
            return self._get_sample_content()
            
        content = []
        published_after = (datetime.now() - timedelta(days=days_back)).isoformat() + 'Z'
        
        for keyword in self.ai_keywords[:5]:  # Limit to 5 keywords for speed
            try:
                search_params = {
                    'part': 'snippet',
                    'q': keyword,
                    'type': 'video',
                    'publishedAfter': published_after,
                    'order': 'relevance',
                    'maxResults': 10,
                    'key': self.api_key
                }
                
                response = requests.get(f"{self.base_url}/search", params=search_params)
                data = response.json()
                
                if 'items' in data:
                    for item in data['items']:
                        video_id = item['id']['videoId']
                        video_stats = self._get_video_stats(video_id)
                        
                        content_item = {
                            'platform': 'youtube',
                            'id': video_id,
                            'title': item['snippet']['title'],
                            'description': item['snippet']['description'][:300],
                            'url': f"https://www.youtube.com/watch?v={video_id}",
                            'thumbnail': item['snippet']['thumbnails'].get('medium', {}).get('url', ''),
                            'creator': item['snippet']['channelTitle'],
                            'published_at': item['snippet']['publishedAt'],
                            'keyword': keyword,
                            'stats': video_stats
                        }
                        content.append(content_item)
                        
            except Exception as e:
                print(f"Error collecting YouTube content for '{keyword}': {e}")
                continue
                
        return sorted(content, key=lambda x: x['stats']['engagement_rate'], reverse=True)[:20]
    
    def _get_video_stats(self, video_id):
        """Get video statistics"""
        try:
            params = {
                'part': 'statistics,contentDetails',
                'id': video_id,
                'key': self.api_key
            }
            
            response = requests.get(f"{self.base_url}/videos", params=params)
            data = response.json()
            
            if 'items' in data and len(data['items']) > 0:
                stats = data['items'][0]['statistics']
                
                views = int(stats.get('viewCount', 0))
                likes = int(stats.get('likeCount', 0))
                comments = int(stats.get('commentCount', 0))
                
                engagement_rate = ((likes + comments) / max(views, 1)) * 100
                
                return {
                    'views': views,
                    'likes': likes,
                    'comments': comments,
                    'engagement_rate': engagement_rate
                }
        except:
            pass
            
        return {'views': 0, 'likes': 0, 'comments': 0, 'engagement_rate': 0}
    
    def _get_sample_content(self):
        """Sample content when API key is missing"""
        return [
            {
                'platform': 'youtube',
                'id': 'sample1',
                'title': 'ChatGPT vs Claude: Ultimate AI Comparison',
                'description': 'Comprehensive comparison of the latest AI models...',
                'url': 'https://youtube.com/watch?v=sample1',
                'thumbnail': '',
                'creator': 'AI Expert Channel',
                'published_at': datetime.now().isoformat(),
                'keyword': 'ChatGPT',
                'stats': {'views': 45000, 'likes': 2300, 'comments': 450, 'engagement_rate': 6.1}
            }
        ]