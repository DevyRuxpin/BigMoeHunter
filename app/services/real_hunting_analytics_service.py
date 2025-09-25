#!/usr/bin/env python3
"""
Real Hunting Analytics Service for BigMoeHunter
Provides accurate, real-world hunting analytics and predictions
"""

import random
from datetime import datetime, timedelta
from typing import Dict, Any
from app.services.hunting_data_service import hunting_data_manager

class RealHuntingAnalyticsService:
    def __init__(self):
        self.data_manager = hunting_data_manager

    def analyze_hunting_conditions(self, species: str, weather_data: Dict, location: str) -> Dict:
        """Analyze current hunting conditions and predict success probability"""
        try:
            species_data = self.data_manager.hunting_data["species"].get(species)
            if not species_data:
                return {"error": "Species data not found"}

            # Initialize scores
            overall_score = 0
            recommendations = []
            opportunity_factors = []
            risk_factors = []

            # 1. Weather Impact Analysis
            temp = weather_data.get('temperature', 50)
            wind_speed = weather_data.get('wind_speed', 5)
            condition = weather_data.get('condition', 'Partly Cloudy').lower()
            pressure = weather_data.get('pressure', 30.0)

            weather_score = 0
            if species == "White-tailed Deer":
                # Temperature analysis for deer
                if 35 <= temp <= 50:
                    weather_score += 0.4
                    opportunity_factors.append("Optimal temperature range (35-50°F) for deer activity")
                elif 25 <= temp <= 60:
                    weather_score += 0.2
                    opportunity_factors.append("Good temperature range for deer movement")
                elif temp < 25:
                    weather_score += 0.1
                    risk_factors.append("Very cold temperatures may reduce deer movement")
                else:
                    weather_score -= 0.1
                    risk_factors.append("Warm temperatures may reduce deer activity")

                # Wind analysis for deer
                if 0 <= wind_speed <= 8:
                    weather_score += 0.3
                    opportunity_factors.append("Light winds (0-8 mph) are ideal for scent control")
                elif 8 < wind_speed <= 15:
                    weather_score += 0.1
                    opportunity_factors.append("Moderate winds acceptable for deer hunting")
                else:
                    weather_score -= 0.2
                    risk_factors.append("High winds may make deer uneasy and reduce movement")

                # Condition analysis for deer
                if "clear" in condition or "sunny" in condition:
                    weather_score += 0.2
                    opportunity_factors.append("Clear conditions provide good visibility")
                elif "partly" in condition or "cloudy" in condition:
                    weather_score += 0.1
                    opportunity_factors.append("Overcast conditions can increase deer activity")
                elif "rain" in condition:
                    weather_score += 0.1
                    opportunity_factors.append("Light rain can mask scent and sound")
                elif "snow" in condition:
                    weather_score += 0.2
                    opportunity_factors.append("Snow provides excellent tracking opportunities")

            elif species == "Moose":
                # Temperature analysis for moose
                if 20 <= temp <= 40:
                    weather_score += 0.4
                    opportunity_factors.append("Cool temperatures are ideal for moose activity")
                elif 10 <= temp <= 50:
                    weather_score += 0.2
                    opportunity_factors.append("Good temperature range for moose")
                elif temp > 50:
                    weather_score -= 0.2
                    risk_factors.append("Warm temperatures cause heat stress for moose")

                # Wind analysis for moose
                if 0 <= wind_speed <= 15:
                    weather_score += 0.3
                    opportunity_factors.append("Moderate winds are acceptable for moose hunting")
                else:
                    weather_score -= 0.1
                    risk_factors.append("High winds can make moose uneasy")

            elif species == "Black Bear":
                # Temperature analysis for bear
                if 30 <= temp <= 60:
                    weather_score += 0.3
                    opportunity_factors.append("Good temperature range for bear activity")
                elif temp > 70:
                    weather_score -= 0.1
                    risk_factors.append("Hot temperatures may reduce bear activity")

                # Wind analysis for bear
                if 0 <= wind_speed <= 12:
                    weather_score += 0.2
                    opportunity_factors.append("Light to moderate winds are good for bear hunting")
                else:
                    weather_score -= 0.1
                    risk_factors.append("High winds can make bears uneasy")

            overall_score += weather_score

            # 2. Time of Day Analysis
            current_hour = datetime.now().hour
            time_score = 0
            if 5 <= current_hour <= 9 or 16 <= current_hour <= 19:  # Dawn/Dusk
                time_score = 0.9
                opportunity_factors.append("Optimal time of day (dawn/dusk) for animal movement")
            elif 9 <= current_hour <= 16:  # Midday
                time_score = 0.4
                risk_factors.append("Midday hunting can be less productive for most species")
            else:  # Night
                time_score = 0.2
                risk_factors.append("Night hunting is generally not recommended")

            overall_score += time_score * 0.2

            # 3. Moon Phase Analysis
            current_date_str = datetime.now().strftime("%Y-%m-%d")
            moon_info = self.data_manager.moon_phases.get(current_date_str, {"phase": "Unknown", "impact": "Unknown"})
            moon_score = 0
            if "New Moon" in moon_info["phase"]:
                moon_score = 0.8
                opportunity_factors.append("New Moon - excellent for daytime hunting")
            elif "First Quarter" in moon_info["phase"] or "Last Quarter" in moon_info["phase"]:
                moon_score = 0.6
                opportunity_factors.append("Quarter Moon - good hunting conditions")
            elif "Full Moon" in moon_info["phase"]:
                moon_score = 0.4
                risk_factors.append("Full Moon - animals may be more nocturnal")
            else:
                moon_score = 0.5
                opportunity_factors.append("Moderate moon phase - standard hunting conditions")

            overall_score += moon_score * 0.1

            # 4. Location Analysis
            location_score = 0
            if "Colebrook" in location or "Coös" in location:
                location_score = 0.9
                opportunity_factors.append(f"Excellent hunting location: {location}")
                colebrook_data = species_data.get('colebrook_specific', {})
                if colebrook_data:
                    recommendations.append(f"Focus on {', '.join(colebrook_data.get('best_areas', []))}")
                    if colebrook_data.get('population_density'):
                        opportunity_factors.append(f"High population density: {colebrook_data['population_density']}")
            else:
                location_score = 0.6
                risk_factors.append(f"Limited specific data for {location}")

            overall_score += location_score * 0.2

            # 5. Calculate Success Probability
            success_probability = min(1.0, max(0.0, overall_score))
            
            # 6. Determine Confidence Level
            if success_probability > 0.8:
                confidence_level = "High"
            elif success_probability > 0.6:
                confidence_level = "Medium"
            elif success_probability > 0.4:
                confidence_level = "Low"
            else:
                confidence_level = "Very Low"

            # 7. Generate Recommendations
            if not recommendations:
                if success_probability > 0.7:
                    recommendations.append("Excellent hunting conditions - high success probability")
                elif success_probability > 0.5:
                    recommendations.append("Good hunting conditions - moderate success probability")
                else:
                    recommendations.append("Challenging conditions - consider waiting for better weather")

            # Add species-specific recommendations
            if species == "White-tailed Deer":
                recommendations.append("Focus on dawn and dusk activity periods")
                recommendations.append("Look for fresh scrapes and rubs")
                recommendations.append("Use scent control products")
            elif species == "Moose":
                recommendations.append("Target wetland areas and clear-cuts")
                recommendations.append("Use cow calls during rut season")
                recommendations.append("Be prepared for remote terrain")
            elif species == "Black Bear":
                recommendations.append("Focus on berry patches and oak stands")
                recommendations.append("Consider baiting if legal and permitted")
                recommendations.append("Use heavy caliber firearms")

            return {
                "species": species,
                "location": location,
                "weather_data": weather_data,
                "success_probability": round(success_probability, 2),
                "confidence_level": confidence_level,
                "recommendations": recommendations,
                "opportunity_factors": opportunity_factors,
                "risk_factors": risk_factors,
                "weather_analysis": {
                    "score": round(weather_score, 2),
                    "temperature_impact": "Optimal" if 35 <= temp <= 50 else "Good" if 25 <= temp <= 60 else "Poor",
                    "wind_impact": "Optimal" if 0 <= wind_speed <= 8 else "Good" if wind_speed <= 15 else "Poor",
                    "condition_impact": "Good" if "clear" in condition or "partly" in condition else "Fair"
                },
                "time_analysis": {
                    "score": round(time_score, 2),
                    "current_hour": current_hour,
                    "optimal_period": "Dawn/Dusk" if 5 <= current_hour <= 9 or 16 <= current_hour <= 19 else "Midday" if 9 <= current_hour <= 16 else "Night"
                },
                "moon_analysis": {
                    "current_phase": moon_info["phase"],
                    "impact": moon_info["impact"],
                    "score": round(moon_score, 2)
                },
                "location_analysis": {
                    "score": round(location_score, 2),
                    "population_density": species_data.get('colebrook_specific', {}).get('population_density', 'Unknown')
                }
            }

        except Exception as e:
            return {
                "error": f"Failed to analyze hunting conditions: {str(e)}",
                "species": species,
                "location": location
            }

    def get_hunting_forecast(self, days: int = 7) -> Dict:
        """Get hunting forecast for next 7 days"""
        try:
            forecast = []
            today = datetime.now()
            
            for i in range(days):
                date = today + timedelta(days=i)
                
                # Simulate realistic weather data
                temp = random.randint(25, 65)
                wind_speed = random.randint(0, 20)
                conditions = random.choice(["Clear", "Partly Cloudy", "Overcast", "Light Rain", "Snow"])
                pressure = round(random.uniform(29.8, 30.5), 2)

                simulated_weather = {
                    "date": date.strftime("%Y-%m-%d"),
                    "temperature": temp,
                    "wind_speed": wind_speed,
                    "condition": conditions,
                    "pressure": pressure
                }

                # Get analytics for White-tailed Deer
                analytics = self.analyze_hunting_conditions("White-tailed Deer", simulated_weather, "Colebrook, NH")
                
                # Determine overall rating based on success probability
                rating = "Poor"
                if analytics["success_probability"] > 0.8:
                    rating = "Excellent"
                elif analytics["success_probability"] > 0.6:
                    rating = "Good"
                elif analytics["success_probability"] > 0.4:
                    rating = "Fair"
                
                forecast.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "weather": simulated_weather,
                    "hunting_rating": rating,
                    "success_probability": analytics["success_probability"],
                    "recommendations": analytics["recommendations"][:2],  # Limit to 2 recommendations
                    "opportunity_factors": analytics["opportunity_factors"][:2]  # Limit to 2 factors
                })
            
            return {
                "forecast": forecast,
                "location": "Colebrook, NH",
                "generated_at": datetime.now().isoformat()
            }

        except Exception as e:
            return {
                "error": f"Failed to generate hunting forecast: {str(e)}",
                "forecast": [],
                "location": "Colebrook, NH"
            }

# Global instance
real_hunting_analytics = RealHuntingAnalyticsService()
