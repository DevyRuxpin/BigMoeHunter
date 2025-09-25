"""
Data seeding script for BigMoeHunter
Populates database with New Hampshire hunting data
"""

import asyncio
from sqlalchemy.orm import Session
from app.models.database import WMU, Species, HuntingSeason, HuntingLocation, Regulation
from app.models import get_db, engine
from datetime import datetime, date

def seed_database():
    """Seed the database with initial hunting data"""
    
    # Create tables
    from app.models.database import Base
    Base.metadata.create_all(bind=engine)
    
    # Get database session
    db = next(get_db())
    
    try:
        # Seed WMUs (Wildlife Management Units)
        wmus_data = [
            {
                "wmu_code": "A",
                "name": "WMU A - Connecticut Lakes",
                "description": "Northernmost WMU, prime moose habitat",
                "area_acres": 450000,
                "coordinates": "POLYGON((-71.8 45.2, -71.2 45.2, -71.2 44.8, -71.8 44.8, -71.8 45.2))"
            },
            {
                "wmu_code": "B", 
                "name": "WMU B - Great North Woods",
                "description": "Large forested area with excellent deer and moose hunting",
                "area_acres": 380000,
                "coordinates": "POLYGON((-71.6 45.0, -71.0 45.0, -71.0 44.6, -71.6 44.6, -71.6 45.0))"
            },
            {
                "wmu_code": "C",
                "name": "WMU C - White Mountains North",
                "description": "Mountainous terrain with mixed hunting opportunities",
                "area_acres": 320000,
                "coordinates": "POLYGON((-71.4 44.8, -70.8 44.8, -70.8 44.4, -71.4 44.4, -71.4 44.8))"
            }
        ]
        
        for wmu_data in wmus_data:
            wmu = WMU(**wmu_data)
            db.add(wmu)
        
        # Seed Species
        species_data = [
            {
                "name": "White-tailed Deer",
                "scientific_name": "Odocoileus virginianus",
                "description": "Most popular big game species in New Hampshire",
                "habitat_info": "Mixed forests, agricultural areas, suburban edges",
                "behavior_patterns": "Active dawn and dusk, rut in November",
                "hunting_tips": "Use deer calls during rut, focus on food sources in fall"
            },
            {
                "name": "Moose",
                "scientific_name": "Alces alces",
                "description": "Largest member of the deer family in NH",
                "habitat_info": "Boreal forests, wetlands, young forest stands",
                "behavior_patterns": "Active early morning and evening, rut in September-October",
                "hunting_tips": "Look for fresh tracks near water sources, use moose calls during rut"
            },
            {
                "name": "Black Bear",
                "scientific_name": "Ursus americanus",
                "description": "Large omnivore found throughout NH forests",
                "habitat_info": "Dense forests, berry patches, agricultural areas",
                "behavior_patterns": "Active throughout day, hibernation in winter",
                "hunting_tips": "Focus on food sources, use bait stations where legal"
            },
            {
                "name": "Wild Turkey",
                "scientific_name": "Meleagris gallopavo",
                "description": "Large game bird with spring and fall seasons",
                "habitat_info": "Mixed forests, fields, agricultural areas",
                "behavior_patterns": "Roost in trees, feed on ground, spring gobbling",
                "hunting_tips": "Use calls near roosting areas, decoys can be effective"
            }
        ]
        
        for species_data in species_data:
            species = Species(**species_data)
            db.add(species)
        
        db.commit()
        
        # Get IDs for relationships
        wmu_a = db.query(WMU).filter(WMU.wmu_code == "A").first()
        wmu_b = db.query(WMU).filter(WMU.wmu_code == "B").first()
        wmu_c = db.query(WMU).filter(WMU.wmu_code == "C").first()
        
        deer = db.query(Species).filter(Species.name == "White-tailed Deer").first()
        moose = db.query(Species).filter(Species.name == "Moose").first()
        bear = db.query(Species).filter(Species.name == "Black Bear").first()
        turkey = db.query(Species).filter(Species.name == "Wild Turkey").first()
        
        # Seed Hunting Seasons
        seasons_data = [
            {
                "species_id": deer.id,
                "wmu_id": wmu_a.id,
                "season_name": "Archery Deer Season",
                "start_date": datetime(2024, 9, 15),
                "end_date": datetime(2024, 12, 15),
                "bag_limit": 1,
                "special_regulations": "Antlered deer only",
                "weapon_types": "Bow, Crossbow"
            },
            {
                "species_id": deer.id,
                "wmu_id": wmu_a.id,
                "season_name": "Firearms Deer Season",
                "start_date": datetime(2024, 11, 13),
                "end_date": datetime(2024, 12, 1),
                "bag_limit": 1,
                "special_regulations": "Antlered deer only",
                "weapon_types": "Rifle, Shotgun, Muzzleloader"
            },
            {
                "species_id": moose.id,
                "wmu_id": wmu_a.id,
                "season_name": "Moose Season",
                "start_date": datetime(2024, 10, 19),
                "end_date": datetime(2024, 10, 27),
                "bag_limit": 1,
                "special_regulations": "Permit required, lottery system",
                "weapon_types": "Rifle, Shotgun, Muzzleloader"
            },
            {
                "species_id": bear.id,
                "wmu_id": wmu_a.id,
                "season_name": "Bear Season",
                "start_date": datetime(2024, 9, 1),
                "end_date": datetime(2024, 11, 15),
                "bag_limit": 1,
                "special_regulations": "No cubs or sows with cubs",
                "weapon_types": "Rifle, Shotgun, Muzzleloader, Bow"
            },
            {
                "species_id": turkey.id,
                "wmu_id": wmu_a.id,
                "season_name": "Spring Turkey Season",
                "start_date": datetime(2024, 5, 1),
                "end_date": datetime(2024, 5, 31),
                "bag_limit": 2,
                "special_regulations": "Male turkeys only",
                "weapon_types": "Shotgun, Bow"
            }
        ]
        
        for season_data in seasons_data:
            season = HuntingSeason(**season_data)
            db.add(season)
        
        # Seed Hunting Locations
        locations_data = [
            {
                "name": "Connecticut Lakes Region",
                "description": "Prime moose and deer hunting area",
                "latitude": 45.0,
                "longitude": -71.5,
                "wmu_id": wmu_a.id,
                "species_id": moose.id,
                "difficulty_level": "Medium",
                "access_type": "Public",
                "parking_available": True,
                "trail_access": True,
                "success_rate": 0.35
            },
            {
                "name": "Dixville Notch",
                "description": "Excellent deer and bear hunting",
                "latitude": 44.9,
                "longitude": -71.3,
                "wmu_id": wmu_b.id,
                "species_id": deer.id,
                "difficulty_level": "Hard",
                "access_type": "Mixed",
                "parking_available": True,
                "trail_access": False,
                "success_rate": 0.28
            },
            {
                "name": "Colebrook State Forest",
                "description": "Local public hunting area",
                "latitude": 44.9,
                "longitude": -71.5,
                "wmu_id": wmu_a.id,
                "species_id": deer.id,
                "difficulty_level": "Easy",
                "access_type": "Public",
                "parking_available": True,
                "trail_access": True,
                "success_rate": 0.22
            },
            {
                "name": "Pittsburg Area",
                "description": "Remote hunting opportunities",
                "latitude": 45.1,
                "longitude": -71.2,
                "wmu_id": wmu_a.id,
                "species_id": moose.id,
                "difficulty_level": "Hard",
                "access_type": "Public",
                "parking_available": False,
                "trail_access": False,
                "success_rate": 0.40
            }
        ]
        
        for location_data in locations_data:
            location = HuntingLocation(**location_data)
            db.add(location)
        
        # Seed Regulations
        regulations_data = [
            {
                "title": "Hunting License Requirements",
                "category": "Legal",
                "content": "All hunters must possess a valid New Hampshire hunting license. Licenses are available online or at license agents.",
                "effective_date": datetime(2024, 1, 1),
                "source": "NH Fish & Game Department",
                "is_active": True
            },
            {
                "title": "Safety Requirements",
                "category": "Safety",
                "content": "Hunters must wear blaze orange during firearms deer season. Minimum 400 square inches above the waist.",
                "effective_date": datetime(2024, 1, 1),
                "source": "NH Fish & Game Department",
                "is_active": True
            },
            {
                "title": "Moose Hunting Permits",
                "category": "Legal",
                "content": "Moose hunting requires a special permit obtained through lottery. Applications typically due in May.",
                "effective_date": datetime(2024, 1, 1),
                "source": "NH Fish & Game Department",
                "is_active": True
            },
            {
                "title": "Bear Baiting Regulations",
                "category": "Legal",
                "content": "Bear baiting is legal in New Hampshire with proper permits. Bait stations must be registered.",
                "effective_date": datetime(2024, 1, 1),
                "source": "NH Fish & Game Department",
                "is_active": True
            }
        ]
        
        for reg_data in regulations_data:
            regulation = Regulation(**reg_data)
            db.add(regulation)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
