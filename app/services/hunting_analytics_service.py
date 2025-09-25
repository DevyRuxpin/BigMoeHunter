#!/usr/bin/env python3
"""
Advanced Hunting Analytics Service
Real-time hunting data analysis and predictions
"""

import json
import math
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

class HuntingAnalytics:
    """Advanced hunting analytics and prediction service"""
    
    def __init__(self):
        self.weather_api_key = None  # Would be set in production
        self.hunting_data = self._initialize_analytics_data()
    
    def _initialize_analytics_data(self) -> Dict:
        """Initialize analytics data"""
        return {
            "historical_success_rates": {
                "deer": {
                    "weather_conditions": {
                        "excellent": 0.45,
                        "good": 0.35,
                        "fair": 0.25,
                        "poor": 0.15
                    },
                    "time_of_day": {
                        "dawn": 0.40,
                        "morning": 0.25,
                        "afternoon": 0.20,
                        "dusk": 0.35,
                        "night": 0.10
                    },
                    "moon_phase": {
                        "new_moon": 0.40,
                        "waxing_crescent": 0.35,
                        "first_quarter": 0.30,
                        "waxing_gibbous": 0.25,
                        "full_moon": 0.20,
                        "waning_gibbous": 0.25,
                        "last_quarter": 0.30,
                        "waning_crescent": 0.35
                    }
                },
                "moose": {
                    "weather_conditions": {
                        "excellent": 0.35,
                        "good": 0.28,
                        "fair": 0.20,
                        "poor": 0.12
                    },
                    "time_of_day": {
                        "dawn": 0.35,
                        "morning": 0.30,
                        "afternoon": 0.25,
                        "dusk": 0.32,
                        "night": 0.15
                    }
                },
                "bear": {
                    "weather_conditions": {
                        "excellent": 0.30,
                        "good": 0.25,
                        "fair": 0.20,
                        "poor": 0.15
                    },
                    "time_of_day": {
                        "dawn": 0.28,
                        "morning": 0.25,
                        "afternoon": 0.22,
                        "dusk": 0.30,
                        "night": 0.20
                    }
                }
            },
            "colebrook_specific_data": {
                "population_densities": {
                    "deer": 28,  # per square mile
                    "moose": 10,
                    "bear": 18,
                    "turkey": 10
                },
                "harvest_rates": {
                    "deer": 0.18,
                    "moose": 0.08,
                    "bear": 0.12,
                    "turkey": 0.25
                },
                "peak_activity_periods": {
                    "deer": ["5:30-8:00 AM", "4:00-6:30 PM"],
                    "moose": ["5:00-8:30 AM", "3:30-7:00 PM"],
                    "bear": ["5:00-8:00 AM", "4:00-7:00 PM"],
                    "turkey": ["6:00-9:00 AM", "3:00-6:00 PM"]
                }
            }
        }
    
    def analyze_hunting_conditions(self, species: str, weather_data: Dict, location: str) -> Dict:
        """Analyze current hunting conditions and predict success probability"""
        
        # Get base success rate for species
        base_success_rate = self.hunting_data["colebrook_specific_data"]["harvest_rates"].get(species, 0.20)
        
        # Analyze weather impact
        weather_score = self._calculate_weather_score(weather_data)
        
        # Calculate time of day impact
        time_score = self._calculate_time_score()
        
        # Calculate moon phase impact
        moon_score = self._calculate_moon_score()
        
        # Calculate location impact
        location_score = self._calculate_location_score(location, species)
        
        # Calculate overall success probability
        success_probability = self._calculate_success_probability(
            base_success_rate, weather_score, time_score, moon_score, location_score
        )
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            species, weather_data, success_probability
        )
        
        return {
            "species": species,
            "location": location,
            "success_probability": success_probability,
            "confidence_level": self._calculate_confidence_level(success_probability),
            "weather_analysis": {
                "score": weather_score,
                "impact": self._get_weather_impact_description(weather_score)
            },
            "time_analysis": {
                "score": time_score,
                "optimal_times": self.hunting_data["colebrook_specific_data"]["peak_activity_periods"].get(species, [])
            },
            "moon_analysis": {
                "score": moon_score,
                "current_phase": self._get_current_moon_phase(),
                "impact": self._get_moon_impact_description(moon_score)
            },
            "location_analysis": {
                "score": location_score,
                "population_density": self.hunting_data["colebrook_specific_data"]["population_densities"].get(species, 0)
            },
            "recommendations": recommendations,
            "risk_factors": self._identify_risk_factors(weather_data, species),
            "opportunity_factors": self._identify_opportunity_factors(weather_data, species)
        }
    
    def _calculate_weather_score(self, weather_data: Dict) -> float:
        """Calculate weather score (0-1)"""
        temp = weather_data.get("temperature", 45)
        wind_speed = weather_data.get("wind_speed", 8)
        condition = weather_data.get("condition", "Partly Cloudy")
        pressure = weather_data.get("pressure", 30.15)
        
        score = 0.5  # Base score
        
        # Temperature impact
        if 35 <= temp <= 50:
            score += 0.2
        elif 25 <= temp <= 60:
            score += 0.1
        elif temp < 25 or temp > 70:
            score -= 0.2
        
        # Wind impact
        if 5 <= wind_speed <= 10:
            score += 0.15
        elif wind_speed <= 15:
            score += 0.05
        elif wind_speed > 20:
            score -= 0.2
        
        # Condition impact
        if condition in ["Overcast", "Partly Cloudy"]:
            score += 0.1
        elif condition in ["Clear", "Sunny"]:
            score += 0.05
        elif condition in ["Heavy Rain", "Snow"]:
            score -= 0.15
        
        # Pressure impact (simplified)
        if pressure > 30.2:
            score += 0.1
        elif pressure < 29.8:
            score -= 0.1
        
        return max(0, min(1, score))
    
    def _calculate_time_score(self) -> float:
        """Calculate time of day score"""
        current_hour = datetime.now().hour
        
        if 5 <= current_hour <= 8:  # Dawn
            return 0.9
        elif 16 <= current_hour <= 19:  # Dusk
            return 0.8
        elif 9 <= current_hour <= 11:  # Morning
            return 0.6
        elif 12 <= current_hour <= 15:  # Afternoon
            return 0.4
        else:  # Night
            return 0.2
    
    def _calculate_moon_score(self) -> float:
        """Calculate moon phase score"""
        # Simplified moon phase calculation
        moon_phases = ["new_moon", "waxing_crescent", "first_quarter", "waxing_gibbous", 
                      "full_moon", "waning_gibbous", "last_quarter", "waning_crescent"]
        
        # For demo, return a random but realistic score
        current_phase = random.choice(moon_phases)
        
        phase_scores = {
            "new_moon": 0.9,
            "waxing_crescent": 0.8,
            "first_quarter": 0.7,
            "waxing_gibbous": 0.6,
            "full_moon": 0.4,
            "waning_gibbous": 0.6,
            "last_quarter": 0.7,
            "waning_crescent": 0.8
        }
        
        return phase_scores.get(current_phase, 0.6)
    
    def _calculate_location_score(self, location: str, species: str) -> float:
        """Calculate location-specific score"""
        location_scores = {
            "Connecticut Lakes": 0.9,
            "Colebrook, NH": 0.8,
            "Dixville Notch": 0.85,
            "Pittsburg": 0.75,
            "WMU A": 0.9,
            "WMU B": 0.8,
            "WMU C": 0.7
        }
        
        base_score = location_scores.get(location, 0.7)
        
        # Adjust based on species
        if species == "Moose" and "Connecticut" in location:
            base_score += 0.1
        elif species == "Bear" and "Dixville" in location:
            base_score += 0.1
        elif species == "Deer" and "Colebrook" in location:
            base_score += 0.05
        
        return min(1.0, base_score)
    
    def _calculate_success_probability(self, base_rate: float, weather: float, 
                                     time: float, moon: float, location: float) -> float:
        """Calculate overall success probability"""
        # Weighted average of factors
        weights = {
            "weather": 0.3,
            "time": 0.25,
            "moon": 0.2,
            "location": 0.25
        }
        
        weighted_score = (
            weather * weights["weather"] +
            time * weights["time"] +
            moon * weights["moon"] +
            location * weights["location"]
        )
        
        # Apply to base success rate
        success_probability = base_rate * (0.5 + weighted_score)
        
        return min(0.95, max(0.05, success_probability))
    
    def _calculate_confidence_level(self, success_probability: float) -> str:
        """Calculate confidence level"""
        if success_probability >= 0.7:
            return "High"
        elif success_probability >= 0.5:
            return "Medium"
        elif success_probability >= 0.3:
            return "Low"
        else:
            return "Very Low"
    
    def _get_weather_impact_description(self, score: float) -> str:
        """Get weather impact description"""
        if score >= 0.8:
            return "Excellent hunting weather - optimal conditions"
        elif score >= 0.6:
            return "Good hunting weather - favorable conditions"
        elif score >= 0.4:
            return "Fair hunting weather - moderate conditions"
        else:
            return "Poor hunting weather - challenging conditions"
    
    def _get_moon_impact_description(self, score: float) -> str:
        """Get moon impact description"""
        if score >= 0.8:
            return "Favorable moon phase - animals more active at dawn/dusk"
        elif score >= 0.6:
            return "Good moon phase - moderate animal activity"
        elif score >= 0.4:
            return "Fair moon phase - some animal activity"
        else:
            return "Poor moon phase - animals more active at night"
    
    def _get_current_moon_phase(self) -> str:
        """Get current moon phase"""
        phases = ["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                 "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"]
        return random.choice(phases)  # Simplified for demo
    
    def _generate_recommendations(self, species: str, weather_data: Dict, 
                                success_probability: float) -> List[str]:
        """Generate hunting recommendations"""
        recommendations = []
        
        # Base recommendations
        if success_probability >= 0.7:
            recommendations.append("Excellent hunting conditions - high success probability")
        elif success_probability >= 0.5:
            recommendations.append("Good hunting conditions - moderate success probability")
        else:
            recommendations.append("Challenging conditions - consider waiting for better weather")
        
        # Weather-specific recommendations
        temp = weather_data.get("temperature", 45)
        if temp < 35:
            recommendations.append("Dress warmly - animals may seek shelter in cold")
        elif temp > 60:
            recommendations.append("Hunt early/late - animals less active in heat")
        
        wind = weather_data.get("wind_speed", 8)
        if wind > 15:
            recommendations.append("Strong winds - animals will seek cover")
        elif wind < 5:
            recommendations.append("Calm conditions - use extra scent control")
        
        # Species-specific recommendations
        if species == "Deer":
            recommendations.append("Focus on food sources and travel corridors")
            recommendations.append("Use calls during rut season")
        elif species == "Moose":
            recommendations.append("Focus on water sources and wetlands")
            recommendations.append("Use bull grunts and cow calls")
        elif species == "Bear":
            recommendations.append("Look for berry patches and food sources")
            recommendations.append("Use bait stations where legal")
        elif species == "Turkey":
            recommendations.append("Set up near roosting areas")
            recommendations.append("Use decoys and calls")
        
        return recommendations
    
    def _identify_risk_factors(self, weather_data: Dict, species: str) -> List[str]:
        """Identify risk factors for hunting"""
        risks = []
        
        temp = weather_data.get("temperature", 45)
        wind = weather_data.get("wind_speed", 8)
        condition = weather_data.get("condition", "Partly Cloudy")
        
        if temp < 25:
            risks.append("Extreme cold - hypothermia risk")
        elif temp > 70:
            risks.append("High temperatures - heat exhaustion risk")
        
        if wind > 20:
            risks.append("Strong winds - difficult shooting conditions")
        
        if condition in ["Heavy Rain", "Snow"]:
            risks.append("Poor visibility and slippery conditions")
        
        if species == "Bear":
            risks.append("Bear encounters - carry bear spray")
        
        return risks
    
    def _identify_opportunity_factors(self, weather_data: Dict, species: str) -> List[str]:
        """Identify opportunity factors for hunting"""
        opportunities = []
        
        temp = weather_data.get("temperature", 45)
        wind = weather_data.get("wind_speed", 8)
        condition = weather_data.get("condition", "Partly Cloudy")
        
        if 35 <= temp <= 50:
            opportunities.append("Optimal temperature for animal activity")
        
        if 5 <= wind <= 10:
            opportunities.append("Perfect wind conditions for scent control")
        
        if condition in ["Overcast", "Partly Cloudy"]:
            opportunities.append("Good visibility with reduced glare")
        
        if species == "Deer" and temp < 50:
            opportunities.append("Cool temperatures increase deer movement")
        
        if species == "Moose" and condition == "Overcast":
            opportunities.append("Overcast conditions favor moose activity")
        
        return opportunities
    
    def get_hunting_forecast(self, days_ahead: int = 7) -> Dict:
        """Get hunting forecast for next N days"""
        forecast = []
        
        for i in range(days_ahead):
            date = datetime.now() + timedelta(days=i)
            
            # Simulate weather data (in production, this would come from weather API)
            weather = {
                "temperature": random.randint(25, 65),
                "wind_speed": random.randint(5, 20),
                "condition": random.choice(["Clear", "Partly Cloudy", "Overcast", "Light Rain"]),
                "pressure": round(random.uniform(29.8, 30.3), 2)
            }
            
            # Analyze conditions for each species
            species_analysis = {}
            for species in ["Deer", "Moose", "Bear", "Turkey"]:
                analysis = self.analyze_hunting_conditions(species, weather, "Colebrook, NH")
                species_analysis[species] = {
                    "success_probability": analysis["success_probability"],
                    "confidence_level": analysis["confidence_level"],
                    "weather_score": analysis["weather_analysis"]["score"]
                }
            
            forecast.append({
                "date": date.strftime("%Y-%m-%d"),
                "day_of_week": date.strftime("%A"),
                "weather": weather,
                "species_analysis": species_analysis,
                "overall_rating": self._calculate_overall_rating(species_analysis)
            })
        
        return {
            "forecast_period": f"{days_ahead} days",
            "location": "Colebrook, NH",
            "daily_forecast": forecast,
            "best_days": self._identify_best_days(forecast),
            "recommendations": self._generate_forecast_recommendations(forecast)
        }
    
    def _calculate_overall_rating(self, species_analysis: Dict) -> str:
        """Calculate overall rating for the day"""
        avg_success = sum(analysis["success_probability"] for analysis in species_analysis.values()) / len(species_analysis)
        
        if avg_success >= 0.7:
            return "Excellent"
        elif avg_success >= 0.5:
            return "Good"
        elif avg_success >= 0.3:
            return "Fair"
        else:
            return "Poor"
    
    def _identify_best_days(self, forecast: List[Dict]) -> List[Dict]:
        """Identify best hunting days from forecast"""
        best_days = []
        
        for day in forecast:
            if day["overall_rating"] in ["Excellent", "Good"]:
                best_days.append({
                    "date": day["date"],
                    "day_of_week": day["day_of_week"],
                    "rating": day["overall_rating"],
                    "best_species": max(day["species_analysis"].items(), 
                                      key=lambda x: x[1]["success_probability"])[0]
                })
        
        return sorted(best_days, key=lambda x: x["rating"], reverse=True)
    
    def _generate_forecast_recommendations(self, forecast: List[Dict]) -> List[str]:
        """Generate forecast recommendations"""
        recommendations = []
        
        excellent_days = [day for day in forecast if day["overall_rating"] == "Excellent"]
        if excellent_days:
            recommendations.append(f"Excellent hunting conditions on {len(excellent_days)} days")
        
        good_days = [day for day in forecast if day["overall_rating"] == "Good"]
        if good_days:
            recommendations.append(f"Good hunting conditions on {len(good_days)} days")
        
        # Find best species for the period
        species_scores = {}
        for day in forecast:
            for species, analysis in day["species_analysis"].items():
                if species not in species_scores:
                    species_scores[species] = []
                species_scores[species].append(analysis["success_probability"])
        
        if species_scores:
            avg_scores = {species: sum(scores)/len(scores) for species, scores in species_scores.items()}
            best_species = max(avg_scores.items(), key=lambda x: x[1])[0]
            recommendations.append(f"Best overall species: {best_species}")
        
        return recommendations

# Global instance
hunting_analytics = HuntingAnalytics()
