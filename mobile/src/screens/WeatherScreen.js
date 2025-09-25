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

const WeatherScreen = () => {
  const [weatherData, setWeatherData] = useState({
    current: {
      temperature: 45,
      condition: 'Partly Cloudy',
      wind: '8 mph NW',
      humidity: '65%',
      pressure: '30.15"',
      visibility: '10 miles',
    },
    forecast: [
      { day: 'Today', high: 48, low: 32, condition: 'Partly Cloudy', wind: '8 mph NW' },
      { day: 'Tomorrow', high: 52, low: 35, condition: 'Sunny', wind: '5 mph N' },
      { day: 'Day 3', high: 46, low: 28, condition: 'Overcast', wind: '12 mph SW' },
      { day: 'Day 4', high: 41, low: 25, condition: 'Rain', wind: '15 mph SE' },
      { day: 'Day 5', high: 38, low: 22, condition: 'Snow', wind: '20 mph NE' },
    ],
  });

  const huntingConditions = [
    {
      condition: 'Temperature',
      value: '45°F',
      impact: 'Excellent',
      description: 'Ideal temperature for animal activity',
      color: '#4CAF50',
    },
    {
      condition: 'Wind',
      value: '8 mph NW',
      impact: 'Good',
      description: 'Light winds help with scent control',
      color: '#8BC34A',
    },
    {
      condition: 'Pressure',
      value: '30.15"',
      impact: 'Excellent',
      description: 'Rising pressure increases activity',
      color: '#4CAF50',
    },
    {
      condition: 'Humidity',
      value: '65%',
      impact: 'Good',
      description: 'Moderate humidity for comfort',
      color: '#8BC34A',
    },
  ];

  const weatherTips = [
    {
      title: 'Temperature Impact',
      tips: [
        '40-50°F: Peak deer activity',
        'Below 30°F: Animals seek shelter',
        'Above 60°F: Reduced daytime movement',
        'Sudden drops: Increased activity',
      ],
    },
    {
      title: 'Wind Conditions',
      tips: [
        'Light winds (5-10 mph): Perfect for hunting',
        'Strong winds (>15 mph): Animals seek cover',
        'Variable winds: Unpredictable movement',
        'Calm conditions: Use extra scent control',
      ],
    },
    {
      title: 'Pressure Changes',
      tips: [
        'Rising pressure: Increased activity',
        'Falling pressure: Animals prepare for weather',
        'Steady pressure: Normal patterns',
        'Rapid changes: Unpredictable behavior',
      ],
    },
  ];

  const refreshWeather = () => {
    Alert.alert('Weather Updated', 'Weather data refreshed successfully!');
    // In a real app, this would fetch from a weather API
  };

  return (
    <ScrollView style={styles.container}>
      {/* Current Weather */}
      <View style={styles.currentWeatherCard}>
        <View style={styles.weatherHeader}>
          <Ionicons name="partly-sunny" size={30} color="#2196F3" />
          <Text style={styles.weatherTitle}>Current Conditions</Text>
          <TouchableOpacity onPress={refreshWeather}>
            <Ionicons name="refresh" size={24} color="#2E7D32" />
          </TouchableOpacity>
        </View>
        
        <View style={styles.currentWeatherGrid}>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.temperature}°F</Text>
            <Text style={styles.weatherLabel}>Temperature</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.condition}</Text>
            <Text style={styles.weatherLabel}>Condition</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.wind}</Text>
            <Text style={styles.weatherLabel}>Wind</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.humidity}</Text>
            <Text style={styles.weatherLabel}>Humidity</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.pressure}</Text>
            <Text style={styles.weatherLabel}>Pressure</Text>
          </View>
          <View style={styles.weatherItem}>
            <Text style={styles.weatherValue}>{weatherData.current.visibility}</Text>
            <Text style={styles.weatherLabel}>Visibility</Text>
          </View>
        </View>
      </View>

      {/* Hunting Conditions */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>🎯 Hunting Conditions</Text>
        {huntingConditions.map((condition, index) => (
          <View key={index} style={styles.conditionCard}>
            <View style={styles.conditionHeader}>
              <Text style={styles.conditionName}>{condition.condition}</Text>
              <View style={[styles.impactBadge, { backgroundColor: condition.color }]}>
                <Text style={styles.impactText}>{condition.impact}</Text>
              </View>
            </View>
            <Text style={styles.conditionValue}>{condition.value}</Text>
            <Text style={styles.conditionDescription}>{condition.description}</Text>
          </View>
        ))}
      </View>

      {/* 5-Day Forecast */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>📅 5-Day Forecast</Text>
        {weatherData.forecast.map((day, index) => (
          <View key={index} style={styles.forecastCard}>
            <View style={styles.forecastHeader}>
              <Text style={styles.forecastDay}>{day.day}</Text>
              <Text style={styles.forecastCondition}>{day.condition}</Text>
            </View>
            <View style={styles.forecastTemps}>
              <Text style={styles.forecastHigh}>{day.high}°F</Text>
              <Text style={styles.forecastLow}>{day.low}°F</Text>
            </View>
            <Text style={styles.forecastWind}>{day.wind}</Text>
          </View>
        ))}
      </View>

      {/* Weather Tips */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>💡 Weather Tips</Text>
        {weatherTips.map((tip, index) => (
          <View key={index} style={styles.tipCard}>
            <Text style={styles.tipTitle}>{tip.title}</Text>
            {tip.tips.map((tipText, tipIndex) => (
              <Text key={tipIndex} style={styles.tipText}>• {tipText}</Text>
            ))}
          </View>
        ))}
      </View>

      {/* Weather Alerts */}
      <View style={styles.alertCard}>
        <View style={styles.alertHeader}>
          <Ionicons name="warning" size={24} color="#FF9800" />
          <Text style={styles.alertTitle}>Weather Alerts</Text>
        </View>
        <Text style={styles.alertText}>
          ⚠️ High winds expected Day 4-5. Consider adjusting hunting plans.
        </Text>
        <Text style={styles.alertText}>
          ❄️ Snow possible Day 5. Prepare for winter conditions.
        </Text>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
  currentWeatherCard: {
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
    justifyContent: 'space-between',
    marginBottom: 20,
  },
  weatherTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333',
    flex: 1,
    marginLeft: 10,
  },
  currentWeatherGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  weatherItem: {
    width: '30%',
    alignItems: 'center',
    marginBottom: 15,
  },
  weatherValue: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2E7D32',
  },
  weatherLabel: {
    fontSize: 12,
    color: '#666',
    marginTop: 2,
    textAlign: 'center',
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
  conditionCard: {
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
  conditionHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 5,
  },
  conditionName: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  impactBadge: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  impactText: {
    fontSize: 12,
    color: 'white',
    fontWeight: 'bold',
  },
  conditionValue: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#2E7D32',
    marginBottom: 5,
  },
  conditionDescription: {
    fontSize: 14,
    color: '#666',
  },
  forecastCard: {
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
  forecastHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  forecastDay: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
  },
  forecastCondition: {
    fontSize: 14,
    color: '#666',
  },
  forecastTemps: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 5,
  },
  forecastHigh: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#FF5722',
    marginRight: 10,
  },
  forecastLow: {
    fontSize: 16,
    color: '#2196F3',
  },
  forecastWind: {
    fontSize: 14,
    color: '#666',
  },
  tipCard: {
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
  tipTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
  },
  tipText: {
    fontSize: 14,
    color: '#666',
    marginBottom: 5,
    lineHeight: 20,
  },
  alertCard: {
    backgroundColor: '#fff3e0',
    margin: 15,
    padding: 15,
    borderRadius: 10,
    borderLeftWidth: 4,
    borderLeftColor: '#FF9800',
  },
  alertHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  alertTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    marginLeft: 10,
    color: '#E65100',
  },
  alertText: {
    fontSize: 14,
    color: '#E65100',
    marginBottom: 5,
    lineHeight: 20,
  },
});

export default WeatherScreen;
