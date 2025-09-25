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

const SpeciesScreen = () => {
  const [selectedSpecies, setSelectedSpecies] = useState('deer');

  const species = {
    deer: {
      name: 'White-tailed Deer',
      icon: 'paw',
      color: '#8BC34A',
      season: 'Oct 1 - Dec 15',
      bagLimit: '1 per year',
      description: 'Most popular game animal in Colebrook area',
      tips: [
        'Hunt during dawn and dusk for peak activity',
        'Focus on food sources and travel corridors',
        'Look for fresh scrapes and rubs',
        'Use scent control products',
        'Consider weather impact on movement'
      ],
      habitat: 'Mixed forests, agricultural edges, apple orchards',
      equipment: 'Rifle (.270 or larger), shotgun, or bow',
    },
    moose: {
      name: 'Moose',
      icon: 'leaf',
      color: '#4CAF50',
      season: 'Oct 1 - Oct 31',
      bagLimit: '1 per lifetime (lottery)',
      description: 'Largest game animal in New Hampshire',
      tips: [
        'Focus on WMU A and B areas',
        'Look for water sources and wetlands',
        'Hunt during early morning and evening',
        'Use calls during rut season',
        'Be prepared for challenging terrain'
      ],
      habitat: 'Wetlands, mixed forests, water sources',
      equipment: 'Rifle (.30-06 or larger), binoculars',
    },
    bear: {
      name: 'Black Bear',
      icon: 'flame',
      color: '#FF9800',
      season: 'Sep 1 - Nov 15',
      bagLimit: '1 per year',
      description: 'Opportunistic omnivore with excellent senses',
      tips: [
        'Focus on Dixville Notch area',
        'Look for berry patches and food sources',
        'Use bait stations where legal',
        'Hunt during early morning and late afternoon',
        'Always carry bear spray'
      ],
      habitat: 'Dense forests, berry patches, food sources',
      equipment: 'Rifle (.30-06 or larger), bear spray',
    },
    turkey: {
      name: 'Wild Turkey',
      icon: 'egg',
      color: '#9C27B0',
      season: 'May 1 - May 31 (Spring)',
      bagLimit: '2 per season',
      description: 'Large game bird with excellent eyesight',
      tips: [
        'Use calls to attract gobblers',
        'Hunt during early morning',
        'Set up near roosting areas',
        'Use decoys for better success',
        'Be patient and still'
      ],
      habitat: 'Mixed forests, agricultural fields',
      equipment: 'Shotgun (12 or 20 gauge), calls, decoys',
    },
  };

  const renderSpeciesInfo = (speciesData) => (
    <View style={styles.speciesInfo}>
      <View style={styles.speciesHeader}>
        <View style={[styles.speciesIcon, { backgroundColor: speciesData.color }]}>
          <Ionicons name={speciesData.icon} size={30} color="white" />
        </View>
        <View style={styles.speciesTitleContainer}>
          <Text style={styles.speciesName}>{speciesData.name}</Text>
          <Text style={styles.speciesDescription}>{speciesData.description}</Text>
        </View>
      </View>

      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>📅 Season & Limits</Text>
        <Text style={styles.infoText}>Season: {speciesData.season}</Text>
        <Text style={styles.infoText}>Bag Limit: {speciesData.bagLimit}</Text>
      </View>

      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>🏠 Habitat</Text>
        <Text style={styles.infoText}>{speciesData.habitat}</Text>
      </View>

      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>🎒 Equipment</Text>
        <Text style={styles.infoText}>{speciesData.equipment}</Text>
      </View>

      <View style={styles.infoCard}>
        <Text style={styles.infoTitle}>💡 Hunting Tips</Text>
        {speciesData.tips.map((tip, index) => (
          <Text key={index} style={styles.tipText}>• {tip}</Text>
        ))}
      </View>
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Species Selector */}
      <ScrollView 
        horizontal 
        showsHorizontalScrollIndicator={false}
        style={styles.speciesSelector}
      >
        {Object.entries(species).map(([key, data]) => (
          <TouchableOpacity
            key={key}
            style={[
              styles.speciesButton,
              selectedSpecies === key && styles.speciesButtonSelected
            ]}
            onPress={() => setSelectedSpecies(key)}
          >
            <Ionicons 
              name={data.icon} 
              size={24} 
              color={selectedSpecies === key ? 'white' : data.color} 
            />
            <Text style={[
              styles.speciesButtonText,
              selectedSpecies === key && styles.speciesButtonTextSelected
            ]}>
              {data.name.split(' ')[0]}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* Species Information */}
      <ScrollView style={styles.contentContainer}>
        {renderSpeciesInfo(species[selectedSpecies])}
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  speciesSelector: {
    backgroundColor: 'white',
    paddingVertical: 15,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  speciesButton: {
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 10,
    marginHorizontal: 5,
    borderRadius: 20,
    backgroundColor: '#f0f0f0',
    minWidth: 100,
  },
  speciesButtonSelected: {
    backgroundColor: '#2E7D32',
  },
  speciesButtonText: {
    fontSize: 12,
    fontWeight: '600',
    marginTop: 5,
    textAlign: 'center',
  },
  speciesButtonTextSelected: {
    color: 'white',
  },
  contentContainer: {
    flex: 1,
    padding: 15,
  },
  speciesInfo: {
    flex: 1,
  },
  speciesHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 10,
    marginBottom: 15,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  speciesIcon: {
    width: 60,
    height: 60,
    borderRadius: 30,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 15,
  },
  speciesTitleContainer: {
    flex: 1,
  },
  speciesName: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  speciesDescription: {
    fontSize: 16,
    color: '#666',
  },
  infoCard: {
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
  infoTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  infoText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
  tipText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
});

export default SpeciesScreen;