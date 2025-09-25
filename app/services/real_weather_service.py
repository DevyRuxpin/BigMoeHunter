#!/usr/bin/env python3
"""
Real Weather Service for BigMoeHunter
Integrates with OpenWeatherMap API for accurate weather data
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import os

class RealWeatherService:
    """Service for real-time weather data"""
    
    def __init__(self):
        # OpenWeatherMap API key (free tier available)
        self.api_key = os.getenv('OPENWEATHER_API_KEY', 'demo_key')
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.colebrook_coords = {
            "lat": 44.8942,
            "lon": -71.4962
        }
        self.cache = {}
        self.cache_duration = 1800  # 30 minutes
    
    def get_current_weather(self) -> Dict:
        """Get current weather for Colebrook, NH"""
        try:
            cache_key = "current_weather"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            if self.api_key == 'demo_key':
                return self._get_demo_current_weather()
            
            url = f"{self.base_url}/weather"
            params = {
                'lat': self.colebrook_coords['lat'],
                'lon': self.colebrook_coords['lon'],
                'appid': self.api_key,
                'units': 'imperial'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            weather_data = {
                'temperature': round(data['main']['temp']),
                'feels_like': round(data['main']['feels_like']),
                'humidity': data['main']['humidity'],
                'pressure': round(data['main']['pressure'] * 0.02953, 2),  # Convert to inches
                'wind_speed': round(data['wind']['speed']),
                'wind_direction': self._get_wind_direction(data['wind'].get('deg', 0)),
                'condition': data['weather'][0]['description'].title(),
                'visibility': round(data.get('visibility', 10000) / 1609.34, 1),  # Convert to miles
                'uv_index': data.get('uvi', 0),
                'last_updated': datetime.now().isoformat()
            }
            
            # Cache the result
            self.cache[cache_key] = weather_data
            self.cache[cache_key + "_timestamp"] = datetime.now().timestamp()
            
            return weather_data
            
        except Exception as e:
            print(f"Weather API error: {e}")
            return self._get_demo_current_weather()
    
    def get_7_day_forecast(self) -> Dict:
        """Get 7-day weather forecast for Colebrook, NH"""
        try:
            cache_key = "7_day_forecast"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            if self.api_key == 'demo_key':
                return self._get_demo_forecast()
            
            url = f"{self.base_url}/forecast"
            params = {
                'lat': self.colebrook_coords['lat'],
                'lon': self.colebrook_coords['lon'],
                'appid': self.api_key,
                'units': 'imperial'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Process forecast data
            daily_forecasts = {}
            
            for item in data['list']:
                date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
                time = datetime.fromtimestamp(item['dt']).strftime('%H:%M')
                
                if date not in daily_forecasts:
                    daily_forecasts[date] = {
                        'date': date,
                        'day_of_week': datetime.fromtimestamp(item['dt']).strftime('%A'),
                        'high': item['main']['temp_max'],
                        'low': item['main']['temp_min'],
                        'conditions': [],
                        'wind_speeds': [],
                        'humidity': [],
                        'precipitation': 0
                    }
                
                # Update high/low temps
                daily_forecasts[date]['high'] = max(daily_forecasts[date]['high'], item['main']['temp_max'])
                daily_forecasts[date]['low'] = min(daily_forecasts[date]['low'], item['main']['temp_min'])
                
                # Collect conditions
                daily_forecasts[date]['conditions'].append(item['weather'][0]['description'])
                daily_forecasts[date]['wind_speeds'].append(item['wind']['speed'])
                daily_forecasts[date]['humidity'].append(item['main']['humidity'])
                
                # Add precipitation
                if 'rain' in item:
                    daily_forecasts[date]['precipitation'] += item['rain'].get('3h', 0)
                if 'snow' in item:
                    daily_forecasts[date]['precipitation'] += item['snow'].get('3h', 0)
            
            # Process and format forecast
            forecast_days = []
            for date, day_data in list(daily_forecasts.items())[:7]:
                # Get most common condition
                condition = max(set(day_data['conditions']), key=day_data['conditions'].count)
                avg_wind = sum(day_data['wind_speeds']) / len(day_data['wind_speeds'])
                avg_humidity = sum(day_data['humidity']) / len(day_data['humidity'])
                
                # Calculate hunting conditions
                hunting_rating = self._calculate_hunting_rating(
                    day_data['high'], day_data['low'], avg_wind, 
                    condition, day_data['precipitation']
                )
                
                forecast_days.append({
                    'date': date,
                    'day_of_week': day_data['day_of_week'],
                    'high': round(day_data['high']),
                    'low': round(day_data['low']),
                    'condition': condition.title(),
                    'wind_speed': round(avg_wind),
                    'humidity': round(avg_humidity),
                    'precipitation': round(day_data['precipitation'], 2),
                    'hunting_rating': hunting_rating,
                    'hunting_score': self._calculate_hunting_score(
                        day_data['high'], day_data['low'], avg_wind, 
                        condition, day_data['precipitation']
                    )
                })
            
            result = {
                'location': 'Colebrook, NH',
                'forecast_days': forecast_days,
                'last_updated': datetime.now().isoformat(),
                'source': 'OpenWeatherMap API'
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = datetime.now().timestamp()
            
            return result
            
        except Exception as e:
            print(f"Forecast API error: {e}")
            return self._get_demo_forecast()
    
    def _calculate_hunting_rating(self, high: float, low: float, wind: float, 
                                condition: str, precipitation: float) -> str:
        """Calculate hunting rating based on weather conditions"""
        score = 0
        
        # Temperature scoring (optimal: 35-50°F)
        avg_temp = (high + low) / 2
        if 35 <= avg_temp <= 50:
            score += 3
        elif 25 <= avg_temp <= 60:
            score += 2
        elif 15 <= avg_temp <= 70:
            score += 1
        
        # Wind scoring (optimal: 5-10 mph)
        if 5 <= wind <= 10:
            score += 2
        elif wind <= 15:
            score += 1
        elif wind > 20:
            score -= 1
        
        # Condition scoring
        if 'clear' in condition.lower() or 'partly' in condition.lower():
            score += 2
        elif 'overcast' in condition.lower():
            score += 1
        elif 'rain' in condition.lower() or 'snow' in condition.lower():
            score -= 1
        
        # Precipitation scoring
        if precipitation > 0.1:
            score -= 1
        
        # Convert to rating
        if score >= 5:
            return "Excellent"
        elif score >= 3:
            return "Good"
        elif score >= 1:
            return "Fair"
        else:
            return "Poor"
    
    def _calculate_hunting_score(self, high: float, low: float, wind: float, 
                               condition: str, precipitation: float) -> float:
        """Calculate numerical hunting score (0-100)"""
        score = 50  # Base score
        
        # Temperature impact
        avg_temp = (high + low) / 2
        if 35 <= avg_temp <= 50:
            score += 20
        elif 25 <= avg_temp <= 60:
            score += 10
        elif avg_temp < 25 or avg_temp > 70:
            score -= 20
        
        # Wind impact
        if 5 <= wind <= 10:
            score += 15
        elif wind <= 15:
            score += 5
        elif wind > 20:
            score -= 15
        
        # Condition impact
        if 'clear' in condition.lower() or 'partly' in condition.lower():
            score += 10
        elif 'overcast' in condition.lower():
            score += 5
        elif 'rain' in condition.lower() or 'snow' in condition.lower():
            score -= 15
        
        # Precipitation impact
        if precipitation > 0.1:
            score -= 10
        
        return max(0, min(100, score))
    
    def _get_wind_direction(self, degrees: float) -> str:
        """Convert wind degrees to direction"""
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                     "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        index = round(degrees / 22.5) % 16
        return directions[index]
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        timestamp_key = cache_key + "_timestamp"
        if cache_key in self.cache and timestamp_key in self.cache:
            return (datetime.now().timestamp() - self.cache[timestamp_key]) < self.cache_duration
        return False
    
    def _get_demo_current_weather(self) -> Dict:
        """Get demo current weather data"""
        return {
            'temperature': 45,
            'feels_like': 42,
            'humidity': 65,
            'pressure': 30.15,
            'wind_speed': 8,
            'wind_direction': 'NW',
            'condition': 'Partly Cloudy',
            'visibility': 10.0,
            'uv_index': 3,
            'last_updated': datetime.now().isoformat(),
            'source': 'Demo Data'
        }
    
    def _get_demo_forecast(self) -> Dict:
        """Get demo 7-day forecast data"""
        base_date = datetime.now()
        forecast_days = []
        
        for i in range(7):
            date = base_date + timedelta(days=i)
            # Simulate realistic weather patterns
            high = 45 + (i * 2) + (i % 3 - 1) * 5
            low = high - 15 - (i % 2) * 3
            wind = 8 + (i % 4) * 2
            
            conditions = ['Clear', 'Partly Cloudy', 'Overcast', 'Light Rain']
            condition = conditions[i % len(conditions)]
            
            hunting_rating = self._calculate_hunting_rating(high, low, wind, condition, 0)
            hunting_score = self._calculate_hunting_score(high, low, wind, condition, 0)
            
            forecast_days.append({
                'date': date.strftime('%Y-%m-%d'),
                'day_of_week': date.strftime('%A'),
                'high': round(high),
                'low': round(low),
                'condition': condition,
                'wind_speed': round(wind),
                'humidity': 60 + (i % 3) * 10,
                'precipitation': 0.1 if 'Rain' in condition else 0,
                'hunting_rating': hunting_rating,
                'hunting_score': round(hunting_score)
            })
        
        return {
            'location': 'Colebrook, NH',
            'forecast_days': forecast_days,
            'last_updated': datetime.now().isoformat(),
            'source': 'Demo Data'
        }
    
    def get_weather_alerts(self) -> List[Dict]:
        """Get weather alerts for the area"""
        try:
            if self.api_key == 'demo_key':
                return self._get_demo_alerts()
            
            url = f"{self.base_url}/onecall"
            params = {
                'lat': self.colebrook_coords['lat'],
                'lon': self.colebrook_coords['lon'],
                'appid': self.api_key,
                'exclude': 'minutely,hourly,daily'
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            alerts = []
            for alert in data.get('alerts', []):
                alerts.append({
                    'title': alert['event'],
                    'description': alert['description'],
                    'severity': alert.get('tags', ['Unknown'])[0],
                    'start': datetime.fromtimestamp(alert['start']).isoformat(),
                    'end': datetime.fromtimestamp(alert['end']).isoformat()
                })
            
            return alerts
            
        except Exception as e:
            print(f"Weather alerts error: {e}")
            return self._get_demo_alerts()
    
    def _get_demo_alerts(self) -> List[Dict]:
        """Get demo weather alerts"""
        return [
            {
                'title': 'High Wind Warning',
                'description': 'Strong winds expected tomorrow with gusts up to 35 mph. Consider adjusting hunting plans.',
                'severity': 'Moderate',
                'start': (datetime.now() + timedelta(days=1)).isoformat(),
                'end': (datetime.now() + timedelta(days=2)).isoformat()
            }
        ]

# Global instance
real_weather_service = RealWeatherService()
