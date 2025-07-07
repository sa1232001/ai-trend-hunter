from dotenv import load_dotenv
load_dotenv()

import os
from src.collectors.youtube_collector import YouTubeCollector
from src.analyzers.ai_content_analyzer import AIContentAnalyzer
from src.generators.report_generator import ReportGenerator

print("🚀 Debug: Testing full pipeline...")

# Test YouTube collector
youtube = YouTubeCollector(os.getenv('YOUTUBE_API_KEY'))
youtube_content = youtube.collect_ai_content(7)
print(f"✅ YouTube found: {len(youtube_content)} videos")

# Test other collectors (placeholder data)
all_content = {
    'youtube': youtube_content,
    'twitter': [],
    'instagram': [],
    'linkedin': []
}

print(f"📊 Total content items: {sum(len(items) for items in all_content.values())}")

# Test analyzer
analyzer = AIContentAnalyzer(None)
analyzed = analyzer.analyze_batch(all_content)

print(f"🧠 After analysis:")
for category, items in analyzed['content'].items():
    print(f"  - {category}: {len(items)} items")

# Test report generator
generator = ReportGenerator()
report_path = generator.create_report(analyzed)
print(f"📋 Report generated: {report_path}")

import os
os.system(f"start {report_path}")