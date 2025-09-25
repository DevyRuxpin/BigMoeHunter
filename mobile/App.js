import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createStackNavigator } from '@react-navigation/stack';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { Ionicons } from '@expo/vector-icons';

// Import screens
import DashboardScreen from './src/screens/DashboardScreen';
import AIAssistantScreen from './src/screens/AIAssistantScreen';
import MapsScreen from './src/screens/MapsScreen';
import SpeciesScreen from './src/screens/SpeciesScreen';
import RegulationsScreen from './src/screens/RegulationsScreen';
import JournalScreen from './src/screens/JournalScreen';
import WeatherScreen from './src/screens/WeatherScreen';
import EquipmentScreen from './src/screens/EquipmentScreen';

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();

// Main Tab Navigator
function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;

          if (route.name === 'Dashboard') {
            iconName = focused ? 'home' : 'home-outline';
          } else if (route.name === 'AI Assistant') {
            iconName = focused ? 'chatbubbles' : 'chatbubbles-outline';
          } else if (route.name === 'Maps') {
            iconName = focused ? 'map' : 'map-outline';
          } else if (route.name === 'Species') {
            iconName = focused ? 'paw' : 'paw-outline';
          } else if (route.name === 'Regulations') {
            iconName = focused ? 'document-text' : 'document-text-outline';
          } else if (route.name === 'Journal') {
            iconName = focused ? 'book' : 'book-outline';
          } else if (route.name === 'Weather') {
            iconName = focused ? 'partly-sunny' : 'partly-sunny-outline';
          } else if (route.name === 'Equipment') {
            iconName = focused ? 'bag' : 'bag-outline';
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#2E7D32',
        tabBarInactiveTintColor: 'gray',
        tabBarStyle: {
          backgroundColor: '#f8f9fa',
          borderTopColor: '#e0e0e0',
          height: 60,
          paddingBottom: 5,
        },
        headerStyle: {
          backgroundColor: '#2E7D32',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      })}
    >
      <Tab.Screen 
        name="Dashboard" 
        component={DashboardScreen}
        options={{ title: 'BigMoeHunter' }}
      />
      <Tab.Screen 
        name="AI Assistant" 
        component={AIAssistantScreen}
        options={{ title: 'AI Guide' }}
      />
      <Tab.Screen 
        name="Maps" 
        component={MapsScreen}
        options={{ title: 'Hunting Maps' }}
      />
      <Tab.Screen 
        name="Species" 
        component={SpeciesScreen}
        options={{ title: 'Species Guide' }}
      />
      <Tab.Screen 
        name="Weather" 
        component={WeatherScreen}
        options={{ title: 'Weather' }}
      />
      <Tab.Screen 
        name="Equipment" 
        component={EquipmentScreen}
        options={{ title: 'Equipment' }}
      />
      <Tab.Screen 
        name="Regulations" 
        component={RegulationsScreen}
        options={{ title: 'Laws & Rules' }}
      />
      <Tab.Screen 
        name="Journal" 
        component={JournalScreen}
        options={{ title: 'Hunt Journal' }}
      />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <StatusBar style="light" />
      <Stack.Navigator>
        <Stack.Screen 
          name="Main" 
          component={MainTabs}
          options={{ headerShown: false }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f9fa',
  },
});