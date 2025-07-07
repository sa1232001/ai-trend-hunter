import os
print('Current directory:', os.getcwd())
print('Files in current directory:', os.listdir('.'))

# Check environment variables
print('\nEnvironment variables:')
for key in ['YOUTUBE_API_KEY', 'TWITTER_BEARER_TOKEN', 'OPENAI_API_KEY']:
    value = os.getenv(key)
    if value:
        print(f'{key}: Set (starts with {value[:10]}...)')
    else:
        print(f'{key}: Not set')

# Test imports
print('\nTesting imports:')
try:
    from src.collectors.youtube_collector import YouTubeCollector
    print('✅ YouTube collector import OK')
except Exception as e:
    print('❌ YouTube collector error:', e)

try:
    from src.analyzers.ai_content_analyzer import AIContentAnalyzer  
    print('✅ Analyzer import OK')
except Exception as e:
    print('❌ Analyzer error:', e)

try:
    from src.generators.report_generator import ReportGenerator
    print('✅ Report generator import OK')
except Exception as e:
    print('❌ Report generator error:', e)