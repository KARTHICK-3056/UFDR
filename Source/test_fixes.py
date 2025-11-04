#!/usr/bin/env python3
"""
Test script to validate all the fixes made to the FORENSIS-AI codebase.
This script tests the main components without running the full Streamlit app.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all critical imports work"""
    print("Testing imports...")
    try:
        from utils.highlighter import clean_text, highlight_entities
        from utils.anomaly_detection import detect_temporal_anomalies, analyze_contact_patterns
        from backend.ingest import create_documents
        from backend.search_engine import hybrid_search
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_html_css_cleaning():
    """Test that HTML/CSS tag cleaning works properly"""
    print("Testing HTML/CSS cleaning...")
    try:
        from utils.highlighter import clean_text
        
        # Test with malformed HTML/CSS
        dirty_text = 'Finding #1 — 2025-09-22T19:00:33Z\n\nSending ETH to 0span style="background-color: #FFD700; padding: 1px 4px; border-radius: 3px; font-weight: 500;" title="Crypto">0x742d35Cc6634C0532925a3b844Bc454e4438f44epadding: 1px 4px; border-radius: 3px; font-weight: 500;" title="Amount">742d35Cc6634C0532925a3b844Bc454e4438f44e now.'
        
        cleaned = clean_text(dirty_text)
        
        # Check that HTML/CSS artifacts are removed
        if 'style=' not in cleaned and 'background-color:' not in cleaned and 'padding:' not in cleaned:
            print("✅ HTML/CSS cleaning works correctly")
            print(f"   Original length: {len(dirty_text)}")
            print(f"   Cleaned length:  {len(cleaned)}")
            print(f"   Sample cleaned:  {cleaned[:100]}...")
            return True
        else:
            print(f"❌ HTML/CSS artifacts still present: {cleaned}")
            return False
    except Exception as e:
        print(f"❌ HTML/CSS cleaning test failed: {e}")
        return False

def test_message_id_handling():
    """Test that message_id handling works properly in behavioral analysis"""
    print("Testing message_id handling...")
    try:
        from utils.anomaly_detection import detect_temporal_anomalies
        from datetime import datetime
        
        # Test with messages without message_id
        test_messages = [
            {
                'timestamp': '2025-01-01T02:00:00Z',
                'sender': 'Alice',
                'recipient': 'Bob',
                'content': 'Test message 1'
            },
            {
                'timestamp': '2025-01-01T03:00:00Z', 
                'sender': 'Bob',
                'recipient': 'Alice',
                'content': 'Test message 2'
            }
        ]
        
        # This should not raise a KeyError now
        result = detect_temporal_anomalies(test_messages)
        
        if 'anomalies' in result:
            print("✅ Message ID handling works correctly")
            print(f"   Detected {len(result['anomalies'])} anomalies")
            return True
        else:
            print("❌ Unexpected result format from detect_temporal_anomalies")
            return False
            
    except Exception as e:
        print(f"❌ Message ID handling test failed: {e}")
        return False

def test_document_creation():
    """Test document creation from UFDR data"""
    print("Testing document creation...")
    try:
        from backend.ingest import create_documents
        
        test_data = {
            "messages": [
                {
                    "timestamp": "2025-01-01T12:00:00Z",
                    "sender": "TestUser",
                    "text": "This is a test message",
                    "media_path": ""
                }
            ]
        }
        
        docs = create_documents(test_data)
        
        if docs and len(docs) > 0:
            print("✅ Document creation works correctly")
            print(f"   Created {len(docs)} documents")
            print(f"   First doc content: {docs[0].page_content[:50]}...")
            return True
        else:
            print("❌ No documents created")
            return False
            
    except Exception as e:
        print(f"❌ Document creation test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 FORENSIS-AI Fix Validation Tests")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_html_css_cleaning,
        test_message_id_handling,
        test_document_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with exception: {e}")
            print()
    
    print("=" * 40)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All fixes are working correctly!")
        print("\nYou can now run the application with:")
        print("streamlit run frontend/app.py")
    else:
        print("⚠️  Some issues remain. Check the failed tests above.")
    
    return passed == total

if __name__ == "__main__":
    main()