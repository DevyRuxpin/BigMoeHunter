import React, { useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  TextInput,
  Alert,
  Modal,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const JournalScreen = () => {
  const [entries, setEntries] = useState([
    {
      id: 1,
      date: '2024-10-15',
      species: 'White-tailed Deer',
      location: 'Connecticut Lakes',
      weather: '45°F, Light winds',
      success: true,
      notes: 'Successful hunt at dawn. Deer came from the north ridge.',
      equipment: 'Rifle, Binoculars',
    },
    {
      id: 2,
      date: '2024-10-10',
      species: 'Moose',
      location: 'WMU A',
      weather: '38°F, Overcast',
      success: false,
      notes: 'Saw tracks but no moose. Need to try different area.',
      equipment: 'Rifle, Calls',
    },
  ]);

  const [showAddModal, setShowAddModal] = useState(false);
  const [newEntry, setNewEntry] = useState({
    species: '',
    location: '',
    weather: '',
    success: false,
    notes: '',
    equipment: '',
  });

  const speciesOptions = [
    'White-tailed Deer',
    'Moose',
    'Black Bear',
    'Wild Turkey',
    'Rabbit',
    'Squirrel',
  ];

  const locationOptions = [
    'Colebrook, NH',
    'Connecticut Lakes',
    'Dixville Notch',
    'Pittsburg',
    'WMU A',
    'WMU B',
    'WMU C',
  ];

  const addEntry = () => {
    if (!newEntry.species || !newEntry.location) {
      Alert.alert('Error', 'Please fill in species and location');
      return;
    }

    const entry = {
      id: Date.now(),
      date: new Date().toISOString().split('T')[0],
      ...newEntry,
    };

    setEntries([entry, ...entries]);
    setNewEntry({
      species: '',
      location: '',
      weather: '',
      success: false,
      notes: '',
      equipment: '',
    });
    setShowAddModal(false);
    Alert.alert('Success', 'Hunt entry added to journal!');
  };

  const deleteEntry = (id) => {
    Alert.alert(
      'Delete Entry',
      'Are you sure you want to delete this entry?',
      [
        { text: 'Cancel', style: 'cancel' },
        { text: 'Delete', style: 'destructive', onPress: () => {
          setEntries(entries.filter(entry => entry.id !== id));
        }},
      ]
    );
  };

  const getSuccessIcon = (success) => {
    return success ? 'checkmark-circle' : 'close-circle';
  };

  const getSuccessColor = (success) => {
    return success ? '#4CAF50' : '#F44336';
  };

  const renderEntry = (entry) => (
    <View key={entry.id} style={styles.entryCard}>
      <View style={styles.entryHeader}>
        <View style={styles.entryInfo}>
          <Text style={styles.entryDate}>{entry.date}</Text>
          <Text style={styles.entrySpecies}>{entry.species}</Text>
        </View>
        <View style={styles.entryActions}>
          <Ionicons 
            name={getSuccessIcon(entry.success)} 
            size={24} 
            color={getSuccessColor(entry.success)} 
          />
          <TouchableOpacity onPress={() => deleteEntry(entry.id)}>
            <Ionicons name="trash" size={20} color="#F44336" />
          </TouchableOpacity>
        </View>
      </View>
      
      <View style={styles.entryDetails}>
        <View style={styles.detailRow}>
          <Ionicons name="location" size={16} color="#666" />
          <Text style={styles.detailText}>{entry.location}</Text>
        </View>
        <View style={styles.detailRow}>
          <Ionicons name="partly-sunny" size={16} color="#666" />
          <Text style={styles.detailText}>{entry.weather}</Text>
        </View>
        <View style={styles.detailRow}>
          <Ionicons name="bag" size={16} color="#666" />
          <Text style={styles.detailText}>{entry.equipment}</Text>
        </View>
      </View>
      
      {entry.notes && (
        <View style={styles.notesContainer}>
          <Text style={styles.notesLabel}>Notes:</Text>
          <Text style={styles.notesText}>{entry.notes}</Text>
        </View>
      )}
    </View>
  );

  const renderAddModal = () => (
    <Modal
      visible={showAddModal}
      animationType="slide"
      presentationStyle="pageSheet"
    >
      <View style={styles.modalContainer}>
        <View style={styles.modalHeader}>
          <Text style={styles.modalTitle}>Add Hunt Entry</Text>
          <TouchableOpacity onPress={() => setShowAddModal(false)}>
            <Ionicons name="close" size={24} color="#666" />
          </TouchableOpacity>
        </View>
        
        <ScrollView style={styles.modalContent}>
          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Species:</Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              {speciesOptions.map((species, index) => (
                <TouchableOpacity
                  key={index}
                  style={[
                    styles.optionChip,
                    newEntry.species === species && styles.optionChipSelected
                  ]}
                  onPress={() => setNewEntry({...newEntry, species})}
                >
                  <Text style={[
                    styles.optionChipText,
                    newEntry.species === species && styles.optionChipTextSelected
                  ]}>
                    {species}
                  </Text>
                </TouchableOpacity>
              ))}
            </ScrollView>
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Location:</Text>
            <ScrollView horizontal showsHorizontalScrollIndicator={false}>
              {locationOptions.map((location, index) => (
                <TouchableOpacity
                  key={index}
                  style={[
                    styles.optionChip,
                    newEntry.location === location && styles.optionChipSelected
                  ]}
                  onPress={() => setNewEntry({...newEntry, location})}
                >
                  <Text style={[
                    styles.optionChipText,
                    newEntry.location === location && styles.optionChipTextSelected
                  ]}>
                    {location}
                  </Text>
                </TouchableOpacity>
              ))}
            </ScrollView>
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Weather:</Text>
            <TextInput
              style={styles.textInput}
              placeholder="e.g., 45°F, Light winds"
              value={newEntry.weather}
              onChangeText={(text) => setNewEntry({...newEntry, weather: text})}
            />
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Equipment Used:</Text>
            <TextInput
              style={styles.textInput}
              placeholder="e.g., Rifle, Binoculars, Calls"
              value={newEntry.equipment}
              onChangeText={(text) => setNewEntry({...newEntry, equipment: text})}
            />
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Success:</Text>
            <View style={styles.successToggle}>
              <TouchableOpacity
                style={[
                  styles.toggleButton,
                  !newEntry.success && styles.toggleButtonSelected
                ]}
                onPress={() => setNewEntry({...newEntry, success: false})}
              >
                <Text style={[
                  styles.toggleButtonText,
                  !newEntry.success && styles.toggleButtonTextSelected
                ]}>
                  No Success
                </Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[
                  styles.toggleButton,
                  newEntry.success && styles.toggleButtonSelected
                ]}
                onPress={() => setNewEntry({...newEntry, success: true})}
              >
                <Text style={[
                  styles.toggleButtonText,
                  newEntry.success && styles.toggleButtonTextSelected
                ]}>
                  Successful
                </Text>
              </TouchableOpacity>
            </View>
          </View>

          <View style={styles.inputGroup}>
            <Text style={styles.inputLabel}>Notes:</Text>
            <TextInput
              style={[styles.textInput, styles.notesInput]}
              placeholder="Add your hunting notes, observations, and tips..."
              value={newEntry.notes}
              onChangeText={(text) => setNewEntry({...newEntry, notes: text})}
              multiline
              numberOfLines={4}
            />
          </View>
        </ScrollView>
        
        <View style={styles.modalFooter}>
          <TouchableOpacity
            style={styles.cancelButton}
            onPress={() => setShowAddModal(false)}
          >
            <Text style={styles.cancelButtonText}>Cancel</Text>
          </TouchableOpacity>
          <TouchableOpacity
            style={styles.saveButton}
            onPress={addEntry}
          >
            <Text style={styles.saveButtonText}>Save Entry</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );

  return (
    <View style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Hunt Journal</Text>
        <TouchableOpacity
          style={styles.addButton}
          onPress={() => setShowAddModal(true)}
        >
          <Ionicons name="add" size={24} color="white" />
        </TouchableOpacity>
      </View>

      {/* Stats */}
      <View style={styles.statsContainer}>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>{entries.length}</Text>
          <Text style={styles.statLabel}>Total Hunts</Text>
        </View>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>
            {entries.filter(entry => entry.success).length}
          </Text>
          <Text style={styles.statLabel}>Successful</Text>
        </View>
        <View style={styles.statCard}>
          <Text style={styles.statNumber}>
            {Math.round((entries.filter(entry => entry.success).length / entries.length) * 100) || 0}%
          </Text>
          <Text style={styles.statLabel}>Success Rate</Text>
        </View>
      </View>

      {/* Entries */}
      <ScrollView style={styles.entriesContainer}>
        {entries.length === 0 ? (
          <View style={styles.emptyState}>
            <Ionicons name="book" size={64} color="#ccc" />
            <Text style={styles.emptyStateText}>No hunt entries yet</Text>
            <Text style={styles.emptyStateSubtext}>
              Tap the + button to add your first hunt entry
            </Text>
          </View>
        ) : (
          entries.map(renderEntry)
        )}
      </ScrollView>

      {renderAddModal()}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 15,
    backgroundColor: 'white',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  addButton: {
    backgroundColor: '#2E7D32',
    width: 40,
    height: 40,
    borderRadius: 20,
    alignItems: 'center',
    justifyContent: 'center',
  },
  statsContainer: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: 'white',
    marginBottom: 10,
  },
  statCard: {
    flex: 1,
    alignItems: 'center',
    padding: 10,
  },
  statNumber: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#2E7D32',
  },
  statLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 2,
  },
  entriesContainer: {
    flex: 1,
    padding: 15,
  },
  entryCard: {
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
  entryHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  entryInfo: {
    flex: 1,
  },
  entryDate: {
    fontSize: 14,
    color: '#666',
    marginBottom: 2,
  },
  entrySpecies: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
  },
  entryActions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 15,
  },
  entryDetails: {
    marginBottom: 10,
  },
  detailRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 5,
  },
  detailText: {
    fontSize: 14,
    color: '#666',
    marginLeft: 8,
  },
  notesContainer: {
    marginTop: 10,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
  },
  notesLabel: {
    fontSize: 14,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 5,
  },
  notesText: {
    fontSize: 14,
    color: '#666',
    lineHeight: 20,
  },
  emptyState: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: 40,
  },
  emptyStateText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#666',
    marginTop: 15,
  },
  emptyStateSubtext: {
    fontSize: 14,
    color: '#999',
    marginTop: 5,
    textAlign: 'center',
  },
  modalContainer: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 15,
    backgroundColor: 'white',
    borderBottomWidth: 1,
    borderBottomColor: '#e0e0e0',
  },
  modalTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
  },
  modalContent: {
    flex: 1,
    padding: 15,
  },
  inputGroup: {
    marginBottom: 20,
  },
  inputLabel: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
    marginBottom: 8,
  },
  optionChip: {
    backgroundColor: '#f0f0f0',
    paddingHorizontal: 15,
    paddingVertical: 8,
    borderRadius: 20,
    marginRight: 10,
    borderWidth: 1,
    borderColor: '#e0e0e0',
  },
  optionChipSelected: {
    backgroundColor: '#2E7D32',
    borderColor: '#2E7D32',
  },
  optionChipText: {
    fontSize: 14,
    color: '#666',
  },
  optionChipTextSelected: {
    color: 'white',
    fontWeight: 'bold',
  },
  textInput: {
    backgroundColor: 'white',
    borderWidth: 1,
    borderColor: '#e0e0e0',
    borderRadius: 10,
    padding: 15,
    fontSize: 16,
  },
  notesInput: {
    minHeight: 100,
    textAlignVertical: 'top',
  },
  successToggle: {
    flexDirection: 'row',
    backgroundColor: 'white',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#e0e0e0',
    overflow: 'hidden',
  },
  toggleButton: {
    flex: 1,
    padding: 15,
    alignItems: 'center',
  },
  toggleButtonSelected: {
    backgroundColor: '#2E7D32',
  },
  toggleButtonText: {
    fontSize: 16,
    color: '#666',
  },
  toggleButtonTextSelected: {
    color: 'white',
    fontWeight: 'bold',
  },
  modalFooter: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: 'white',
    borderTopWidth: 1,
    borderTopColor: '#e0e0e0',
  },
  cancelButton: {
    flex: 1,
    padding: 15,
    alignItems: 'center',
    backgroundColor: '#f0f0f0',
    borderRadius: 10,
    marginRight: 10,
  },
  cancelButtonText: {
    fontSize: 16,
    color: '#666',
    fontWeight: 'bold',
  },
  saveButton: {
    flex: 1,
    padding: 15,
    alignItems: 'center',
    backgroundColor: '#2E7D32',
    borderRadius: 10,
    marginLeft: 10,
  },
  saveButtonText: {
    fontSize: 16,
    color: 'white',
    fontWeight: 'bold',
  },
});

export default JournalScreen;