"""
AI-powered hunting recommendations service
Integrates OpenAI GPT-4 for intelligent hunting advice
"""

import openai
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import os
from dotenv import load_dotenv

load_dotenv()

class HuntingAI:
    """AI service for hunting recommendations"""
    
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4"
    
    async def get_hunting_recommendation(
        self,
        location: str,
        species: str,
        weather_data: Dict,
        user_preferences: Optional[Dict] = None
    ) -> Dict:
        """
        Generate AI-powered hunting recommendation
        
        Args:
            location: Hunting location (e.g., "Colebrook, NH")
            species: Target species (e.g., "White-tailed Deer")
            weather_data: Current weather conditions
            user_preferences: User's hunting preferences and experience level
        
        Returns:
            Dict containing AI recommendation and confidence score
        """
        
        # Build context for AI
        context = self._build_context(location, species, weather_data, user_preferences)
        
        # Create AI prompt
        prompt = self._create_prompt(context)
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": self._get_system_prompt()
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            recommendation_text = response.choices[0].message.content
            
            # Parse and structure the response
            recommendation = self._parse_recommendation(recommendation_text, context)
            
            return recommendation
            
        except Exception as e:
            return {
                "error": f"AI service error: {str(e)}",
                "recommendation": "Unable to generate recommendation at this time.",
                "confidence_score": 0.0
            }
    
    def _build_context(self, location: str, species: str, weather_data: Dict, user_preferences: Optional[Dict]) -> Dict:
        """Build context dictionary for AI analysis"""
        context = {
            "location": location,
            "species": species,
            "weather": weather_data,
            "timestamp": datetime.now().isoformat(),
            "season": self._get_current_season(),
            "moon_phase": self._get_moon_phase(),
            "user_preferences": user_preferences or {}
        }
        return context
    
    def _create_prompt(self, context: Dict) -> str:
        """Create detailed prompt for AI analysis"""
        prompt = f"""
        As an expert New Hampshire hunting guide specializing in the Colebrook region, provide a comprehensive hunting recommendation based on the following information:
        
        Location: {context['location']}
        Target Species: {context['species']}
        Current Weather: {json.dumps(context['weather'], indent=2)}
        Current Season: {context['season']}
        Moon Phase: {context['moon_phase']}
        
        Please provide:
        1. Optimal hunting times for today/tomorrow
        2. Best hunting strategies for current conditions
        3. Equipment recommendations
        4. Safety considerations
        5. Expected animal behavior patterns
        6. Location-specific tips for the Colebrook area
        
        Format your response as a structured hunting plan with specific, actionable advice.
        """
        return prompt
    
    def _get_system_prompt(self) -> str:
        """Get system prompt for AI behavior"""
        return """
        You are an expert hunting guide with extensive knowledge of New Hampshire wildlife, 
        particularly in the Colebrook region. You have deep understanding of:
        
        - New Hampshire Fish & Game regulations
        - Wildlife Management Unit boundaries
        - Species behavior patterns and seasonal movements
        - Weather impact on hunting success
        - Local terrain and hunting strategies
        - Safety protocols and best practices
        
        Provide accurate, practical, and safe hunting advice based on real-world conditions.
        Always prioritize safety and legal compliance in your recommendations.
        """
    
    def _parse_recommendation(self, ai_response: str, context: Dict) -> Dict:
        """Parse AI response into structured format"""
        return {
            "recommendation": ai_response,
            "confidence_score": self._calculate_confidence(context),
            "factors_considered": [
                "Weather conditions",
                "Species behavior patterns",
                "Seasonal timing",
                "Location characteristics",
                "Moon phase",
                "Historical success rates"
            ],
            "generated_at": datetime.now().isoformat(),
            "expires_at": (datetime.now() + timedelta(hours=6)).isoformat()
        }
    
    def _calculate_confidence(self, context: Dict) -> float:
        """Calculate confidence score based on available data"""
        confidence = 0.5  # Base confidence
        
        # Increase confidence based on data completeness
        if context.get("weather"):
            confidence += 0.2
        if context.get("species"):
            confidence += 0.1
        if context.get("location"):
            confidence += 0.1
        if context.get("user_preferences"):
            confidence += 0.1
        
        return min(confidence, 1.0)
    
    def _get_current_season(self) -> str:
        """Determine current hunting season"""
        month = datetime.now().month
        if month in [9, 10, 11, 12]:
            return "Fall"
        elif month in [1, 2, 3]:
            return "Winter"
        elif month in [4, 5]:
            return "Spring"
        else:
            return "Summer"
    
    def _get_moon_phase(self) -> str:
        """Get current moon phase (simplified)"""
        # This is a simplified calculation
        # In production, use a proper astronomical library
        return "Waxing Gibbous"  # Placeholder
    
    async def get_species_specific_advice(self, species: str, location: str) -> Dict:
        """Get species-specific hunting advice"""
        species_info = {
            "White-tailed Deer": {
                "rut_timing": "Late October to early December",
                "feeding_patterns": "Dawn and dusk",
                "habitat_preferences": "Mixed forests, agricultural edges",
                "colebrook_tips": "Focus on Connecticut Lakes region, use apple orchards"
            },
            "Moose": {
                "rut_timing": "Late September to early October",
                "feeding_patterns": "Early morning and evening",
                "habitat_preferences": "Wetlands, boreal forests",
                "colebrook_tips": "WMU A and B have highest success rates"
            },
            "Black Bear": {
                "rut_timing": "June to July",
                "feeding_patterns": "Active throughout day",
                "habitat_preferences": "Dense forests, berry patches",
                "colebrook_tips": "Focus on Dixville Notch area"
            },
            "Wild Turkey": {
                "rut_timing": "Spring (April-May)",
                "feeding_patterns": "Early morning",
                "habitat_preferences": "Mixed forests, fields",
                "colebrook_tips": "Use calls near roosting areas"
            }
        }
        
        return species_info.get(species, {
            "general_info": "Species-specific information not available",
            "colebrook_tips": "Contact local Fish & Game office for current information"
        })
    
    async def analyze_weather_impact(self, weather_data: Dict, species: str) -> Dict:
        """Analyze how weather conditions affect hunting success"""
        analysis = {
            "wind_impact": "Moderate winds (5-15 mph) are ideal for most hunting",
            "temperature_impact": "Cooler temperatures increase animal activity",
            "pressure_impact": "Rising barometric pressure often increases activity",
            "precipitation_impact": "Light rain can be good for tracking",
            "recommendations": []
        }
        
        # Add specific recommendations based on weather
        if weather_data.get("wind_speed", 0) > 20:
            analysis["recommendations"].append("High winds may reduce animal movement")
        
        if weather_data.get("temperature", 0) > 70:
            analysis["recommendations"].append("Hot weather may reduce daytime activity")
        
        return analysis
