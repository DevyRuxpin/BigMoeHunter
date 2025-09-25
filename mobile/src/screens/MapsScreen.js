import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const MapsScreen = () => {
  const [selectedMap, setSelectedMap] = useState('hunting-zones');

  const mapTypes = [
    {
      id: 'hunting-zones',
      title: 'Hunting Zones',
      icon: 'map',
      description: 'WMU boundaries and hunting areas',
    },
    {
      id: 'public-lands',
      title: 'Public Lands',
      icon: 'leaf',
      description: 'State forests and public hunting areas',
    },
    {
      id: 'topography',
      title: 'Topography',
      icon: 'mountain',
      description: 'Elevation and terrain features',
    },
    {
      id: 'water-sources',
      title: 'Water Sources',
      icon: 'water',
      description: 'Lakes, rivers, and streams',
    },
  ];

  const huntingZones = [
    {
      name: 'WMU A',
      description: 'Northern Zone - Prime moose hunting',
      area: 'Connecticut Lakes Region',
      species: ['Moose', 'Deer', 'Bear'],
      color: '#4CAF50',
    },
    {
      name: 'WMU B',
      description: 'Central Zone - Mixed hunting opportunities',
      area: 'Colebrook Area',
      species: ['Deer', 'Moose', 'Turkey'],
      color: '#2196F3',
    },
    {
      name: 'WMU C',
      description: 'Southern Zone - Deer and small game',
      area: 'Pittsburg Area',
      species: ['Deer', 'Rabbit', 'Squirrel'],
      color: '#FF9800',
    },
  ];

  const publicLands = [
    {
      name: 'Connecticut Lakes State Forest',
      size: '25,000 acres',
      access: 'Public',
      features: ['Moose hunting', 'Deer hunting', 'Fishing'],
    },
    {
      name: 'Dixville Notch State Park',
      size: '1,200 acres',
      access: 'Public',
      features: ['Bear hunting', 'Hiking', 'Scenic views'],
    },
    {
      name: 'Colebrook State Forest',
      size: '8,500 acres',
      access: 'Public',
      features: ['Deer hunting', 'Turkey hunting', 'Camping'],
    },
  ];

  const renderHuntingZones = () => (
    <View style={styles.mapContent}>
      <Text style={styles.mapTitle}>Wildlife Management Units</Text>
      {huntingZones.map((zone, index) => (
        <TouchableOpacity
          key={index}
          style={[styles.zoneCard, { borderLeftColor: zone.color }]}
          onPress={() => Alert.alert(zone.name, zone.description)}
        >
          <View style={styles.zoneHeader}>
            <Text style={styles.zoneName}>{zone.name}</Text>
            <View style={[styles.zoneColor, { backgroundColor: zone.color }]} />
          </View>
          <Text style={styles.zoneDescription}>{zone.description}</Text>
          <Text style={styles.zoneArea}>📍 {zone.area}</Text>
          <View style={styles.speciesContainer}>
            {zone.species.map((species, idx) => (
              <View key={idx} style={styles.speciesTag}>
                <Text style={styles.speciesText}>{species}</Text>
              </View>
            ))}
          </View>
        </TouchableOpacity>
      ))}
    </View>
  );

  const renderPublicLands = () => (
    <View style={styles.mapContent}>
      <Text style={styles.mapTitle}>Public Hunting Areas</Text>
      {publicLands.map((land, index) => (
        <TouchableOpacity
          key={index}
          style={styles.landCard}
          onPress={() => Alert.alert(land.name, `Size: ${land.size}\nAccess: ${land.access}`)}
        >
          <View style={styles.landHeader}>
            <Text style={styles.landName}>{land.name}</Text>
            <Text style={styles.landSize}>{land.size}</Text>
          </View>
          <Text style={styles.landAccess}>🔓 {land.access} Access</Text>
          <View style={styles.featuresContainer}>
            {land.features.map((feature, idx) => (
              <View key={idx} style={styles.featureTag}>
                <Text style={styles.featureText}>{feature}</Text>
              </View>
            ))}
          </View>
        </TouchableOpacity>
      ))}
    </View>
  );

  const renderTopography = () => (
    <View style={styles.mapContent}>
      <Text style={styles.mapTitle}>Terrain Features</Text>
      <View style={styles.topographyCard}>
        <Text style={styles.topographyTitle}>Colebrook Area Elevation</Text>
        <Text style={styles.topographyText}>
          • Highest Point: 3,200 ft (Dixville Notch)
        </Text>
        <Text style={styles.topographyText}>
          • Lowest Point: 1,100 ft (Connecticut River)
        </Text>
        <Text style={styles.topographyText}>
          • Average Elevation: 1,800 ft
        </Text>
        <Text style={styles.topographyText}>
          • Terrain: Mixed forests, wetlands, mountains
        </Text>
      </View>
      
      <View style={styles.topographyCard}>
        <Text style={styles.topographyTitle}>Key Landmarks</Text>
        <Text style={styles.topographyText}>
          • Connecticut Lakes (4 lakes)
        </Text>
        <Text style={styles.topographyText}>
          • Dixville Notch (mountain pass)
        </Text>
        <Text style={styles.topographyText}>
          • Balsams Resort area
        </Text>
        <Text style={styles.topographyText}>
          • Pittsburg-Clarksville region
        </Text>
      </View>
    </View>
  );

  const renderWaterSources = () => (
    <View style={styles.mapContent}>
      <Text style={styles.mapTitle}>Water Sources</Text>
      <View style={styles.waterCard}>
        <Text style={styles.waterTitle}>Major Water Bodies</Text>
        <Text style={styles.waterText}>
          • Connecticut Lakes (First, Second, Third, Fourth)
        </Text>
        <Text style={styles.waterText}>
          • Connecticut River
        </Text>
        <Text style={styles.waterText}>
          • Indian Stream
        </Text>
        <Text style={styles.waterText}>
          • Perry Stream
        </Text>
        <Text style={styles.waterText}>
          • Magalloway River
        </Text>
      </View>
      
      <View style={styles.waterCard}>
        <Text style={styles.waterTitle}>Wildlife Attraction</Text>
        <Text style={styles.waterText}>
          • Moose frequent water sources
        </Text>
        <Text style={styles.waterText}>
          • Deer use streams as travel corridors
        </Text>
        <Text style={styles.waterText}>
          • Bear fishing areas
        </Text>
        <Text style={styles.waterText}>
          • Waterfowl migration routes
        </Text>
      </View>
    </View>
  );

  const renderMapContent = () => {
    switch (selectedMap) {
      case 'hunting-zones':
        return renderHuntingZones();
      case 'public-lands':
        return renderPublicLands();
      case 'topography':
        return renderTopography();
      case 'water-sources':
        return renderWaterSources();
      default:
        return renderHuntingZones();
    }
  };

  return (
    <View style={styles.container}>
      {/* Map Type Selector */}
      <ScrollView 
        horizontal 
        showsHorizontalScrollIndicator={false}
        style={styles.mapTypeSelector}
      >
        {mapTypes.map((mapType) => (
          <TouchableOpacity
            key={mapType.id}
            style={[
              styles.mapTypeButton,
              selectedMap === mapType.id && styles.mapTypeButtonSelected
            ]}
            onPress={() => setSelectedMap(mapType.id)}
          >
            <Ionicons 
              name={mapType.icon} 
              size={24} 
              color={selectedMap === mapType.id ? 'white' : '#2E7D32'} 
            />
            <Text style={[
              styles.mapTypeText,
              selectedMap === mapType.id && styles.mapTypeTextSelected
            ]}>
              {mapType.title}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* Map Content */}
      <ScrollView style={styles.mapContainer}>
        {renderMapContent()}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  mapTypeSelector: {
    backgroundColor: 'white',
    paddingVertical: 15,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  mapTypeButton: {
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 10,
    marginHorizontal: 5,
    borderRadius: 20,
    backgroundColor: '#f0f0f0',
    minWidth: 100,
  },
  mapTypeButtonSelected: {
    backgroundColor: '#2E7D32',
  },
  mapTypeText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#2E7D32',
    marginTop: 5,
    textAlign: 'center',
  },
  mapTypeTextSelected: {
    color: 'white',
  },
  mapContainer: {
    flex: 1,
    padding: 15,
  },
  mapContent: {
    flex: 1,
  },
  mapTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
    textAlign: 'center',
  },
  zoneCard: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    borderLeftWidth: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  zoneHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  zoneName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
  },
  zoneColor: {
    width: 20,
    height: 20,
    borderRadius: 10,
  },
  zoneDescription: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  zoneArea: {
    fontSize: 14,
    color: '#2E7D32',
    fontWeight: '600',
    marginBottom: 10,
  },
  speciesContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  speciesTag: {
    backgroundColor: '#e8f5e8',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 15,
    marginRight: 8,
    marginBottom: 5,
  },
  speciesText: {
    fontSize: 12,
    color: '#2E7D32',
    fontWeight: '600',
  },
  landCard: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  landHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  landName: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    flex: 1,
  },
  landSize: {
    fontSize: 14,
    color: '#666',
    fontWeight: '600',
  },
  landAccess: {
    fontSize: 14,
    color: '#4CAF50',
    fontWeight: '600',
    marginBottom: 10,
  },
  featuresContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  featureTag: {
    backgroundColor: '#e3f2fd',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 15,
    marginRight: 8,
    marginBottom: 5,
  },
  featureText: {
    fontSize: 12,
    color: '#1976D2',
    fontWeight: '600',
  },
  topographyCard: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  topographyTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  topographyText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
  waterCard: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  waterTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  waterText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
});

export default MapsScreen;