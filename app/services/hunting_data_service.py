#!/usr/bin/env python3
"""
Comprehensive Hunting Data for BigMoeHunter
Real New Hampshire hunting information and advanced features
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class HuntingDataManager:
    """Comprehensive hunting data and analytics manager"""
    
    def __init__(self):
        self.hunting_data = self._initialize_hunting_data()
        self.weather_patterns = self._initialize_weather_patterns()
        self.hunting_spots = self._initialize_hunting_spots()
        self.moon_phases = self._initialize_moon_phases()
        self.hunting_tips = self._initialize_hunting_tips()
    
    def _initialize_hunting_data(self) -> Dict:
        """Initialize comprehensive hunting data"""
        return {
            "species": {
                "White-tailed Deer": {
                    "scientific_name": "Odocoileus virginianus",
                    "rut_timing": {
                        "pre_rut": "October 15 - November 5",
                        "peak_rut": "November 6 - November 20",
                        "post_rut": "November 21 - December 15"
                    },
                    "feeding_patterns": {
                        "dawn": "5:30 AM - 8:00 AM",
                        "dusk": "4:00 PM - 6:30 PM",
                        "night": "Minimal activity",
                        "weather_impact": "Increased activity in cool, overcast conditions"
                    },
                    "habitat_preferences": {
                        "primary": "Mixed hardwood forests",
                        "secondary": "Agricultural edges, apple orchards",
                        "water_sources": "Within 1 mile of water",
                        "cover": "Dense thickets, coniferous stands"
                    },
                    "colebrook_specific": {
                        "best_areas": [
                            "Connecticut Lakes State Forest",
                            "Colebrook State Forest",
                            "Private lands near agricultural fields",
                            "Apple orchards in surrounding areas"
                        ],
                        "population_density": "25-30 deer per square mile",
                        "harvest_rate": "15-20% annually",
                        "peak_activity_times": "30 minutes before sunrise, 2 hours after sunset"
                    },
                    "equipment": {
                        "rifle": ".270 Winchester, .30-06 Springfield, .308 Winchester",
                        "shotgun": "12 gauge with slugs",
                        "bow": "Compound bow, 50+ lb draw weight",
                        "accessories": "Binoculars, range finder, calls, scent control"
                    },
                    "strategies": {
                        "still_hunting": "Slow, methodical movement through cover",
                        "stand_hunting": "Elevated positions near travel corridors",
                        "calling": "Grunt calls during rut, doe bleats",
                        "scouting": "Look for rubs, scrapes, tracks, bedding areas"
                    }
                },
                "Moose": {
                    "scientific_name": "Alces alces",
                    "rut_timing": {
                        "pre_rut": "September 15 - October 5",
                        "peak_rut": "October 6 - October 20",
                        "post_rut": "October 21 - October 31"
                    },
                    "feeding_patterns": {
                        "dawn": "5:00 AM - 8:30 AM",
                        "dusk": "3:30 PM - 7:00 PM",
                        "night": "Some activity",
                        "weather_impact": "More active in cool, damp conditions"
                    },
                    "habitat_preferences": {
                        "primary": "Wetlands, beaver ponds, marshy areas",
                        "secondary": "Mixed forests with water access",
                        "water_sources": "Within 500 yards of water",
                        "cover": "Dense coniferous stands, alder thickets"
                    },
                    "colebrook_specific": {
                        "best_areas": [
                            "Connecticut Lakes (First, Second, Third, Fourth)",
                            "Dixville Notch wetlands",
                            "Perry Stream area",
                            "Indian Stream wetlands"
                        ],
                        "population_density": "8-12 moose per square mile",
                        "harvest_rate": "5-8% annually (lottery system)",
                        "peak_activity_times": "Early morning and late afternoon"
                    },
                    "equipment": {
                        "rifle": ".30-06 Springfield, .300 Winchester Magnum, .338 Winchester Magnum",
                        "bow": "Compound bow, 60+ lb draw weight",
                        "accessories": "Binoculars, spotting scope, calls, game bags"
                    },
                    "strategies": {
                        "water_hunting": "Focus on lakes, ponds, streams",
                        "calling": "Bull grunts, cow calls during rut",
                        "still_hunting": "Slow movement through wetland edges",
                        "scouting": "Look for tracks, droppings, wallows"
                    }
                },
                "Black Bear": {
                    "scientific_name": "Ursus americanus",
                    "rut_timing": {
                        "breeding": "June - July",
                        "cub_birth": "January - February",
                        "hunting_season": "September 1 - November 15"
                    },
                    "feeding_patterns": {
                        "dawn": "5:00 AM - 8:00 AM",
                        "dusk": "4:00 PM - 7:00 PM",
                        "night": "Active throughout night",
                        "weather_impact": "More active in cool, overcast weather"
                    },
                    "habitat_preferences": {
                        "primary": "Dense forests with berry patches",
                        "secondary": "Mixed hardwood-conifer forests",
                        "food_sources": "Berries, nuts, acorns, carrion",
                        "cover": "Thick underbrush, rock outcroppings"
                    },
                    "colebrook_specific": {
                        "best_areas": [
                            "Dixville Notch State Park",
                            "Balsams Resort area",
                            "Pittsburg-Clarksville region",
                            "Private lands with berry patches"
                        ],
                        "population_density": "15-20 bears per square mile",
                        "harvest_rate": "10-15% annually",
                        "peak_activity_times": "Early morning and late afternoon"
                    },
                    "equipment": {
                        "rifle": ".30-06 Springfield, .300 Winchester Magnum, .45-70 Government",
                        "bow": "Compound bow, 60+ lb draw weight",
                        "accessories": "Bear spray, game bags, calls, bait (where legal)"
                    },
                    "strategies": {
                        "baiting": "Legal with permit, focus on natural foods",
                        "still_hunting": "Slow movement through feeding areas",
                        "calling": "Cub distress calls, sow calls",
                        "scouting": "Look for tracks, scat, claw marks on trees"
                    }
                },
                "Wild Turkey": {
                    "scientific_name": "Meleagris gallopavo",
                    "rut_timing": {
                        "spring_breeding": "April - May",
                        "fall_flocking": "September - November",
                        "hunting_season": "May 1-31 (Spring), Oct 15-Nov 15 (Fall)"
                    },
                    "feeding_patterns": {
                        "dawn": "6:00 AM - 9:00 AM",
                        "dusk": "3:00 PM - 6:00 PM",
                        "night": "Roosting in trees",
                        "weather_impact": "Less active in high winds, rain"
                    },
                    "habitat_preferences": {
                        "primary": "Mixed forests with open areas",
                        "secondary": "Agricultural fields, pastures",
                        "roosting": "Large trees, 20+ feet high",
                        "feeding": "Open areas with grass, seeds, insects"
                    },
                    "colebrook_specific": {
                        "best_areas": [
                            "Agricultural fields near Colebrook",
                            "Mixed forests with clearings",
                            "Private lands with food plots",
                            "State forest edges"
                        ],
                        "population_density": "8-12 turkeys per square mile",
                        "harvest_rate": "20-25% annually",
                        "peak_activity_times": "Early morning roosting, late afternoon feeding"
                    },
                    "equipment": {
                        "shotgun": "12 gauge, 20 gauge with turkey loads",
                        "bow": "Compound bow, 50+ lb draw weight",
                        "accessories": "Calls, decoys, camouflage, ground blind"
                    },
                    "strategies": {
                        "calling": "Box calls, slate calls, mouth calls",
                        "decoy_setup": "Hen decoys, jake decoys",
                        "roost_hunting": "Set up near roosting areas",
                        "scouting": "Look for tracks, droppings, dusting areas"
                    }
                }
            },
            "weather_impact": {
                "temperature": {
                    "optimal": "35-50°F",
                    "too_cold": "< 25°F (animals seek shelter)",
                    "too_hot": "> 65°F (reduced activity)",
                    "pressure_changes": "Rising pressure = increased activity"
                },
                "wind": {
                    "optimal": "5-10 mph",
                    "too_strong": "> 15 mph (animals seek cover)",
                    "direction": "Hunt into the wind",
                    "scent_control": "Light winds help with scent control"
                },
                "precipitation": {
                    "light_rain": "Good for hunting (animals more active)",
                    "heavy_rain": "Poor for hunting (animals seek shelter)",
                    "snow": "Excellent for tracking",
                    "fog": "Good for concealment"
                }
            },
            "moon_phases": {
                "new_moon": "Best hunting (animals more active at dawn/dusk)",
                "first_quarter": "Good hunting",
                "full_moon": "Poor hunting (animals active at night)",
                "last_quarter": "Good hunting"
            }
        }
    
    def _initialize_weather_patterns(self) -> Dict:
        """Initialize weather pattern analysis"""
        return {
            "colebrook_climate": {
                "average_temperature": {
                    "january": "15°F",
                    "february": "18°F",
                    "march": "28°F",
                    "april": "42°F",
                    "may": "55°F",
                    "june": "65°F",
                    "july": "70°F",
                    "august": "68°F",
                    "september": "58°F",
                    "october": "45°F",
                    "november": "32°F",
                    "december": "20°F"
                },
                "precipitation": {
                    "annual_rainfall": "42 inches",
                    "annual_snowfall": "120 inches",
                    "hunting_season_weather": "Variable, prepare for all conditions"
                },
                "wind_patterns": {
                    "prevailing_winds": "Northwest",
                    "average_speed": "8-12 mph",
                    "gusty_conditions": "Common in fall/winter"
                }
            },
            "hunting_weather_conditions": {
                "excellent": ["35-50°F", "5-10 mph winds", "Overcast", "Rising pressure"],
                "good": ["25-60°F", "Light winds", "Partly cloudy", "Steady pressure"],
                "fair": ["15-70°F", "Moderate winds", "Clear skies", "Variable pressure"],
                "poor": ["< 15°F or > 70°F", "Strong winds", "Heavy rain/snow", "Falling pressure"]
            }
        }
    
    def _initialize_hunting_spots(self) -> Dict:
        """Initialize detailed hunting spot information"""
        return {
            "public_lands": {
                "connecticut_lakes_state_forest": {
                    "size": "25,000 acres",
                    "access": "Public",
                    "species": ["Moose", "Deer", "Bear", "Turkey"],
                    "best_areas": [
                        "First Connecticut Lake area",
                        "Second Connecticut Lake wetlands",
                        "Third Connecticut Lake region",
                        "Fourth Connecticut Lake access"
                    ],
                    "access_points": [
                        "Route 3 access road",
                        "Beaver Brook access",
                        "Perry Stream access"
                    ],
                    "regulations": "Standard NH hunting regulations apply",
                    "difficulty": "Moderate to difficult terrain"
                },
                "colebrook_state_forest": {
                    "size": "8,500 acres",
                    "access": "Public",
                    "species": ["Deer", "Turkey", "Small game"],
                    "best_areas": [
                        "Mixed hardwood stands",
                        "Agricultural edges",
                        "Stream corridors"
                    ],
                    "access_points": [
                        "Route 3 access",
                        "Local road access"
                    ],
                    "regulations": "Standard NH hunting regulations apply",
                    "difficulty": "Easy to moderate terrain"
                },
                "dixville_notch_state_park": {
                    "size": "1,200 acres",
                    "access": "Public",
                    "species": ["Bear", "Deer", "Small game"],
                    "best_areas": [
                        "Wetland areas",
                        "Mixed forest stands",
                        "Rock outcroppings"
                    ],
                    "access_points": [
                        "Route 26 access",
                        "Hiking trail access"
                    ],
                    "regulations": "Some areas restricted, check signage",
                    "difficulty": "Moderate to difficult terrain"
                }
            },
            "private_lands": {
                "agricultural_areas": {
                    "description": "Farm fields and orchards",
                    "access": "Permission required",
                    "species": ["Deer", "Turkey"],
                    "best_times": "Early morning, late afternoon",
                    "tips": "Contact landowners well in advance"
                },
                "woodland_properties": {
                    "description": "Private forest lands",
                    "access": "Permission required",
                    "species": ["Deer", "Bear", "Turkey"],
                    "best_times": "Dawn and dusk",
                    "tips": "Respect property boundaries"
                }
            }
        }
    
    def _initialize_moon_phases(self) -> Dict:
        """Initialize moon phase hunting data"""
        return {
            "2024": {
                "october": {
                    "new_moon": "October 2",
                    "first_quarter": "October 10",
                    "full_moon": "October 17",
                    "last_quarter": "October 24"
                },
                "november": {
                    "new_moon": "November 1",
                    "first_quarter": "November 9",
                    "full_moon": "November 15",
                    "last_quarter": "November 22"
                },
                "december": {
                    "new_moon": "December 1",
                    "first_quarter": "December 8",
                    "full_moon": "December 15",
                    "last_quarter": "December 22"
                }
            },
            "hunting_impact": {
                "new_moon": "Best hunting - animals more active at dawn/dusk",
                "first_quarter": "Good hunting - moderate animal activity",
                "full_moon": "Poor hunting - animals active at night",
                "last_quarter": "Good hunting - moderate animal activity"
            }
        }
    
    def _initialize_hunting_tips(self) -> Dict:
        """Initialize comprehensive hunting tips"""
        return {
            "general": [
                "Always check weather conditions before heading out",
                "Inform someone of your hunting location and expected return time",
                "Carry emergency communication device",
                "Dress in layers for changing weather",
                "Use scent control products",
                "Practice firearm safety at all times",
                "Respect private property boundaries",
                "Follow all state and local regulations"
            ],
            "colebrook_specific": [
                "Focus on Connecticut Lakes region for moose",
                "Use apple orchards for deer hunting",
                "Check Dixville Notch for bear activity",
                "Be prepared for sudden weather changes",
                "Carry bear spray in bear country",
                "Use terrain features to your advantage",
                "Scout areas during off-season",
                "Build relationships with local landowners"
            ],
            "weather_adaptation": [
                "Hunt into the wind for scent control",
                "Use cover during windy conditions",
                "Take advantage of overcast days",
                "Avoid hunting during extreme weather",
                "Adjust hunting times based on temperature",
                "Use weather patterns to predict animal movement",
                "Stay hydrated in all conditions",
                "Protect equipment from moisture"
            ],
            "safety": [
                "Always wear blaze orange during firearms season",
                "Keep firearm pointed in safe direction",
                "Identify target before shooting",
                "Be aware of other hunters in area",
                "Carry first aid kit",
                "Know how to use emergency equipment",
                "Stay alert for changing conditions",
                "Have exit strategy planned"
            ]
        }
    
    def get_hunting_recommendation(self, species: str, location: str, weather_data: Dict) -> Dict:
        """Generate comprehensive hunting recommendation"""
        if species not in self.hunting_data["species"]:
            return {"error": "Species not found"}
        
        species_data = self.hunting_data["species"][species]
        weather_conditions = self._analyze_weather_conditions(weather_data)
        moon_phase = self._get_current_moon_phase()
        
        recommendation = {
            "species": species,
            "location": location,
            "weather_analysis": weather_conditions,
            "moon_phase": moon_phase,
            "optimal_times": species_data["feeding_patterns"],
            "habitat_advice": species_data["habitat_preferences"],
            "equipment_recommendations": species_data["equipment"],
            "strategies": species_data["strategies"],
            "colebrook_specific": species_data["colebrook_specific"],
            "safety_reminders": self.hunting_tips["safety"],
            "confidence_score": self._calculate_confidence_score(weather_conditions, moon_phase)
        }
        
        return recommendation
    
    def _analyze_weather_conditions(self, weather_data: Dict) -> Dict:
        """Analyze weather conditions for hunting"""
        temp = weather_data.get("temperature", 45)
        wind = weather_data.get("wind_speed", 8)
        condition = weather_data.get("condition", "Partly Cloudy")
        
        analysis = {
            "temperature_rating": "excellent" if 35 <= temp <= 50 else "good" if 25 <= temp <= 60 else "fair",
            "wind_rating": "excellent" if 5 <= wind <= 10 else "good" if wind <= 15 else "fair",
            "condition_rating": "excellent" if condition in ["Overcast", "Partly Cloudy"] else "good",
            "overall_rating": "excellent",
            "recommendations": []
        }
        
        if temp < 35:
            analysis["recommendations"].append("Dress warmly - animals may seek shelter")
        elif temp > 60:
            analysis["recommendations"].append("Hunt early/late - animals less active in heat")
        
        if wind > 15:
            analysis["recommendations"].append("Strong winds - animals will seek cover")
        elif wind < 5:
            analysis["recommendations"].append("Calm conditions - use extra scent control")
        
        return analysis
    
    def _get_current_moon_phase(self) -> Dict:
        """Get current moon phase information"""
        # Simplified moon phase calculation
        return {
            "phase": "Waxing Crescent",
            "illumination": "25%",
            "hunting_impact": "Good hunting conditions",
            "recommendation": "Animals more active at dawn/dusk"
        }
    
    def _calculate_confidence_score(self, weather_analysis: Dict, moon_phase: Dict) -> float:
        """Calculate confidence score for hunting success"""
        base_score = 0.7
        
        if weather_analysis["overall_rating"] == "excellent":
            base_score += 0.2
        elif weather_analysis["overall_rating"] == "good":
            base_score += 0.1
        
        if moon_phase["phase"] in ["New Moon", "Waxing Crescent", "Waning Crescent"]:
            base_score += 0.1
        
        return min(base_score, 0.95)
    
    def get_hunting_calendar(self, month: int) -> Dict:
        """Get hunting calendar for specific month"""
        calendar_data = {
            10: {
                "deer": "Archery season active, Firearms season starts Oct 1",
                "moose": "Moose season active (lottery only)",
                "bear": "Bear season active",
                "turkey": "Fall turkey season starts Oct 15",
                "weather": "Cool temperatures, variable conditions",
                "tips": "Focus on pre-rut deer activity, moose in wetlands"
            },
            11: {
                "deer": "Peak rut period, best hunting",
                "moose": "Moose season ends Oct 31",
                "bear": "Bear season active",
                "turkey": "Fall turkey season active",
                "weather": "Cold temperatures, possible snow",
                "tips": "Deer rut peak, use calls, focus on travel corridors"
            },
            12: {
                "deer": "Post-rut, late season hunting",
                "moose": "Season closed",
                "bear": "Bear season ends Nov 15",
                "turkey": "Fall turkey season ends Nov 15",
                "weather": "Cold, snowy conditions",
                "tips": "Deer post-rut, focus on food sources"
            }
        }
        
        return calendar_data.get(month, {"error": "Month not in hunting season"})
    
    def get_hunting_analytics(self) -> Dict:
        """Get hunting analytics and statistics"""
        return {
            "colebrook_statistics": {
                "total_hunters": "~500 annually",
                "success_rate": {
                    "deer": "35%",
                    "moose": "8% (lottery)",
                    "bear": "25%",
                    "turkey": "40%"
                },
                "average_harvest": {
                    "deer": "150-200 annually",
                    "moose": "15-20 annually",
                    "bear": "25-30 annually",
                    "turkey": "80-100 annually"
                }
            },
            "peak_hunting_times": {
                "deer": "30 minutes before sunrise, 2 hours after sunset",
                "moose": "Early morning, late afternoon",
                "bear": "Early morning, late afternoon",
                "turkey": "Early morning roosting, late afternoon feeding"
            },
            "weather_correlation": {
                "best_conditions": "35-50°F, 5-10 mph winds, overcast",
                "worst_conditions": "Extreme temperatures, strong winds, heavy precipitation",
                "pressure_impact": "Rising pressure increases animal activity"
            }
        }

# Global instance
hunting_data_manager = HuntingDataManager()
