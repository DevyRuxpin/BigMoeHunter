#!/usr/bin/env python3
"""
Test script for BigMoeHunter Free AI Service
Tests the lightweight AI without any external dependencies
"""

import asyncio
import sys
import os

# Add the app directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.services.lightweight_ai_service import LightweightHuntingAI

async def test_free_ai():
    """Test the free AI service"""
    print("🎯 Testing BigMoeHunter Free AI Service")
    print("=" * 50)
    
    # Initialize AI service
    ai = LightweightHuntingAI()
    print("✅ AI Service initialized successfully")
    
    # Test data
    location = "Colebrook, NH"
    species = "White-tailed Deer"
    weather_data = {
        "temperature": 45,
        "wind_speed": 8,
        "wind_direction": 315,
        "barometric_pressure": 30.15,
        "humidity": 65,
        "precipitation": 0
    }
    
    print(f"\n📍 Location: {location}")
    print(f"🦌 Species: {species}")
    print(f"🌤️ Weather: {weather_data['temperature']}°F, {weather_data['wind_speed']} mph winds")
    
    # Get AI recommendation
    print("\n🤖 Getting AI recommendation...")
    try:
        recommendation = await ai.get_hunting_recommendation(
            location=location,
            species=species,
            weather_data=weather_data,
            user_preferences={"experience_level": "intermediate"}
        )
        
        print("✅ AI recommendation generated successfully!")
        print(f"📊 Confidence Score: {recommendation['confidence_score']:.2f}")
        print(f"🤖 AI Model: {recommendation['ai_model']}")
        print(f"⏰ Generated: {recommendation['generated_at']}")
        
        print("\n📝 Recommendation:")
        print("-" * 50)
        print(recommendation['recommendation'])
        print("-" * 50)
        
        # Test species-specific advice
        print("\n🦌 Testing species-specific advice...")
        species_advice = await ai.get_species_specific_advice("Moose", "Colebrook, NH")
        print("✅ Species advice generated!")
        print(f"Colebrook Tips: {species_advice.get('colebrook_tips', 'N/A')}")
        
        # Test weather impact analysis
        print("\n🌤️ Testing weather impact analysis...")
        weather_analysis = await ai.analyze_weather_impact(weather_data, "White-tailed Deer")
        print("✅ Weather analysis generated!")
        print(f"Temperature Impact: {weather_analysis['temperature_impact']}")
        print(f"Recommendations: {len(weather_analysis['recommendations'])} items")
        
        print("\n🎉 All tests passed! Free AI service is working perfectly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing AI service: {e}")
        return False

async def main():
    """Main test function"""
    success = await test_free_ai()
    
    if success:
        print("\n✅ BigMoeHunter Free AI Service is ready to use!")
        print("🚀 No API keys required - completely free!")
        print("🎯 Perfect for your father's hunting needs in Colebrook, NH")
    else:
        print("\n❌ Tests failed. Please check the implementation.")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
