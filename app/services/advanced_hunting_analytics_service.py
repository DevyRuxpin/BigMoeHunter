#!/usr/bin/env python3
"""
Advanced Hunting Analytics Service for BigMoeHunter
Provides real-world hunting analytics based on scientific algorithms and research
"""

import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from app.services.hunting_data_service import hunting_data_manager

class AdvancedHuntingAnalyticsService:
    """Service for advanced hunting analytics using real algorithms"""
    
    def __init__(self):
        self.data_manager = hunting_data_manager
        
        # Scientific data based on wildlife research
        self.species_behavior_data = {
            "White-tailed Deer": {
                "optimal_temp_range": (25, 55),
                "peak_activity_hours": [(6, 8), (17, 19)],
                "rut_season": (10, 11),
                "feeding_patterns": "Crepuscular",
                "wind_tolerance": 15,
                "pressure_sensitivity": 0.3
            },
            "Moose": {
                "optimal_temp_range": (15, 35),
                "peak_activity_hours": [(5, 9), (16, 20)],
                "rut_season": (9, 10),
                "feeding_patterns": "Diurnal",
                "wind_tolerance": 10,
                "pressure_sensitivity": 0.4
            },
            "Black Bear": {
                "optimal_temp_range": (35, 65),
                "peak_activity_hours": [(6, 10), (16, 20)],
                "rut_season": (6, 7),
                "feeding_patterns": "Diurnal",
                "wind_tolerance": 12,
                "pressure_sensitivity": 0.2
            }
        }
    
    def analyze_hunting_conditions(self, species: str, weather_data: Dict, location: str) -> Dict:
        """Analyze hunting conditions using advanced algorithms"""
        try:
            # Get species behavior data
            species_info = self.species_behavior_data.get(species, self.species_behavior_data["White-tailed Deer"])
            
            # Extract current conditions
            current_time = datetime.now()
            temperature = weather_data.get('temperature', 50)
            wind_speed = weather_data.get('wind_speed', 5)
            condition = weather_data.get('condition', 'Clear')
            pressure = weather_data.get('pressure', 30.0)
            
            # Calculate advanced metrics
            animal_activity_score = self._calculate_animal_activity_score(
                species_info, temperature, wind_speed, condition, pressure, current_time
            )
            
            hunting_effectiveness = self._calculate_hunting_effectiveness(
                species_info, temperature, wind_speed, condition, current_time
            )
            
            weather_advantage = self._calculate_weather_advantage(
                species_info, temperature, wind_speed, condition, pressure
            )
            
            time_advantage = self._calculate_time_advantage(
                species_info, current_time
            )
            
            seasonal_advantage = self._calculate_seasonal_advantage(
                species_info, current_time
            )
            
            location_advantage = self._calculate_location_advantage(
                location, species
            )
            
            # Generate comprehensive analysis
            analysis = {
                "hunting_effectiveness": round(hunting_effectiveness, 1),
                "animal_activity_score": round(animal_activity_score, 1),
                "weather_advantage": round(weather_advantage, 1),
                "time_advantage": round(time_advantage, 1),
                "seasonal_advantage": round(seasonal_advantage, 1),
                "location_advantage": round(location_advantage, 1),
                "overall_rating": self._get_overall_rating(hunting_effectiveness),
                "current_conditions": {
                    "temperature": temperature,
                    "wind_speed": wind_speed,
                    "condition": condition,
                    "pressure": pressure,
                    "time": current_time.strftime("%H:%M"),
                    "date": current_time.strftime("%Y-%m-%d"),
                    "day_of_week": current_time.strftime("%A")
                },
                "scientific_analysis": {
                    "optimal_temp_range": species_info["optimal_temp_range"],
                    "peak_activity_hours": species_info["peak_activity_hours"],
                    "rut_season": species_info["rut_season"],
                    "feeding_patterns": species_info["feeding_patterns"]
                },
                "recommendations": self._generate_advanced_recommendations(
                    species_info, temperature, wind_speed, condition, current_time, hunting_effectiveness
                ),
                "risk_assessment": self._assess_advanced_risks(
                    temperature, wind_speed, condition, current_time
                ),
                "opportunity_analysis": self._analyze_advanced_opportunities(
                    species_info, temperature, wind_speed, condition, current_time
                ),
                "tactical_advice": self._provide_advanced_tactical_advice(
                    species_info, temperature, wind_speed, condition, current_time
                ),
                "equipment_recommendations": self._suggest_advanced_equipment(
                    temperature, condition, wind_speed, species
                )
            }
            
            return analysis
            
        except Exception as e:
            return {"error": f"Advanced analytics calculation failed: {str(e)}"}
    
    def _calculate_animal_activity_score(self, species_info: Dict, temperature: float, wind_speed: float, 
                                       condition: str, pressure: float, current_time: datetime) -> float:
        """Calculate animal activity score based on scientific research"""
        score = 50.0  # Base score
        
        # Temperature effect (based on animal physiology)
        optimal_min, optimal_max = species_info["optimal_temp_range"]
        if optimal_min <= temperature <= optimal_max:
            score += 30  # Optimal temperature
        elif optimal_min - 10 <= temperature <= optimal_max + 10:
            score += 15  # Acceptable temperature
        else:
            score -= 20  # Poor temperature
        
        # Wind effect (animals avoid high winds)
        wind_tolerance = species_info["wind_tolerance"]
        if wind_speed <= wind_tolerance / 2:
            score += 20  # Light winds
        elif wind_speed <= wind_tolerance:
            score += 10  # Moderate winds
        elif wind_speed <= wind_tolerance * 1.5:
            score -= 10  # Strong winds
        else:
            score -= 25  # Very strong winds
        
        # Weather condition effect
        condition_effects = {
            "Clear": 15,
            "Partly Cloudy": 10,
            "Overcast": 5,
            "Light Rain": -10,
            "Heavy Rain": -25,
            "Snow": -15,
            "Fog": -20
        }
        score += condition_effects.get(condition, 0)
        
        # Barometric pressure effect
        pressure_sensitivity = species_info["pressure_sensitivity"]
        if pressure >= 30.2:
            score += pressure_sensitivity * 20  # High pressure
        elif pressure <= 29.8:
            score -= pressure_sensitivity * 20  # Low pressure
        
        # Time of day effect
        current_hour = current_time.hour
        peak_hours = species_info["peak_activity_hours"]
        time_score = 0
        for start_hour, end_hour in peak_hours:
            if start_hour <= current_hour <= end_hour:
                time_score = 25
                break
            elif start_hour - 1 <= current_hour <= end_hour + 1:
                time_score = 15
                break
            else:
                time_score = 5
        
        score += time_score
        
        return max(0, min(100, score))
    
    def _calculate_hunting_effectiveness(self, species_info: Dict, temperature: float, wind_speed: float, 
                                       condition: str, current_time: datetime) -> float:
        """Calculate hunting effectiveness score"""
        effectiveness = 50.0
        
        # Weather conditions for hunting
        if 20 <= temperature <= 60:
            effectiveness += 20  # Comfortable for hunter
        elif 10 <= temperature <= 70:
            effectiveness += 10
        else:
            effectiveness -= 15  # Extreme temperatures
        
        # Wind conditions for hunting
        if wind_speed <= 5:
            effectiveness += 25  # Light winds ideal
        elif wind_speed <= 10:
            effectiveness += 10  # Moderate winds
        elif wind_speed <= 15:
            effectiveness -= 10  # Strong winds
        else:
            effectiveness -= 25  # Very strong winds
        
        # Visibility conditions
        visibility_effects = {
            "Clear": 20,
            "Partly Cloudy": 15,
            "Overcast": 10,
            "Light Rain": -15,
            "Heavy Rain": -30,
            "Snow": -20,
            "Fog": -35
        }
        effectiveness += visibility_effects.get(condition, 0)
        
        # Time effectiveness
        current_hour = current_time.hour
        if 6 <= current_hour <= 8 or 17 <= current_hour <= 19:
            effectiveness += 25  # Prime hunting time
        elif 5 <= current_hour <= 9 or 16 <= current_hour <= 20:
            effectiveness += 15  # Good hunting time
        else:
            effectiveness += 5  # Poor hunting time
        
        return max(0, min(100, effectiveness))
    
    def _calculate_weather_advantage(self, species_info: Dict, temperature: float, wind_speed: float, 
                                   condition: str, pressure: float) -> float:
        """Calculate weather advantage score"""
        advantage = 50.0
        
        # Temperature advantage
        optimal_min, optimal_max = species_info["optimal_temp_range"]
        if optimal_min <= temperature <= optimal_max:
            advantage += 25
        elif optimal_min - 5 <= temperature <= optimal_max + 5:
            advantage += 15
        else:
            advantage -= 10
        
        # Wind advantage
        wind_tolerance = species_info["wind_tolerance"]
        if wind_speed <= wind_tolerance / 3:
            advantage += 20
        elif wind_speed <= wind_tolerance:
            advantage += 10
        else:
            advantage -= 15
        
        # Pressure advantage
        if pressure >= 30.1:
            advantage += 10
        elif pressure <= 29.9:
            advantage -= 10
        
        return max(0, min(100, advantage))
    
    def _calculate_time_advantage(self, species_info: Dict, current_time: datetime) -> float:
        """Calculate time advantage score"""
        current_hour = current_time.hour
        peak_hours = species_info["peak_activity_hours"]
        
        for start_hour, end_hour in peak_hours:
            if start_hour <= current_hour <= end_hour:
                return 95  # Peak activity time
            elif start_hour - 1 <= current_hour <= end_hour + 1:
                return 80  # Near peak time
            elif start_hour - 2 <= current_hour <= end_hour + 2:
                return 60  # Extended peak time
        
        return 30  # Off-peak time
    
    def _calculate_seasonal_advantage(self, species_info: Dict, current_time: datetime) -> float:
        """Calculate seasonal advantage score"""
        current_month = current_time.month
        rut_start, rut_end = species_info["rut_season"]
        
        if rut_start <= current_month <= rut_end:
            return 95  # Peak rut season
        elif rut_start - 1 <= current_month <= rut_end + 1:
            return 80  # Near rut season
        elif rut_start - 2 <= current_month <= rut_end + 2:
            return 60  # Extended rut season
        else:
            return 40  # Off-season
    
    def _calculate_location_advantage(self, location: str, species: str) -> float:
        """Calculate location advantage score"""
        if "colebrook" in location.lower() or "coos" in location.lower():
            if species == "Moose":
                return 90  # Excellent moose habitat
            elif species == "White-tailed Deer":
                return 85  # Good deer habitat
            elif species == "Black Bear":
                return 80  # Good bear habitat
            else:
                return 75
        else:
            return 60  # Unknown location
    
    def _get_overall_rating(self, effectiveness: float) -> str:
        """Get overall rating based on effectiveness score"""
        if effectiveness >= 85:
            return "Excellent"
        elif effectiveness >= 70:
            return "Very Good"
        elif effectiveness >= 55:
            return "Good"
        elif effectiveness >= 40:
            return "Fair"
        else:
            return "Poor"
    
    def _generate_advanced_recommendations(self, species_info: Dict, temperature: float, wind_speed: float, 
                                         condition: str, current_time: datetime, effectiveness: float) -> List[str]:
        """Generate advanced hunting recommendations"""
        recommendations = []
        
        # Overall effectiveness
        if effectiveness >= 80:
            recommendations.append("Excellent hunting conditions - High success probability")
        elif effectiveness >= 60:
            recommendations.append("Good hunting conditions - Moderate success probability")
        else:
            recommendations.append("Poor hunting conditions - Consider waiting for better weather")
        
        # Temperature recommendations
        optimal_min, optimal_max = species_info["optimal_temp_range"]
        if optimal_min <= temperature <= optimal_max:
            recommendations.append(f"Optimal temperature range ({optimal_min}-{optimal_max}°F) for {species_info['feeding_patterns'].lower()} activity")
        elif temperature < optimal_min:
            recommendations.append("Cold temperatures - Animals may be less active")
        else:
            recommendations.append("Warm temperatures - Animals may seek shade")
        
        # Wind recommendations
        wind_tolerance = species_info["wind_tolerance"]
        if wind_speed <= wind_tolerance / 2:
            recommendations.append("Light winds - Excellent for stalking and scent control")
        elif wind_speed <= wind_tolerance:
            recommendations.append("Moderate winds - Good for hunting")
        else:
            recommendations.append("Strong winds - May affect animal movement and shot accuracy")
        
        # Time recommendations
        current_hour = current_time.hour
        peak_hours = species_info["peak_activity_hours"]
        if any(start <= current_hour <= end for start, end in peak_hours):
            recommendations.append("Prime hunting time - Animals most active")
        else:
            recommendations.append("Consider hunting during peak activity hours")
        
        # Seasonal recommendations
        current_month = current_time.month
        rut_start, rut_end = species_info["rut_season"]
        if rut_start <= current_month <= rut_end:
            recommendations.append("Peak rut season - Animals most active and vocal")
        elif rut_start - 1 <= current_month <= rut_end + 1:
            recommendations.append("Near rut season - Good hunting opportunities")
        
        return recommendations
    
    def _assess_advanced_risks(self, temperature: float, wind_speed: float, condition: str, current_time: datetime) -> List[str]:
        """Assess advanced hunting risks"""
        risks = []
        
        # Weather risks
        if wind_speed > 25:
            risks.append("Extreme wind speeds - Dangerous hunting conditions")
        if temperature < 0:
            risks.append("Sub-zero temperatures - Hypothermia risk")
        if temperature > 90:
            risks.append("Extreme heat - Heat exhaustion risk")
        if condition in ["Heavy Rain", "Snow", "Fog"]:
            risks.append("Poor visibility - Safety and accuracy concerns")
        
        # Time risks
        current_hour = current_time.hour
        if current_hour < 5 or current_hour > 21:
            risks.append("Limited visibility - Night hunting safety concerns")
        
        # Equipment risks
        if temperature < 20:
            risks.append("Cold weather - Equipment may malfunction")
        if condition == "Rain":
            risks.append("Wet conditions - Equipment protection needed")
        
        return risks
    
    def _analyze_advanced_opportunities(self, species_info: Dict, temperature: float, wind_speed: float, 
                                      condition: str, current_time: datetime) -> List[str]:
        """Analyze advanced hunting opportunities"""
        opportunities = []
        
        # Weather opportunities
        if wind_speed <= 5:
            opportunities.append("Light winds - Excellent for scent control and stalking")
        if 20 <= temperature <= 60:
            opportunities.append("Comfortable temperatures - Extended hunting time possible")
        if condition == "Clear":
            opportunities.append("Clear skies - Good visibility and tracking conditions")
        if condition == "Overcast":
            opportunities.append("Overcast skies - Reduced shadows, good for movement")
        
        # Time opportunities
        current_hour = current_time.hour
        if 6 <= current_hour <= 8:
            opportunities.append("Morning prime time - Animals feeding and moving")
        if 17 <= current_hour <= 19:
            opportunities.append("Evening prime time - Animals returning to feed")
        
        # Seasonal opportunities
        current_month = current_time.month
        rut_start, rut_end = species_info["rut_season"]
        if rut_start <= current_month <= rut_end:
            opportunities.append("Rut season - Animals most active and vocal")
        
        return opportunities
    
    def _provide_advanced_tactical_advice(self, species_info: Dict, temperature: float, wind_speed: float, 
                                        condition: str, current_time: datetime) -> List[str]:
        """Provide advanced tactical hunting advice"""
        advice = []
        
        # Wind tactics
        if wind_speed <= 5:
            advice.append("Use wind to your advantage - Approach from downwind")
        if wind_speed > 10:
            advice.append("Strong winds - Use terrain features for wind breaks")
        
        # Time tactics
        current_hour = current_time.hour
        if 6 <= current_hour <= 8:
            advice.append("Morning hunt - Focus on feeding areas and travel corridors")
        if 17 <= current_hour <= 19:
            advice.append("Evening hunt - Set up near food sources and water")
        if 10 <= current_hour <= 15:
            advice.append("Midday hunt - Focus on bedding areas and thick cover")
        
        # Weather tactics
        if condition == "Overcast":
            advice.append("Overcast conditions - Good for movement, less shadows")
        if condition == "Light Rain":
            advice.append("Light rain - May mask human scent and movement")
        if temperature <= 40:
            advice.append("Cold weather - Animals more active, less cautious")
        
        # Species-specific tactics
        feeding_patterns = species_info["feeding_patterns"]
        if feeding_patterns == "Crepuscular":
            advice.append("Crepuscular species - Focus on dawn and dusk activity")
        elif feeding_patterns == "Diurnal":
            advice.append("Diurnal species - Active during daylight hours")
        
        return advice
    
    def _suggest_advanced_equipment(self, temperature: float, condition: str, wind_speed: float, species: str) -> List[str]:
        """Suggest advanced equipment recommendations"""
        suggestions = []
        
        # Clothing recommendations
        if temperature < 30:
            suggestions.append("Heavy insulated clothing and boots")
        elif temperature < 50:
            suggestions.append("Medium-weight clothing with layers")
        else:
            suggestions.append("Lightweight, breathable clothing")
        
        # Weather protection
        if condition in ["Rain", "Snow"]:
            suggestions.append("Waterproof outer layer and rain cover for equipment")
        if wind_speed > 15:
            suggestions.append("Wind-resistant clothing and face protection")
        
        # Species-specific equipment
        if species == "Moose":
            suggestions.append("Large caliber rifle (.30-06 or larger) with scope")
            suggestions.append("Moose calls for rut season")
        elif species == "White-tailed Deer":
            suggestions.append("Medium caliber rifle (.243 to .30-06) with scope")
            suggestions.append("Deer calls and scent attractants")
        elif species == "Black Bear":
            suggestions.append("Heavy caliber rifle (.30-06 or larger) with scope")
            suggestions.append("Bear spray and bear calls")
        
        # General equipment
        suggestions.append("Quality binoculars for spotting")
        suggestions.append("Range finder for accurate shooting")
        suggestions.append("GPS or compass for navigation")
        suggestions.append("First aid kit and emergency supplies")
        
        return suggestions

# Global instance
advanced_hunting_analytics = AdvancedHuntingAnalyticsService()
