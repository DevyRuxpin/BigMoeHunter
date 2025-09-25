"""
Ultra-lightweight AI service - No external dependencies required
Uses pure Python rule-based system for hunting recommendations
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

class LightweightHuntingAI:
    """Ultra-lightweight AI service - no external dependencies"""
    
    def __init__(self):
        self.hunting_knowledge = self._initialize_hunting_knowledge()
    
    async def get_hunting_recommendation(
        self,
        location: str,
        species: str,
        weather_data: Dict,
        user_preferences: Optional[Dict] = None
    ) -> Dict:
        """Generate hunting recommendation using rule-based system"""
        
        context = self._build_context(location, species, weather_data, user_preferences)
        recommendation_text = self._generate_recommendation(context)
        
        recommendation = self._parse_recommendation(recommendation_text, context)
        return recommendation
    
    def _initialize_hunting_knowledge(self) -> Dict:
        """Initialize comprehensive hunting knowledge base"""
        return {
            "species": {
                "White-tailed Deer": {
                    "rut_timing": "Late October to early December",
                    "feeding_patterns": "Dawn and dusk, especially 30 minutes before sunrise and after sunset",
                    "habitat_preferences": "Mixed forests, agricultural edges, apple orchards",
                    "weather_impact": "Cool temperatures increase activity, high winds reduce movement",
                    "colebrook_tips": "Focus on Connecticut Lakes region, use apple orchards, look for fresh scrapes",
                    "equipment": "Rifle, shotgun, or bow. Use scent control products.",
                    "strategies": "Still hunting, stand hunting, calling during rut",
                    "optimal_times": "Early morning (5:30-8:00 AM) and late afternoon (4:00-6:30 PM)"
                },
                "Moose": {
                    "rut_timing": "Late September to early October",
                    "feeding_patterns": "Early morning and evening, active near water",
                    "habitat_preferences": "Wetlands, boreal forests, young forest stands",
                    "weather_impact": "Cool, overcast days are best. Avoid hot, sunny days.",
                    "colebrook_tips": "WMU A and B have highest success rates, focus on water sources",
                    "equipment": "Rifle (.30 caliber minimum), binoculars, GPS",
                    "strategies": "Spot and stalk, calling during rut, glassing open areas",
                    "optimal_times": "Early morning (6:00-9:00 AM) and evening (4:00-7:00 PM)"
                },
                "Black Bear": {
                    "rut_timing": "June to July",
                    "feeding_patterns": "Active throughout day, especially near food sources",
                    "habitat_preferences": "Dense forests, berry patches, agricultural areas",
                    "weather_impact": "Moderate temperatures ideal, avoid extreme heat",
                    "colebrook_tips": "Focus on Dixville Notch area, look for berry patches",
                    "equipment": "Rifle (.30 caliber), bear spray, bait where legal",
                    "strategies": "Baiting, spot and stalk, calling",
                    "optimal_times": "Early morning (6:00-10:00 AM) and late afternoon (3:00-7:00 PM)"
                },
                "Wild Turkey": {
                    "rut_timing": "Spring (April-May)",
                    "feeding_patterns": "Early morning feeding, roosting in trees",
                    "habitat_preferences": "Mixed forests, fields, agricultural areas",
                    "weather_impact": "Calm, clear mornings are best. Avoid windy conditions.",
                    "colebrook_tips": "Use calls near roosting areas, decoys can be effective",
                    "equipment": "Shotgun (12 or 20 gauge), turkey calls, decoys",
                    "strategies": "Calling, decoying, roost hunting",
                    "optimal_times": "Early morning (5:00-8:00 AM) and late afternoon (4:00-6:00 PM)"
                }
            },
            "weather_patterns": {
                "temperature": {
                    "cold": "Increases animal activity, especially deer and moose",
                    "hot": "Reduces daytime activity, animals seek shade and water",
                    "moderate": "Optimal conditions for most species"
                },
                "wind": {
                    "calm": "Perfect for still hunting and calling",
                    "light": "Good for scent control and movement",
                    "strong": "Difficult conditions, reduces animal movement"
                },
                "pressure": {
                    "rising": "Often increases animal activity",
                    "falling": "May reduce activity, storm approaching",
                    "stable": "Normal activity patterns"
                }
            },
            "colebrook_locations": {
                "Connecticut Lakes": "Prime moose and deer hunting, remote area",
                "Dixville Notch": "Excellent deer and bear hunting, challenging terrain",
                "Colebrook State Forest": "Local public hunting, easier access",
                "Pittsburg": "Remote hunting opportunities, high success rates"
            }
        }
    
    def _generate_recommendation(self, context: Dict) -> str:
        """Generate comprehensive hunting recommendation"""
        species = context.get("species", "White-tailed Deer")
        location = context.get("location", "Colebrook, NH")
        weather = context.get("weather", {})
        
        knowledge = self.hunting_knowledge["species"].get(species, {})
        
        # Build recommendation
        recommendation_parts = []
        
        # Introduction
        recommendation_parts.append(f"🎯 **Hunting Recommendation for {species} in {location}**")
        recommendation_parts.append("")
        
        # Weather analysis
        temp = weather.get("temperature", 50)
        wind_speed = weather.get("wind_speed", 5)
        pressure = weather.get("barometric_pressure", 30.0)
        
        recommendation_parts.append("🌤️ **Weather Analysis:**")
        if temp < 40:
            recommendation_parts.append(f"• Cool temperature ({temp}°F) is excellent for animal activity")
        elif temp > 70:
            recommendation_parts.append(f"• Warm temperature ({temp}°F) may reduce daytime activity")
        else:
            recommendation_parts.append(f"• Moderate temperature ({temp}°F) provides good hunting conditions")
        
        if wind_speed < 5:
            recommendation_parts.append("• Calm winds are perfect for still hunting and calling")
        elif wind_speed < 15:
            recommendation_parts.append("• Light winds are good for scent control")
        else:
            recommendation_parts.append("• Strong winds may reduce animal movement")
        
        if pressure > 30.2:
            recommendation_parts.append("• Rising barometric pressure indicates increased activity")
        elif pressure < 29.8:
            recommendation_parts.append("• Falling pressure may reduce activity")
        
        # Optimal times
        recommendation_parts.append("")
        recommendation_parts.append("⏰ **Optimal Hunting Times:**")
        if knowledge.get("optimal_times"):
            recommendation_parts.append(f"• {knowledge['optimal_times']}")
        else:
            recommendation_parts.append("• Early morning (5:30-8:00 AM) - Peak activity period")
            recommendation_parts.append("• Late afternoon (4:00-6:30 PM) - Secondary activity window")
        
        # Species-specific advice
        if knowledge:
            recommendation_parts.append("")
            recommendation_parts.append("🦌 **Species-Specific Tips:**")
            if "colebrook_tips" in knowledge:
                recommendation_parts.append(f"• {knowledge['colebrook_tips']}")
            if "strategies" in knowledge:
                recommendation_parts.append(f"• Recommended strategies: {knowledge['strategies']}")
            if "equipment" in knowledge:
                recommendation_parts.append(f"• Equipment: {knowledge['equipment']}")
        
        # Colebrook-specific advice
        recommendation_parts.append("")
        recommendation_parts.append("🗺️ **Colebrook Area Tips:**")
        recommendation_parts.append("• Focus on WMU A and B for moose hunting")
        recommendation_parts.append("• Connecticut Lakes region offers excellent deer hunting")
        recommendation_parts.append("• Dixville Notch is prime for bear hunting")
        recommendation_parts.append("• Early morning hunts are most successful in this region")
        
        # Safety reminders
        recommendation_parts.append("")
        recommendation_parts.append("⚠️ **Safety Reminders:**")
        recommendation_parts.append("• Always wear blaze orange during firearms season")
        recommendation_parts.append("• Inform someone of your hunting location")
        recommendation_parts.append("• Check weather conditions before heading out")
        recommendation_parts.append("• Carry emergency communication device")
        
        # Additional tips based on conditions
        recommendation_parts.append("")
        recommendation_parts.append("💡 **Additional Tips:**")
        if temp < 30:
            recommendation_parts.append("• Dress warmly - cold weather increases animal activity")
        if wind_speed > 15:
            recommendation_parts.append("• Consider hunting from a stand due to windy conditions")
        if pressure > 30.2:
            recommendation_parts.append("• Rising pressure suggests excellent hunting conditions")
        
        return "\n".join(recommendation_parts)
    
    def _build_context(self, location: str, species: str, weather_data: Dict, user_preferences: Optional[Dict]) -> Dict:
        """Build context dictionary for analysis"""
        return {
            "location": location,
            "species": species,
            "weather": weather_data,
            "timestamp": datetime.now().isoformat(),
            "season": self._get_current_season(),
            "moon_phase": self._get_moon_phase(),
            "user_preferences": user_preferences or {}
        }
    
    def _parse_recommendation(self, recommendation_text: str, context: Dict) -> Dict:
        """Parse recommendation into structured format"""
        return {
            "recommendation": recommendation_text,
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
            "expires_at": (datetime.now() + timedelta(hours=6)).isoformat(),
            "ai_model": "Lightweight Rule-Based System"
        }
    
    def _calculate_confidence(self, context: Dict) -> float:
        """Calculate confidence score"""
        confidence = 0.75  # Base confidence for rule-based system
        
        # Increase confidence based on data completeness
        if context.get("weather"):
            confidence += 0.1
        if context.get("species"):
            confidence += 0.1
        if context.get("location"):
            confidence += 0.05
        
        return min(confidence, 0.9)  # Cap at 90%
    
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
        phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous", 
                 "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
        return random.choice(phases)
    
    async def get_species_specific_advice(self, species: str, location: str) -> Dict:
        """Get species-specific hunting advice"""
        knowledge = self.hunting_knowledge["species"].get(species, {})
        
        if not knowledge:
            return {
                "general_info": "Species-specific information not available",
                "colebrook_tips": "Contact local Fish & Game office for current information"
            }
        
        return knowledge
    
    async def analyze_weather_impact(self, weather_data: Dict, species: str) -> Dict:
        """Analyze weather impact on hunting"""
        temp = weather_data.get("temperature", 50)
        wind_speed = weather_data.get("wind_speed", 5)
        pressure = weather_data.get("barometric_pressure", 30.0)
        
        analysis = {
            "wind_impact": "Moderate winds (5-15 mph) are ideal for most hunting",
            "temperature_impact": "Cooler temperatures increase animal activity",
            "pressure_impact": "Rising barometric pressure often increases activity",
            "precipitation_impact": "Light rain can be good for tracking",
            "recommendations": []
        }
        
        # Add specific recommendations
        if wind_speed > 20:
            analysis["recommendations"].append("High winds may reduce animal movement")
        elif wind_speed < 3:
            analysis["recommendations"].append("Calm conditions are perfect for still hunting")
        
        if temp > 70:
            analysis["recommendations"].append("Hot weather may reduce daytime activity")
        elif temp < 30:
            analysis["recommendations"].append("Cold weather increases animal activity")
        
        if pressure > 30.2:
            analysis["recommendations"].append("Rising pressure indicates good hunting conditions")
        elif pressure < 29.8:
            analysis["recommendations"].append("Falling pressure may reduce activity")
        
        return analysis
