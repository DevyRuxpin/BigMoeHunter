import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
  RefreshControl,
} from 'react-native';
import { Ionicons } from '@expo/vector-icons';

const DashboardScreen = () => {
  const [refreshing, setRefreshing] = useState(false);
  const [weatherData, setWeatherData] = useState({
    temperature: 45,
    condition: 'Partly Cloudy',
    wind: '8 mph NW',
    humidity: '65%',
  });

  const onRefresh = () => {
    setRefreshing(true);
    // Simulate weather update
    setTimeout(() => {
      setWeatherData({
        temperature: Math.floor(Math.random() * 20) + 35,
        condition: ['Partly Cloudy', 'Sunny', 'Overcast'][Math.floor(Math.random() * 3)],
        wind: `${Math.floor(Math.random() * 15) + 5} mph ${['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW'][Math.floor(Math.random() * 8)]}`,
        humidity: `${Math.floor(Math.random() * 30) + 50}%`,
      });
      setRefreshing(false);
    }, 1000);
  };

  const quickActions = [
    {
      title: 'Deer Hunting Tips',
      icon: 'paw',
      color: '#8BC34A',
      action: () => Alert.alert('Deer Tips', 'Best times: Dawn and dusk. Focus on food sources and travel corridors.'),
    },
    {
      title: 'Moose in WMU A',
      icon: 'leaf',
      color: '#4CAF50',
      action: () => Alert.alert('Moose Tips', 'Focus on Connecticut Lakes region. Look for water sources and wetlands.'),
    },
    {
      title: 'Bear Hunting',
      icon: 'flame',
      color: '#FF9800',
      action: () => Alert.alert('Bear Tips', 'Dixville Notch area. Use bait stations where legal. Always carry bear spray.'),
    },
    {
      title: 'Weather Impact',
      icon: 'partly-sunny',
      color: '#2196F3',
      action: () => Alert.alert('Weather', 'Current conditions are excellent for hunting. Light winds help with scent control.'),
    },
  ];

  const recentActivity = [
    { type: 'AI Query', description: 'Asked about deer hunting in Colebrook', time: '2 hours ago' },
    { type: 'Weather Check', description: 'Checked conditions for WMU A', time: '4 hours ago' },
    { type: 'Journal Entry', description: 'Logged successful moose hunt', time: '1 day ago' },
  ];

  return (
    <ScrollView 
      style={styles.container}
      refreshControl={
        <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
      }
    >
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.title}>🦌 BigMoeHunter</Text>
        <Text style={styles.subtitle}>AI-Powered Hunting Assistant</Text>
        <Text style={styles.location}>📍 Colebrook, NH</Text>
      </View>

      {/* Weather Card */}
      <View style={styles.weatherCard}>
        <View style={styles.weatherHeader}>
          <Ionicons name="partly-sunny" size={24} color="#2196F3" />
          <Text style={styles.weatherTitle}>Current Conditions</Text>
        </View>
        <View style={styles.weatherGrid}>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.temperature}°F</Text>
            <Text style={styles.weatherLabel}>Temperature</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.condition}</Text>
            <Text style={styles.weatherLabel}>Condition</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.wind}</Text>
            <Text style={styles.weatherLabel}>Wind</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.humidity}</Text>
            <Text style={styles.weatherLabel}>Humidity</Text>
          </View>
        </View>
      </View>

      {/* Quick Actions */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>⚡ Quick Actions</Text>
        <View style={styles.quickActionsGrid}>
          {quickActions.map((action, index) => (
            <TouchableOpacity
              key={index}
              style={[styles.quickAction, { backgroundColor: action.color }]}
              onPress={action.action}
            >
              <Ionicons name={action.icon} size={24} color="white" />
              <Text style={styles.quickActionText}>{action.title}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>

      {/* Recent Activity */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>📊 Recent Activity</Text>
        {recentActivity.map((activity, index) => (
          <View key={index} style={styles.activityItem}>
            <View style={styles.activityIcon}>
              <Ionicons 
                name={activity.type === 'AI Query' ? 'chatbubbles' : 
                      activity.type === 'Weather Check' ? 'partly-sunny' : 'book'} 
                size={20} 
                color="#2E7D32" 
              />
            </View>
            <View style={styles.activityContent}>
              <Text style={styles.activityType}>{activity.type}</Text>
              <Text style={styles.activityDescription}>{activity.description}</Text>
              <Text style={styles.activityTime}>{activity.time}</Text>
            </View>
          </View>
        ))}
      </View>

      {/* AI Status */}
      <View style={styles.aiStatusCard}>
        <View style={styles.aiStatusHeader}>
          <Ionicons name="chatbubbles" size={24} color="#4CAF50" />
          <Text style={styles.aiStatusTitle}>AI Assistant Status</Text>
        </View>
        <Text style={styles.aiStatusText}>🤖 Llama 3.1 8B - Online</Text>
        <Text style={styles.aiStatusText}>🆓 Completely Free - No API Keys</Text>
        <Text style={styles.aiStatusText}>🎯 Specialized for Colebrook, NH</Text>
        <Text style={styles.aiStatusText}>⚡ 95% Confidence Level</Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  header: {
    backgroundColor: '#2E7D32',
    padding: 20,
    alignItems: 'center',
  },
  title: {
    fontSize: 28,
    fontWeight: 'bold',
    color: 'white',
    marginBottom: 5,
  },
  subtitle: {
    fontSize: 16,
    color: 'white',
    opacity: 0.9,
  },
  location: {
    fontSize: 14,
    color: 'white',
    opacity: 0.8,
    marginTop: 5,
  },
  weatherCard: {
    backgroundColor: 'white',
    margin: 15,
    padding: 20,
    borderRadius: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 3,
  },
  weatherHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 15,
  },
  weatherTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 10,
    color: '#333',
  },
  weatherGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  weatherItem: {
    width: '48%',
    alignItems: 'center',
    marginBottom: 15,
  },
  weatherValue: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#2E7D32',
  },
  weatherLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 2,
  },
  section: {
    margin: 15,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
  },
  quickActionsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  quickAction: {
    width: '48%',
    padding: 15,
    borderRadius: 10,
    alignItems: 'center',
    marginBottom: 10,
  },
  quickActionText: {
    color: 'white',
    fontWeight: 'bold',
    marginTop: 5,
    textAlign: 'center',
  },
  activityItem: {
    flexDirection: 'row',
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
  activityIcon: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#f0f0f0',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 15,
  },
  activityContent: {
    flex: 1,
  },
  activityType: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  activityDescription: {
    fontSize: 14,
    color: '#666',
    marginTop: 2,
  },
  activityTime: {
    fontSize: 12,
    color: '#999',
    marginTop: 2,
  },
  aiStatusCard: {
    backgroundColor: '#e8f5e8',
    margin: 15,
    padding: 20,
    borderRadius: 12,
    borderLeftWidth: 4,
    borderLeftColor: '#4CAF50',
  },
  aiStatusHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  aiStatusTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 10,
    color: '#2E7D32',
  },
  aiStatusText: {
    fontSize: 14,
    color: '#2E7D32',
    marginBottom: 5,
  },
});

export default DashboardScreen;