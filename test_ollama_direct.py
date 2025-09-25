#!/usr/bin/env python3
"""
Simple test of Ollama + Llama 3.1 for BigMoeHunter
Tests the modern AI without complex dependencies
"""

import subprocess
import json

def test_ollama_direct():
    """Test Ollama directly with hunting questions"""
    print("🤖 Testing BigMoeHunter Modern AI (Ollama + Llama 3.1)")
    print("=" * 60)
    
    # Test questions for your father's hunting needs
    test_questions = [
        "What's the best time to hunt deer in Colebrook, NH when it's 45°F with light winds?",
        "Give me hunting advice for moose in WMU A near Connecticut Lakes",
        "What equipment should I use for bear hunting in Dixville Notch?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n🎯 Test {i}: {question}")
        print("-" * 50)
        
        try:
            # Use ollama run directly
            result = subprocess.run([
                "ollama", "run", "llama3.1:8b", question
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                response = result.stdout.strip()
                print(f"✅ AI Response:")
                print(response)
                print(f"\n📊 Response Length: {len(response)} characters")
            else:
                print(f"❌ Error: {result.stderr}")
                
        except subprocess.TimeoutExpired:
            print("⏰ Request timed out")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n" + "=" * 60)
    print("🎉 Modern AI Test Complete!")
    print("🤖 You now have cutting-edge Llama 3.1 AI running locally!")
    print("🦌 Perfect for your father's hunting needs in Colebrook, NH!")

if __name__ == "__main__":
    test_ollama_direct()
