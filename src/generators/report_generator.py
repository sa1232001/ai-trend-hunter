from datetime import datetime
import os

class ReportGenerator:
    def __init__(self):
        self.output_dir = "reports"
        os.makedirs(self.output_dir, exist_ok=True)
        
    def create_report(self, analyzed_content):
        """Generate HTML report"""
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = f"ai-trends-{report_date}.html"
        report_path = os.path.join(self.output_dir, report_filename)
        
        html_content = self._generate_html(analyzed_content)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Also create index.html
        index_path = os.path.join(self.output_dir, "index.html")
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return report_path
    
    def _generate_html(self, data):
        """Generate HTML report content"""
        report_date = datetime.now().strftime("%B %d, %Y")
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Trend Hunter Report - {report_date}</title>
    <style>
        body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; max-width: 1200px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; }}
        .container {{ background: rgba(255, 255, 255, 0.95); border-radius: 25px; padding: 40px; box-shadow: 0 25px 50px rgba(0,0,0,0.15); }}
        .header {{ text-align: center; background: linear-gradient(45deg, #667eea, #764ba2); color: white; padding: 30px; border-radius: 15px; margin-bottom: 30px; }}
        .header h1 {{ margin: 0; font-size: 2.5em; }}
        .section {{ background: white; padding: 25px; margin-bottom: 25px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .content-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
        .content-card {{ border: 1px solid #ddd; padding: 20px; border-radius: 8px; background: #f9f9f9; }}
        .platform-badge {{ background: #3498db; color: white; padding: 5px 10px; border-radius: 15px; font-size: 0.8em; }}
        .engagement-stats {{ color: #666; font-size: 0.9em; margin: 10px 0; }}
        h2 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        .insight {{ background: #e8f5e8; padding: 15px; border-left: 4px solid #27ae60; margin: 10px 0; }}
        a {{ color: #3498db; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🚀 AI Trend Hunter</h1>
            <p>Your AI trend discovery agent - {report_date}</p>
            <p><strong>{data['total_items']} trending items discovered!</strong></p>
        </div>
        
        <div class="section">
            <h2>🔥 Top Trending Content</h2>
            <div class="content-grid">
"""
        
        # Add top items from each category
        all_items = []
        for category, items in data['content'].items():
            all_items.extend(items[:2])
        
        for item in all_items[:8]:
            html += f"""
            <div class="content-card">
                <div style="margin-bottom: 10px;">
                    <span class="platform-badge">{item['platform'].upper()}</span>
                </div>
                <h3>{item.get('title', 'Untitled')}</h3>
                <p>{(item.get('description', item.get('content', ''))[:150])}...</p>
                <div class="engagement-stats">
                    {self._format_engagement_stats(item)}
                </div>
                <a href="{item.get('url', '#')}" target="_blank">View Content →</a>
            </div>
            """
        
        html += """
        </div>
    </div>
    
    <div class="section">
        <h2>🛠️ New AI Tools</h2>
        <div class="content-grid">
"""
        
        for item in data['content'].get('tools', [])[:4]:
            html += self._generate_content_card(item)
        
        html += """
        </div>
    </div>
    
    <div class="section">
        <h2>💡 Creative Use Cases</h2>
        <div class="content-grid">
"""
        
        for item in data['content'].get('use_cases', [])[:4]:
            html += self._generate_content_card(item)
        
        html += """
        </div>
    </div>
    
    <div class="section">
        <h2>📚 Best Tutorials</h2>
        <div class="content-grid">
"""
        
        for item in data['content'].get('tutorials', [])[:4]:
            html += self._generate_content_card(item)
        
        html += """
        </div>
    </div>
    
    <div class="section">
        <h2>🤖 AI Agent's Insights</h2>
"""
        
        for insight in data.get('insights', []):
            html += f'<div class="insig
