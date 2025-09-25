"""
Hunting API routes
Endpoints for hunting data, recommendations, and regulations
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import json

from app.models.database import WMU, Species, HuntingSeason, HuntingLocation, Regulation
from app.models import get_db
from app.services.modern_ai_service import ModernHuntingAI

router = APIRouter(prefix="/api/hunting", tags=["hunting"])

# Initialize modern AI service (Llama 3.1 via Ollama)
ai_service = ModernHuntingAI()

@router.get("/wmus")
async def get_wmus(db: Session = Depends(get_db)):
    """Get all Wildlife Management Units"""
    wmus = db.query(WMU).all()
    return [
        {
            "id": wmu.id,
            "wmu_code": wmu.wmu_code,
            "name": wmu.name,
            "description": wmu.description,
            "area_acres": wmu.area_acres
        }
        for wmu in wmus
    ]

@router.get("/species")
async def get_species(db: Session = Depends(get_db)):
    """Get all hunting species"""
    species = db.query(Species).all()
    return [
        {
            "id": species.id,
            "name": species.name,
            "scientific_name": species.scientific_name,
            "description": species.description,
            "habitat_info": species.habitat_info,
            "hunting_tips": species.hunting_tips
        }
        for species in species
    ]

@router.get("/seasons")
async def get_hunting_seasons(
    species_id: Optional[int] = None,
    wmu_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    """Get hunting seasons with optional filters"""
    query = db.query(HuntingSeason)
    
    if species_id:
        query = query.filter(HuntingSeason.species_id == species_id)
    if wmu_id:
        query = query.filter(HuntingSeason.wmu_id == wmu_id)
    
    seasons = query.all()
    return [
        {
            "id": season.id,
            "species": season.species.name if season.species else None,
            "wmu": season.wmu.name if season.wmu else None,
            "season_name": season.season_name,
            "start_date": season.start_date.isoformat() if season.start_date else None,
            "end_date": season.end_date.isoformat() if season.end_date else None,
            "bag_limit": season.bag_limit,
            "special_regulations": season.special_regulations,
            "weapon_types": season.weapon_types
        }
        for season in seasons
    ]

@router.get("/locations")
async def get_hunting_locations(
    species_id: Optional[int] = None,
    wmu_id: Optional[int] = None,
    difficulty: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get prime hunting locations with optional filters"""
    query = db.query(HuntingLocation)
    
    if species_id:
        query = query.filter(HuntingLocation.species_id == species_id)
    if wmu_id:
        query = query.filter(HuntingLocation.wmu_id == wmu_id)
    if difficulty:
        query = query.filter(HuntingLocation.difficulty_level == difficulty)
    
    locations = query.all()
    return [
        {
            "id": location.id,
            "name": location.name,
            "description": location.description,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "species": location.species.name if location.species else None,
            "wmu": location.wmu.name if location.wmu else None,
            "difficulty_level": location.difficulty_level,
            "access_type": location.access_type,
            "parking_available": location.parking_available,
            "trail_access": location.trail_access,
            "success_rate": location.success_rate
        }
        for location in locations
    ]

@router.get("/regulations")
async def get_regulations(
    category: Optional[str] = None,
    active_only: bool = True,
    db: Session = Depends(get_db)
):
    """Get hunting regulations"""
    query = db.query(Regulation)
    
    if category:
        query = query.filter(Regulation.category == category)
    if active_only:
        query = query.filter(Regulation.is_active == True)
    
    regulations = query.all()
    return [
        {
            "id": reg.id,
            "title": reg.title,
            "category": reg.category,
            "content": reg.content,
            "effective_date": reg.effective_date.isoformat() if reg.effective_date else None,
            "expiration_date": reg.expiration_date.isoformat() if reg.expiration_date else None,
            "source": reg.source
        }
        for reg in regulations
    ]

@router.post("/recommendations")
async def get_ai_recommendation(
    location: str,
    species: str,
    weather_data: dict,
    user_preferences: Optional[dict] = None,
    db: Session = Depends(get_db)
):
    """Get AI-powered hunting recommendation"""
    try:
        recommendation = await ai_service.get_hunting_recommendation(
            location=location,
            species=species,
            weather_data=weather_data,
            user_preferences=user_preferences
        )
        return recommendation
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate recommendation: {str(e)}")

@router.get("/colebrook-info")
async def get_colebrook_specific_info():
    """Get Colebrook, NH specific hunting information"""
    return {
        "location": "Colebrook, NH",
        "coordinates": {
            "latitude": 44.8942,
            "longitude": -71.4962
        },
        "nearby_wmus": ["WMU A", "WMU B", "WMU C"],
        "prime_species": [
            "White-tailed Deer",
            "Moose",
            "Black Bear",
            "Wild Turkey"
        ],
        "nearby_locations": [
            {
                "name": "Connecticut Lakes Region",
                "distance": "15 miles",
                "species": ["Moose", "Deer", "Bear"]
            },
            {
                "name": "Dixville Notch",
                "distance": "25 miles",
                "species": ["Deer", "Bear", "Turkey"]
            },
            {
                "name": "Pittsburg",
                "distance": "30 miles",
                "species": ["Moose", "Deer", "Bear"]
            }
        ],
        "local_tips": [
            "Focus on WMU A and B for moose hunting",
            "Connecticut Lakes region offers excellent deer hunting",
            "Dixville Notch is prime for bear hunting",
            "Early morning hunts are most successful in this region"
        ]
    }

@router.get("/weather-impact/{species}")
async def get_weather_impact(species: str, weather_data: dict):
    """Analyze weather impact on hunting for specific species"""
    try:
        analysis = await ai_service.analyze_weather_impact(weather_data, species)
        return analysis
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to analyze weather impact: {str(e)}")

@router.get("/species-advice/{species}")
async def get_species_advice(species: str, location: str = "Colebrook, NH"):
    """Get species-specific hunting advice"""
    try:
        advice = await ai_service.get_species_specific_advice(species, location)
        return advice
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get species advice: {str(e)}")
