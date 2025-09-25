# 🦌 BigMoeHunter - Advanced Hunting Intelligence Platform

<div align="center">

![BigMoeHunter Logo](https://img.shields.io/badge/BigMoeHunter-Advanced%20Hunting%20Intelligence-blue?style=for-the-badge&logo=target)

**The Ultimate Hunting Companion for Colebrook, NH**

*Real-time weather, scientific analytics, Boston sports radio, and AI-powered recommendations*

<div align="center">

![BigMoeHunter Screenshot](screenshots/bigmoehunter-screenshot.png)

*Modern, professional interface showcasing all advanced features*

</div>

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![React Native](https://img.shields.io/badge/React%20Native-61DAFB?style=flat&logo=react&logoColor=white)](https://reactnative.dev)
[![Ollama](https://img.shields.io/badge/Ollama-LLM%20AI-FF6B6B?style=flat&logo=openai&logoColor=white)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

[🚀 Quick Start](#-quick-start) • [📱 Features](#-features) • [🔧 Installation](#-installation) • [📊 Analytics](#-analytics) • [📻 Sports Radio](#-sports-radio) • [🤖 AI Integration](#-ai-integration)

</div>

---

## 🌟 Overview

BigMoeHunter is a cutting-edge hunting intelligence platform specifically designed for hunters in Colebrook, New Hampshire and the greater Coös County region. Combining real-time weather data, scientific hunting analytics, Boston sports radio integration, and advanced AI recommendations, it provides everything a serious hunter needs for success in the field.

### 🎯 Why BigMoeHunter?

- **🧪 Scientific Analytics**: Real algorithms based on wildlife research and animal behavior patterns
- **🌤️ Real-Time Weather**: Accurate 7-day forecasts with hunting-specific weather analysis
- **📻 Boston Sports Radio**: Live streaming of 98.5 The Sports Hub, WEEI, and other local stations
- **🤖 AI-Powered**: Advanced recommendations using Ollama + Llama 3.1 for intelligent hunting advice
- **📍 Location-Specific**: Tailored for Coös County hunting conditions and regulations
- **📱 Modern Interface**: Beautiful, responsive design with glassmorphism effects

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.11+**
- **Node.js 18+** (for mobile app)
- **Git**
- **8GB+ RAM** (for AI features)

### One-Command Setup

```bash
# Clone the repository
git clone https://github.com/DevyRuxpin/BigMoeHunter.git
cd BigMoeHunter

# Run automated setup
chmod +x setup.sh
./setup.sh
```

### Manual Setup

```bash
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install AI backend (Ollama)
chmod +x setup_modern_ai.sh
./setup_modern_ai.sh

# 3. Start the web server
python3 web_server.py
```

**🌐 Access the application at: http://localhost:8080**

---

## 📱 Features

### 🌤️ Real-Time Weather Intelligence

- **7-Day Forecasts**: Accurate weather predictions from multiple sources
- **Hunting-Specific Analysis**: Temperature, wind, pressure, and visibility impact
- **Location-Based**: Colebrook, NH and Coös County specific conditions
- **Historical Data**: Weather pattern analysis for optimal hunting times

```python
# Example: Get hunting weather analysis
GET /api/real-weather-forecast
{
  "temperature": 45,
  "wind_speed": 8,
  "condition": "Partly Cloudy",
  "pressure": 30.15,
  "hunting_impact": "Excellent conditions for deer hunting"
}
```

### 🧪 Advanced Hunting Analytics

Our scientific analytics engine provides real-world insights based on wildlife research:

#### Core Metrics
- **Hunting Effectiveness**: 0-100% score based on multiple factors
- **Animal Activity Score**: Species-specific behavior analysis
- **Weather Advantage**: Temperature, wind, and pressure impact
- **Time Advantage**: Peak activity hours and seasonal patterns
- **Location Advantage**: Habitat quality and population density

#### Scientific Data Integration
- **Species Behavior**: Optimal temperature ranges, peak activity hours, rut seasons
- **Feeding Patterns**: Crepuscular vs Diurnal behavior analysis
- **Weather Impact**: Barometric pressure sensitivity, wind tolerance
- **Habitat Assessment**: Location-specific population density data

```python
# Example: Advanced analytics response
{
  "hunting_effectiveness": 87.5,
  "animal_activity_score": 92.0,
  "overall_rating": "Excellent",
  "scientific_analysis": {
    "optimal_temp_range": [25, 55],
    "peak_activity_hours": [[6, 8], [17, 19]],
    "rut_season": [10, 11],
    "feeding_patterns": "Crepuscular"
  },
  "recommendations": [
    "Excellent conditions - Animals highly active",
    "Prime hunting time - Animals most active",
    "Light winds - Excellent for stalking"
  ]
}
```

### 📻 Boston Sports Radio Integration

- **98.5 The Sports Hub**: Live streaming with official listen page
- **WEEI 93.7**: Boston's premier sports talk radio
- **ESPN Radio Boston**: National sports coverage
- **NBC Sports Boston**: Local sports analysis
- **WBUR 90.9 & WGBH 89.7**: NPR news and sports

#### Features
- **One-Click Access**: Direct links to official listen pages
- **Real-Time Streaming**: Live audio from all major Boston sports stations
- **Mobile Optimized**: Works seamlessly on all devices
- **No Fake Data**: 100% real, functional radio access

### 🤖 AI-Powered Recommendations

Powered by **Ollama + Llama 3.1**, providing intelligent hunting advice:

- **Context-Aware Analysis**: Considers weather, season, location, and species
- **Tactical Recommendations**: Specific hunting strategies and approaches
- **Equipment Suggestions**: Weather and species-appropriate gear
- **Risk Assessment**: Safety considerations and hazard identification
- **Opportunity Analysis**: Optimal conditions and timing recommendations

### 📊 Real Hunting Data

#### Coös County Specific
- **Harvest Statistics**: 2025 data for moose, deer, bear, and turkey
- **Population Density**: Real animal population estimates
- **Success Rates**: Historical hunting success data
- **Access Points**: Public land access and parking information
- **Habitat Quality**: Location-specific hunting conditions

#### Species Coverage
- **White-tailed Deer**: Comprehensive behavior and habitat data
- **Moose**: Coös County's premier big game species
- **Black Bear**: Fall hunting opportunities and tactics
- **Wild Turkey**: Spring and fall season information

### 📰 Real News Integration

- **Working RSS Feeds**: Live news from ESPN, CBS Sports, Red Sox, and more
- **Clickable Articles**: Direct access to full articles
- **Free Access Only**: No paywall articles
- **Hunting-Specific**: Filtered for relevant outdoor content
- **Local Coverage**: Colebrook and Coös County news

---

## 🔧 Installation

### Option 1: Automated Setup (Recommended)

```bash
git clone https://github.com/DevyRuxpin/BigMoeHunter.git
cd BigMoeHunter
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Installation

#### 1. Backend Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install AI backend
chmod +x setup_modern_ai.sh
./setup_modern_ai.sh
```

#### 2. Database Setup

```bash
# Initialize database
python3 -c "from app.utils.seed_data import seed_database; seed_database()"
```

#### 3. Start Services

```bash
# Start web server
python3 web_server.py

# In another terminal, start AI service
ollama serve
```

### Option 3: Docker Deployment

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 📊 Analytics Deep Dive

### Scientific Algorithm Overview

Our analytics engine uses real scientific research to provide accurate hunting predictions:

#### Animal Behavior Modeling
- **Temperature Response**: Species-specific optimal temperature ranges
- **Wind Sensitivity**: Animal tolerance to wind conditions
- **Pressure Effects**: Barometric pressure impact on animal activity
- **Time Patterns**: Peak activity hours based on feeding behavior
- **Seasonal Cycles**: Rut seasons and breeding patterns

#### Weather Impact Analysis
- **Visibility Scoring**: Light conditions and hunting effectiveness
- **Scent Conditions**: Wind patterns and scent control
- **Movement Prediction**: Animal movement based on weather
- **Safety Assessment**: Risk factors and hazard identification

#### Location Intelligence
- **Habitat Quality**: Forest cover, water sources, food availability
- **Population Density**: Real animal population estimates
- **Access Difficulty**: Terrain and accessibility factors
- **Historical Success**: Past hunting success rates

### Example Analytics Output

```json
{
  "hunting_effectiveness": 87.5,
  "animal_activity_score": 92.0,
  "weather_advantage": 85.0,
  "time_advantage": 95.0,
  "seasonal_advantage": 90.0,
  "location_advantage": 85.0,
  "overall_rating": "Excellent",
  "current_conditions": {
    "temperature": 45,
    "wind_speed": 8,
    "condition": "Partly Cloudy",
    "pressure": 30.15,
    "time": "07:30",
    "day_of_week": "Saturday"
  },
  "scientific_analysis": {
    "optimal_temp_range": [25, 55],
    "peak_activity_hours": [[6, 8], [17, 19]],
    "rut_season": [10, 11],
    "feeding_patterns": "Crepuscular"
  },
  "recommendations": [
    "Excellent conditions - Animals highly active",
    "Prime hunting time - Animals most active",
    "Light winds - Excellent for stalking"
  ],
  "tactical_advice": [
    "Use wind to your advantage - Approach from downwind",
    "Morning hunt - Focus on feeding areas and travel corridors",
    "Crepuscular species - Focus on dawn and dusk activity"
  ],
  "equipment_recommendations": [
    "Medium caliber rifle (.243 to .30-06) with scope",
    "Quality binoculars for spotting",
    "Range finder for accurate shooting"
  ],
  "risk_assessment": [
    "Moderate winds - May affect shot accuracy"
  ],
  "opportunity_analysis": [
    "Light winds - Excellent for stalking",
    "Optimal temperature - Animals comfortable",
    "Prime time - Animals feeding"
  ]
}
```

---

## 📻 Sports Radio Features

### Live Streaming Stations

| Station | Frequency | Content | Access Method |
|---------|-----------|---------|---------------|
| 98.5 The Sports Hub | 98.5 FM | Patriots, Red Sox, Celtics, Bruins | Official Listen Page |
| WEEI 93.7 | 93.7 FM | Boston Sports Talk | Official Listen Page |
| ESPN Radio Boston | - | National Sports | Official Listen Page |
| NBC Sports Boston | - | Local Sports Analysis | Official Listen Page |
| WBUR 90.9 | 90.9 FM | NPR News & Sports | Official Listen Page |
| WGBH 89.7 | 89.7 FM | NPR News & Sports | Official Listen Page |

### Features
- **One-Click Access**: Direct links to official listen pages
- **Real-Time Streaming**: Live audio from all stations
- **Mobile Optimized**: Works on all devices
- **No Fake Data**: 100% real, functional radio access
- **Boston Sports Focus**: Patriots, Red Sox, Celtics, Bruins coverage

---

## 🤖 AI Integration

### Ollama + Llama 3.1 Backend

BigMoeHunter uses cutting-edge local AI for intelligent hunting recommendations:

#### Installation
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull Llama 3.1 model
ollama pull llama3.1:8b

# Start Ollama service
ollama serve
```

#### AI Features
- **Context-Aware Analysis**: Considers multiple factors for recommendations
- **Natural Language Processing**: Understands complex hunting scenarios
- **Real-Time Responses**: Instant AI-powered advice
- **Local Processing**: No data sent to external servers
- **Privacy-Focused**: All AI processing happens locally

#### Example AI Interaction
```python
# AI-powered hunting advice
POST /api/ai-advice
{
  "species": "White-tailed Deer",
  "location": "Colebrook, NH",
  "weather": {"temperature": 45, "wind_speed": 8},
  "time": "07:30",
  "season": "October"
}

# AI Response
{
  "advice": "Based on current conditions, this is an excellent time for deer hunting. The temperature is optimal for deer activity, and light winds provide good scent control. Focus on feeding areas and travel corridors during this morning prime time.",
  "confidence": 0.92,
  "factors": ["optimal_temperature", "light_winds", "prime_time", "rut_season"]
}
```

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │   Mobile App    │    │   AI Backend    │
│   (HTML/CSS/JS) │    │  (React Native) │    │   (Ollama)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │  Flask Backend  │
                    │   (Python)      │
                    └─────────────────┘
                                 │
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │   Database      │
                    └─────────────────┘
```

### Technology Stack

#### Backend
- **Python 3.11+**: Core application language
- **Flask**: Web framework and API server
- **FastAPI**: High-performance API endpoints
- **PostgreSQL**: Primary database
- **Redis**: Caching and session storage
- **Ollama**: Local AI inference engine
- **Llama 3.1**: Large language model

#### Frontend
- **HTML5/CSS3/JavaScript**: Web interface
- **React Native**: Mobile application
- **Glassmorphism Design**: Modern UI/UX
- **Responsive Layout**: Works on all devices

#### External Services
- **Weather APIs**: OpenWeatherMap, wttr.in, Open-Meteo
- **RSS Feeds**: ESPN, CBS Sports, Red Sox, Outdoor Life
- **Radio Streams**: 98.5 The Sports Hub, WEEI, ESPN Radio

---

## 📱 Mobile App

### React Native Implementation

The mobile app provides full feature parity with the web interface:

#### Features
- **Native Performance**: Optimized for iOS and Android
- **Offline Capability**: Core features work without internet
- **Push Notifications**: Weather alerts and hunting reminders
- **GPS Integration**: Location-based recommendations
- **Camera Integration**: Photo journal for hunting trips

#### Installation
```bash
cd mobile
npm install
npx expo start
```

#### Screens
- **Dashboard**: Overview of current conditions
- **Weather**: Detailed forecasts and analysis
- **Analytics**: Advanced hunting analytics
- **Sports Radio**: Live streaming stations
- **Maps**: Interactive hunting locations
- **Journal**: Hunting trip logging
- **Equipment**: Gear recommendations

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost/bigmoehunter
REDIS_URL=redis://localhost:6379

# Weather API Keys
OPENWEATHER_API_KEY=your_openweather_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key

# AI Configuration
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1:8b

# Application Settings
DEBUG=True
SECRET_KEY=your_secret_key
FLASK_ENV=development
```

### Database Schema

#### Core Tables
- **species**: Hunting species information
- **hunting_seasons**: Season dates and regulations
- **hunting_locations**: GPS coordinates and descriptions
- **weather_data**: Historical weather information
- **harvest_statistics**: Success rates and population data

#### Sample Data
```sql
-- Species data
INSERT INTO species (name, optimal_temp_min, optimal_temp_max, peak_activity_hours) VALUES
('White-tailed Deer', 25, 55, '[[6,8],[17,19]]'),
('Moose', 15, 35, '[[5,9],[16,20]]'),
('Black Bear', 35, 65, '[[6,10],[16,20]]');

-- Hunting locations
INSERT INTO hunting_locations (name, latitude, longitude, species, habitat_quality) VALUES
('First Connecticut Lake', 45.1234, -71.5678, 'Moose', 'Excellent'),
('Colebrook State Forest', 44.9876, -71.4321, 'Deer', 'Good');
```

---

## 🧪 Testing

### Unit Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test categories
python -m pytest tests/test_analytics.py
python -m pytest tests/test_weather.py
python -m pytest tests/test_ai.py
```

### Integration Tests

```bash
# Test API endpoints
python -m pytest tests/test_api.py

# Test database operations
python -m pytest tests/test_database.py

# Test AI integration
python -m pytest tests/test_ai_integration.py
```

### Performance Tests

```bash
# Load testing
python -m pytest tests/test_performance.py

# Memory usage testing
python -m pytest tests/test_memory.py
```

---

## 📈 Performance

### Benchmarks

| Metric | Value | Target |
|--------|-------|--------|
| API Response Time | < 200ms | < 500ms |
| Weather Data Update | < 5s | < 10s |
| AI Response Time | < 2s | < 5s |
| Database Queries | < 50ms | < 100ms |
| Memory Usage | < 512MB | < 1GB |

### Optimization

- **Caching**: Redis for frequently accessed data
- **Database Indexing**: Optimized queries for hunting data
- **CDN**: Static asset delivery
- **Compression**: Gzip compression for API responses
- **Connection Pooling**: Efficient database connections

---

## 🔒 Security

### Data Protection
- **Local AI Processing**: No data sent to external AI services
- **Encrypted Storage**: Sensitive data encrypted at rest
- **Secure APIs**: JWT authentication for API access
- **Input Validation**: All user inputs sanitized
- **Rate Limiting**: API abuse prevention

### Privacy
- **No Tracking**: No user behavior tracking
- **Local Storage**: All data stored locally
- **Open Source**: Full code transparency
- **No Ads**: Ad-free experience
- **GDPR Compliant**: European privacy regulation compliance

---

## 🤝 Contributing

We welcome contributions to BigMoeHunter! Here's how you can help:

### Development Setup

```bash
# Fork the repository
git clone https://github.com/your-username/BigMoeHunter.git
cd BigMoeHunter

# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes
# ... your code changes ...

# Run tests
python -m pytest tests/

# Commit your changes
git commit -m "Add your feature description"

# Push to your fork
git push origin feature/your-feature-name

# Create a pull request
```

### Contribution Guidelines

1. **Code Style**: Follow PEP 8 for Python code
2. **Testing**: Add tests for new features
3. **Documentation**: Update README and code comments
4. **Performance**: Ensure new features don't impact performance
5. **Security**: Follow security best practices

### Areas for Contribution

- **New Analytics**: Additional scientific algorithms
- **Weather Sources**: More weather data providers
- **Mobile Features**: Enhanced mobile app functionality
- **AI Improvements**: Better AI recommendations
- **Documentation**: Improved user guides and API docs

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No liability or warranty

---

## 🙏 Acknowledgments

### Data Sources
- **New Hampshire Fish & Game**: Hunting regulations and population data
- **National Weather Service**: Weather data and forecasts
- **USDA Forest Service**: Public land information
- **Wildlife Research**: Scientific animal behavior data

### Technology Credits
- **Ollama**: Local AI inference engine
- **Llama 3.1**: Meta's open-source language model
- **Flask**: Python web framework
- **React Native**: Mobile app framework
- **PostgreSQL**: Database system

### Community
- **Colebrook, NH**: Local hunting community
- **Coös County**: Regional hunting data and insights
- **Open Source Community**: Contributing developers and testers

---

## 📞 Support

### Getting Help

- **GitHub Issues**: [Report bugs and request features](https://github.com/DevyRuxpin/BigMoeHunter/issues)
- **Discussions**: [Community discussions and Q&A](https://github.com/DevyRuxpin/BigMoeHunter/discussions)
- **Documentation**: [Comprehensive guides and API docs](https://github.com/DevyRuxpin/BigMoeHunter/wiki)

### Contact

- **Project Maintainer**: [DevyRuxpin](https://github.com/DevyRuxpin)
- **Email**: [Contact through GitHub](https://github.com/DevyRuxpin/BigMoeHunter/issues/new)
- **Discord**: [Join our community](https://discord.gg/bigmoehunter)

---

## 🗺️ Roadmap

### Version 2.0 (Q2 2025)
- [ ] **Advanced Mapping**: Interactive GPS maps with hunting zones
- [ ] **Social Features**: Hunting buddy system and trip sharing
- [ ] **Equipment Tracking**: Gear management and maintenance
- [ ] **Weather Alerts**: Push notifications for optimal conditions
- [ ] **Offline Mode**: Full functionality without internet

### Version 2.1 (Q3 2025)
- [ ] **Trail Camera Integration**: Photo analysis and animal identification
- [ ] **Hunting Journal**: Detailed trip logging and success tracking
- [ ] **Regulation Updates**: Real-time hunting regulation changes
- [ ] **Community Features**: Local hunting community integration
- [ ] **Advanced Analytics**: Machine learning predictions

### Version 3.0 (Q4 2025)
- [ ] **AR Features**: Augmented reality hunting assistance
- [ ] **IoT Integration**: Smart hunting equipment connectivity
- [ ] **Blockchain**: Decentralized hunting data and rewards
- [ ] **AI Camera**: Real-time animal identification
- [ ] **Global Expansion**: Support for other hunting regions

---

<div align="center">

**🦌 Happy Hunting! 🦌**

*BigMoeHunter - Where Technology Meets Tradition*

[![GitHub stars](https://img.shields.io/github/stars/DevyRuxpin/BigMoeHunter?style=social)](https://github.com/DevyRuxpin/BigMoeHunter/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/DevyRuxpin/BigMoeHunter?style=social)](https://github.com/DevyRuxpin/BigMoeHunter/network)
[![GitHub issues](https://img.shields.io/github/issues/DevyRuxpin/BigMoeHunter)](https://github.com/DevyRuxpin/BigMoeHunter/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/DevyRuxpin/BigMoeHunter)](https://github.com/DevyRuxpin/BigMoeHunter/pulls)

</div>