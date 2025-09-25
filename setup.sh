#!/bin/bash

# BigMoeHunter Setup Script
# Sets up the development environment for the New Hampshire hunting app

echo "🎯 Setting up BigMoeHunter - New Hampshire Hunting App"
echo "=================================================="

# Check if Python 3.11+ is installed
python_version=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1,2)
required_version="3.11"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.11+ is required. Current version: $python_version"
    echo "Please install Python 3.11 or higher"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv311
source venv311/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your API keys and configuration"
fi

# Install Node.js dependencies for mobile app
if command -v npm &> /dev/null; then
    echo "📦 Installing Node.js dependencies..."
    cd mobile
    npm install
    cd ..
else
    echo "⚠️  npm not found. Please install Node.js to develop the mobile app"
fi

# Create necessary directories
echo "📁 Creating project directories..."
mkdir -p logs
mkdir -p data/nh_fish_game
mkdir -p data/maps
mkdir -p data/regulations

# Set up database
echo "🗄️  Setting up database..."
python app/utils/seed_data.py

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start the development server:"
echo "1. Activate virtual environment: source venv311/bin/activate"
echo "2. Start the API server: python app/main.py"
echo "3. Or use Docker: docker-compose up"
echo ""
echo "API will be available at: http://localhost:8000"
echo "API documentation at: http://localhost:8000/docs"
echo ""
echo "For mobile app development:"
echo "1. cd mobile"
echo "2. npm start"
echo ""
echo "Happy hunting! 🦌"
