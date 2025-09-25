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

const EquipmentScreen = () => {
  const [selectedCategory, setSelectedCategory] = useState('essential');

  const equipmentCategories = {
    essential: {
      title: 'Essential Gear',
      icon: 'checkmark-circle',
      color: '#4CAF50',
      items: [
        { name: 'Hunting License', required: true, description: 'Valid NH hunting license' },
        { name: 'Firearm/Bow', required: true, description: 'Properly sighted and legal' },
        { name: 'Ammunition/Arrows', required: true, description: 'Appropriate for target species' },
        { name: 'Blaze Orange', required: true, description: 'Required during firearms season' },
        { name: 'First Aid Kit', required: true, description: 'Basic medical supplies' },
        { name: 'Compass/GPS', required: true, description: 'Navigation and safety' },
      ],
    },
    clothing: {
      title: 'Clothing',
      icon: 'shirt',
      color: '#2196F3',
      items: [
        { name: 'Base Layers', required: false, description: 'Moisture-wicking materials' },
        { name: 'Insulating Layers', required: false, description: 'Wool or synthetic insulation' },
        { name: 'Outer Shell', required: false, description: 'Waterproof and windproof' },
        { name: 'Hunting Boots', required: false, description: 'Waterproof and insulated' },
        { name: 'Gloves', required: false, description: 'Warm and dexterous' },
        { name: 'Hat/Balaclava', required: false, description: 'Warmth and concealment' },
      ],
    },
    accessories: {
      title: 'Accessories',
      icon: 'bag',
      color: '#FF9800',
      items: [
        { name: 'Binoculars', required: false, description: '8x42 or 10x42 recommended' },
        { name: 'Range Finder', required: false, description: 'Accurate distance measurement' },
        { name: 'Calls', required: false, description: 'Species-specific calls' },
        { name: 'Scent Control', required: false, description: 'Sprays and soaps' },
        { name: 'Game Bags', required: false, description: 'Field dressing supplies' },
        { name: 'Headlamp', required: false, description: 'Hands-free lighting' },
      ],
    },
    safety: {
      title: 'Safety Equipment',
      icon: 'shield',
      color: '#F44336',
      items: [
        { name: 'Bear Spray', required: false, description: 'For bear encounters' },
        { name: 'Emergency Whistle', required: false, description: 'Signal for help' },
        { name: 'Emergency Blanket', required: false, description: 'Hypothermia prevention' },
        { name: 'Fire Starter', required: false, description: 'Emergency warmth' },
        { name: 'Water Purification', required: false, description: 'Safe drinking water' },
        { name: 'Communication Device', required: false, description: 'Satellite phone or radio' },
      ],
    },
  };

  const weatherRecommendations = [
    {
      condition: 'Cold Weather (< 30°F)',
      recommendations: [
        'Extra insulating layers',
        'Hand warmers',
        'Insulated boots',
        'Balaclava or face mask',
        'Hot beverages',
      ],
    },
    {
      condition: 'Wet Weather',
      recommendations: [
        'Waterproof outer shell',
        'Waterproof boots',
        'Rain cover for gear',
        'Extra dry clothing',
        'Waterproof storage bags',
      ],
    },
    {
      condition: 'Windy Conditions',
      recommendations: [
        'Windproof outer layer',
        'Secure gear straps',
        'Wind-resistant shelter',
        'Extra anchoring for stands',
        'Wind direction awareness',
      ],
    },
  ];

  const renderEquipmentList = (category) => (
    <View style={styles.equipmentList}>
      {category.items.map((item, index) => (
        <TouchableOpacity
          key={index}
          style={styles.equipmentItem}
          onPress={() => Alert.alert(item.name, item.description)}
        >
          <View style={styles.equipmentHeader}>
            <View style={styles.equipmentInfo}>
              <Text style={styles.equipmentName}>{item.name}</Text>
              {item.required && (
                <View style={styles.requiredBadge}>
                  <Text style={styles.requiredText}>Required</Text>
                </View>
              )}
            </View>
            <Ionicons name="chevron-forward" size={20} color="#666" />
          </View>
          <Text style={styles.equipmentDescription}>{item.description}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );

  return (
    <View style={styles.container}>
      {/* Category Selector */}
      <ScrollView 
        horizontal 
        showsHorizontalScrollIndicator={false}
        style={styles.categorySelector}
      >
        {Object.entries(equipmentCategories).map(([key, category]) => (
          <TouchableOpacity
            key={key}
            style={[
              styles.categoryButton,
              selectedCategory === key && styles.categoryButtonSelected
            ]}
            onPress={() => setSelectedCategory(key)}
          >
            <Ionicons 
              name={category.icon} 
              size={24} 
              color={selectedCategory === key ? 'white' : category.color} 
            />
            <Text style={[
              styles.categoryButtonText,
              selectedCategory === key && styles.categoryButtonTextSelected
            ]}>
              {category.title}
            </Text>
          </TouchableOpacity>
        ))}
      </ScrollView>

      {/* Equipment Content */}
      <ScrollView style={styles.contentContainer}>
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>
            {equipmentCategories[selectedCategory].title}
          </Text>
          {renderEquipmentList(equipmentCategories[selectedCategory])}
        </View>

        {/* Weather Recommendations */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>🌤️ Weather-Specific Gear</Text>
          {weatherRecommendations.map((weather, index) => (
            <View key={index} style={styles.weatherCard}>
              <Text style={styles.weatherTitle}>{weather.condition}</Text>
              {weather.recommendations.map((rec, recIndex) => (
                <Text key={recIndex} style={styles.weatherRecommendation}>
                  • {rec}
                </Text>
              ))}
            </View>
          ))}
        </View>

        {/* Packing Checklist */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>📋 Pre-Hunt Checklist</Text>
          <View style={styles.checklistCard}>
            <Text style={styles.checklistTitle}>Before You Go:</Text>
            <Text style={styles.checklistItem}>✓ Check weather forecast</Text>
            <Text style={styles.checklistItem}>✓ Verify hunting license</Text>
            <Text style={styles.checklistItem}>✓ Test firearm/bow</Text>
            <Text style={styles.checklistItem}>✓ Pack emergency supplies</Text>
            <Text style={styles.checklistItem}>✓ Inform someone of your plans</Text>
            <Text style={styles.checklistItem}>✓ Check equipment condition</Text>
            <Text style={styles.checklistItem}>✓ Review safety protocols</Text>
          </View>
        </View>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  categorySelector: {
    backgroundColor: 'white',
    paddingVertical: 15,
    paddingHorizontal: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  categoryButton: {
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 10,
    marginHorizontal: 5,
    borderRadius: 20,
    backgroundColor: '#f0f0f0',
    minWidth: 120,
  },
  categoryButtonSelected: {
    backgroundColor: '#2E7D32',
  },
  categoryButtonText: {
    fontSize: 12,
    fontWeight: '600',
    marginTop: 5,
    textAlign: 'center',
  },
  categoryButtonTextSelected: {
    color: 'white',
  },
  contentContainer: {
    flex: 1,
    padding: 15,
  },
  section: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
  },
  equipmentList: {
    flex: 1,
  },
  equipmentItem: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
    elevation: 2,
  },
  equipmentHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 5,
  },
  equipmentInfo: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
  },
  equipmentName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    flex: 1,
  },
  requiredBadge: {
    backgroundColor: '#F44336',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 10,
    marginLeft: 10,
  },
  requiredText: {
    fontSize: 10,
    color: 'white',
    fontWeight: 'bold',
  },
  equipmentDescription: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  weatherCard: {
    backgroundColor: 'white',
    padding: 15,
    borderRadius: 10,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
    elevation: 2,
  },
  weatherTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  weatherRecommendation: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
  checklistCard: {
    backgroundColor: '#e8f5e8',
    padding: 15,
    borderRadius: 10,
    borderLeftWidth: 4,
    borderLeftColor: '#4CAF50',
  },
  checklistTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 10,
  },
  checklistItem: {
    fontSize: 14,
    color: '#2E7D32',
    marginBottom: 5,
    lineHeight: 20,
  },
});

export default EquipmentScreen;
