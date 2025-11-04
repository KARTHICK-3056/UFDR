#!/usr/bin/env python3
"""
Quick final verification test
"""

import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

def main():
    """Quick verification test"""
    
    print("🔧 Testing critical imports...")
    try:
        from utils.anomaly_detection import detect_temporal_anomalies, analyze_contact_patterns
        from utils.highlighter import highlight_entities, clean_text, highlight_query_terms
        from backend.ingest import load_ufdr_data, create_documents
        print("✅ All imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    print("📁 Testing sample data...")
    try:
        sample_path = os.path.join(PROJECT_ROOT, "data", "sample_ufdr.json")
        data = load_ufdr_data(sample_path)
        print(f"✅ Loaded UFDR data: {len(data.get('messages', []))} messages")
    except Exception as e:
        print(f"❌ Sample data error: {e}")
        return False
    
    print("🧠 Testing behavioral intelligence...")
    try:
        messages = data['messages']
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({
                'message_id': msg.get('message_id', 'unknown'),
                'timestamp': msg.get('timestamp', ''),
                'sender': msg.get('sender', 'Unknown'),
                'recipient': msg.get('recipient', 'Unknown'),
                'content': clean_text(msg.get('content', ''))
            })
        
        temporal_results = detect_temporal_anomalies(formatted_messages)
        contact_results = analyze_contact_patterns(formatted_messages, new_contact_window_hours=72)
        
        print(f"✅ Found {len(temporal_results.get('odd_hour_messages', []))} odd-hour messages")
        print(f"✅ Found {len(contact_results.get('new_contacts', []))} new contacts")
    except Exception as e:
        print(f"❌ Behavioral intelligence error: {e}")
        return False
    
    print("🧹 Testing text cleaning...")
    try:
        test_text = '<span style="color: red;">Test message with HTML</span>'
        cleaned = clean_text(test_text)
        if '<' not in cleaned:
            print("✅ Text cleaning working")
        else:
            print(f"❌ HTML still present: {cleaned}")
            return False
    except Exception as e:
        print(f"❌ Text cleaning error: {e}")
        return False
    
    print("\n🎉 All critical functions working correctly!")
    print("🚀 Application should now run without errors!")
    return True

if __name__ == "__main__":
    main()