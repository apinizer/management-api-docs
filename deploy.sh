#!/bin/bash

# MkDocs Material Deployment Script
echo "🚀 Deploying documentation to GitHub Pages..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.x"
    exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m pip install --user -r requirements.txt

# Deploy to GitHub Pages
echo "📤 Deploying to GitHub Pages..."
python3 -m mkdocs gh-deploy --force

echo "✅ Deployment complete!"
echo "🌐 Your site should be available at: https://apinizer.github.io/management-api-docs/"
echo "⏳ Please wait a few minutes for GitHub Pages to update."

