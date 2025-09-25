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

const RegulationsScreen = () => {
  const [selectedCategory, setSelectedCategory] = useState('seasons');

  const regulationCategories = {
    seasons: {
      title: 'Hunting Seasons',
      icon: 'calendar',
      color: '#4CAF50',
      content: [
        {
          species: 'White-tailed Deer',
          season: 'October 1 - December 15',
          bagLimit: '1 per year',
          notes: 'Archery: Sep 15 - Dec 15, Muzzleloader: Nov 2-10',
        },
        {
          species: 'Moose',
          season: 'October 1 - October 31',
          bagLimit: '1 per lifetime (lottery)',
          notes: 'WMU A & B only, lottery system',
        },
        {
          species: 'Black Bear',
          season: 'September 1 - November 15',
          bagLimit: '1 per year',
          notes: 'Baiting allowed with permit',
        },
        {
          species: 'Wild Turkey',
          season: 'May 1 - May 31 (Spring)',
          bagLimit: '2 per season',
          notes: 'Fall season: Oct 15 - Nov 15',
        },
      ],
    },
    licenses: {
      title: 'Licenses & Permits',
      icon: 'card',
      color: '#2196F3',
      content: [
        {
          type: 'Resident Hunting License',
          cost: '$26',
          duration: 'Annual',
          requirements: 'NH resident, 16+ years old',
        },
        {
          type: 'Non-Resident Hunting License',
          cost: '$103',
          duration: 'Annual',
          requirements: 'Non-NH resident, 16+ years old',
        },
        {
          type: 'Big Game Permit',
          cost: '$26',
          duration: 'Annual',
          requirements: 'Required for deer, moose, bear',
        },
        {
          type: 'Moose Lottery Application',
          cost: '$15',
          duration: 'Annual',
          requirements: 'Must apply by June 15',
        },
      ],
    },
    safety: {
      title: 'Safety Regulations',
      icon: 'shield',
      color: '#F44336',
      content: [
        {
          rule: 'Blaze Orange Requirement',
          description: 'Must wear 400 sq in during firearms season',
          penalty: 'Fine up to $1,000',
        },
        {
          rule: 'Firearm Safety',
          description: 'Treat every firearm as loaded',
          penalty: 'Criminal charges possible',
        },
        {
          rule: 'Private Property',
          description: 'Must have written permission',
          penalty: 'Trespassing charges',
        },
        {
          rule: 'Tagging Requirements',
          description: 'Must tag immediately after harvest',
          penalty: 'Fine up to $500',
        },
      ],
    },
    areas: {
      title: 'Hunting Areas',
      icon: 'map',
      color: '#FF9800',
      content: [
        {
          area: 'WMU A (Northern Zone)',
          description: 'Connecticut Lakes region',
          restrictions: 'Moose lottery only, some private land',
          access: 'Public lands available',
        },
        {
          area: 'WMU B (Central Zone)',
          description: 'Colebrook area',
          restrictions: 'Mixed public/private land',
          access: 'State forests, some private',
        },
        {
          area: 'WMU C (Southern Zone)',
          description: 'Pittsburg area',
          restrictions: 'Limited moose hunting',
          access: 'Mostly public land',
        },
        {
          area: 'Private Land',
          description: 'Various locations',
          restrictions: 'Permission required',
          access: 'Landowner permission only',
        },
      ],
    },
  };

  const emergencyContacts = [
    { name: 'NH Fish & Game', number: '(603) 271-3125', type: 'General Info' },
    { name: 'Emergency Dispatch', number: '911', type: 'Emergency' },
    { name: 'Game Warden', number: '(603) 271-3125', type: 'Violations' },
    { name: 'Wildlife Rescue', number: '(603) 271-3125', type: 'Injured Wildlife' },
  ];

  const renderRegulationContent = (category) => (
    <View style={styles.contentList}>
      {category.content.map((item, index) => (
        <View key={index} style={styles.regulationCard}>
          <View style={styles.regulationHeader}>
            <Text style={styles.regulationTitle}>
              {item.species || item.type || item.rule || item.area}
            </Text>
            {(item.season || item.cost || item.description) && (
              <Text style={styles.regulationSubtitle}>
                {item.season || item.cost || item.description}
              </Text>
            )}
          </View>
          <View style={styles.regulationDetails}>
            {item.bagLimit && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Bag Limit:</Text>
                <Text style={styles.detailValue}>{item.bagLimit}</Text>
              </View>
            )}
            {item.requirements && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Requirements:</Text>
                <Text style={styles.detailValue}>{item.requirements}</Text>
              </View>
            )}
            {item.restrictions && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Restrictions:</Text>
                <Text style={styles.detailValue}>{item.restrictions}</Text>
              </View>
            )}
            {item.access && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Access:</Text>
                <Text style={styles.detailValue}>{item.access}</Text>
              </View>
            )}
            {item.penalty && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Penalty:</Text>
                <Text style={styles.detailValue}>{item.penalty}</Text>
              </View>
            )}
            {item.notes && (
              <View style={styles.detailItem}>
                <Text style={styles.detailLabel}>Notes:</Text>
                <Text style={styles.detailValue}>{item.notes}</Text>
              </View>
            )}
          </View>
        </View>
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
        {Object.entries(regulationCategories).map(([key, category]) => (
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

      {/* Regulation Content */}
      <ScrollView style={styles.contentContainer}>
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>
            {regulationCategories[selectedCategory].title}
          </Text>
          {renderRegulationContent(regulationCategories[selectedCategory])}
        </View>

        {/* Emergency Contacts */}
        <View style={styles.section}>
          <Text style={styles.sectionTitle}>📞 Emergency Contacts</Text>
          {emergencyContacts.map((contact, index) => (
            <TouchableOpacity
              key={index}
              style={styles.contactCard}
              onPress={() => Alert.alert('Call', `Calling ${contact.name}...`)}
            >
              <View style={styles.contactHeader}>
                <Text style={styles.contactName}>{contact.name}</Text>
                <Text style={styles.contactType}>{contact.type}</Text>
              </View>
              <Text style={styles.contactNumber}>{contact.number}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Important Notes */}
        <View style={styles.notesCard}>
          <View style={styles.notesHeader}>
            <Ionicons name="information-circle" size={24} color="#2196F3" />
            <Text style={styles.notesTitle}>Important Notes</Text>
          </View>
          <Text style={styles.notesText}>
            • Always check current regulations before hunting
          </Text>
          <Text style={styles.notesText}>
            • Regulations may change annually
          </Text>
          <Text style={styles.notesText}>
            • Contact NH Fish & Game for updates
          </Text>
          <Text style={styles.notesText}>
            • Respect private property rights
          </Text>
          <Text style={styles.notesText}>
            • Practice ethical hunting
          </Text>
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
  contentList: {
    flex: 1,
  },
  regulationCard: {
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
  regulationHeader: {
    marginBottom: 10,
  },
  regulationTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  regulationSubtitle: {
    fontSize: 16,
    color: '#2E7D32',
    fontWeight: '600',
  },
  regulationDetails: {
    marginTop: 10,
  },
  detailItem: {
    flexDirection: 'row',
    marginBottom: 8,
  },
  detailLabel: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#666',
    width: 100,
  },
  detailValue: {
    fontSize: 14,
    color: '#333',
    flex: 1,
  },
  contactCard: {
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
  contactHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 5,
  },
  contactName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  contactType: {
    fontSize: 12,
    color: '#666',
    backgroundColor: '#f0f0f0',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 10,
  },
  contactNumber: {
    fontSize: 18,
    color: '#2E7D32',
    fontWeight: 'bold',
  },
  notesCard: {
    backgroundColor: '#e3f2fd',
    padding: 15,
    borderRadius: 10,
    borderLeftWidth: 4,
    borderLeftColor: '#2196F3',
  },
  notesHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  notesTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 10,
    color: '#1976D2',
  },
  notesText: {
    fontSize: 14,
    color: '#1976D2',
    marginBottom: 5,
    lineHeight: 20,
  },
});

export default RegulationsScreen;