#!/usr/bin/env python3
"""
Local News Integration Service for BigMoeHunter
Integrates local New Hampshire newspapers and news sources
"""

import requests
import json
import feedparser
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time

class LocalNewsService:
    """Service for integrating local news into BigMoeHunter"""
    
    def __init__(self):
        self.news_sources = self._initialize_news_sources()
        self.cache = {}
        self.cache_duration = 3600  # 1 hour cache
    
    def _initialize_news_sources(self) -> Dict:
        """Initialize local news sources for Colebrook, NH area"""
        return {
            "local_newspapers": {
                "coos_county_democrat": {
                    "name": "Coös County Democrat",
                    "url": "https://www.cooscountydemocrat.com",
                    "rss": "https://www.cooscountydemocrat.com/feed",
                    "area": "Coös County",
                    "description": "Local newspaper covering Coös County including Colebrook"
                },
                "berlin_daily_sun": {
                    "name": "Berlin Daily Sun",
                    "url": "https://www.berlindailysun.com",
                    "rss": "https://www.berlindailysun.com/feed",
                    "area": "Berlin, Coös County",
                    "description": "Daily newspaper serving Berlin and surrounding areas"
                },
                "lancaster_news": {
                    "name": "Lancaster News",
                    "url": "https://www.lancasternews.com",
                    "rss": "https://www.lancasternews.com/feed",
                    "area": "Lancaster, Coös County",
                    "description": "Local news for Lancaster and northern Coös County"
                }
            },
            "regional_sources": {
                "nh_union_leader": {
                    "name": "New Hampshire Union Leader",
                    "url": "https://www.unionleader.com",
                    "rss": "https://www.unionleader.com/rss",
                    "area": "New Hampshire",
                    "description": "State's largest daily newspaper"
                },
                "concord_monitor": {
                    "name": "Concord Monitor",
                    "url": "https://www.concordmonitor.com",
                    "rss": "https://www.concordmonitor.com/rss",
                    "area": "Concord, NH",
                    "description": "Capital region news and state politics"
                }
            },
            "hunting_outdoors": {
                "nh_fish_game": {
                    "name": "NH Fish & Game News",
                    "url": "https://www.wildlife.state.nh.us",
                    "rss": "https://www.wildlife.state.nh.us/news/rss.xml",
                    "area": "New Hampshire",
                    "description": "Official hunting and fishing news from NH Fish & Game"
                },
                "outdoor_life": {
                    "name": "Outdoor Life",
                    "url": "https://www.outdoorlife.com",
                    "rss": "https://www.outdoorlife.com/feed",
                    "area": "National",
                    "description": "Hunting and outdoor recreation news"
                }
            }
        }
    
    def get_local_news(self, source_type: str = "all", limit: int = 10) -> Dict:
        """Get local news from specified sources"""
        try:
            cache_key = f"local_news_{source_type}_{limit}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            news_items = []
            
            if source_type == "all" or source_type == "local":
                news_items.extend(self._fetch_rss_news("local_newspapers", limit))
            
            if source_type == "all" or source_type == "regional":
                news_items.extend(self._fetch_rss_news("regional_sources", limit))
            
            if source_type == "all" or source_type == "hunting":
                news_items.extend(self._fetch_rss_news("hunting_outdoors", limit))
            
            # Sort by date and limit results
            news_items.sort(key=lambda x: x.get('published', ''), reverse=True)
            news_items = news_items[:limit]
            
            result = {
                "source_type": source_type,
                "total_items": len(news_items),
                "last_updated": datetime.now().isoformat(),
                "news_items": news_items
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = time.time()
            
            return result
            
        except Exception as e:
            return {
                "error": f"Failed to fetch local news: {str(e)}",
                "source_type": source_type,
                "total_items": 0,
                "news_items": []
            }
    
    def _fetch_rss_news(self, source_category: str, limit: int) -> List[Dict]:
        """Fetch news from RSS feeds"""
        news_items = []
        sources = self.news_sources.get(source_category, {})
        
        for source_id, source_info in sources.items():
            try:
                if source_info.get('rss'):
                    feed = feedparser.parse(source_info['rss'])
                    
                    for entry in feed.entries[:limit]:
                        # Filter for relevant content
                        if self._is_relevant_content(entry, source_category):
                            news_item = {
                                "title": entry.get('title', 'No title'),
                                "summary": entry.get('summary', 'No summary available'),
                                "link": entry.get('link', ''),
                                "published": entry.get('published', ''),
                                "source": source_info['name'],
                                "source_url": source_info['url'],
                                "area": source_info['area'],
                                "category": source_category,
                                "relevance_score": self._calculate_relevance_score(entry, source_category)
                            }
                            news_items.append(news_item)
                            
            except Exception as e:
                print(f"Error fetching RSS from {source_info['name']}: {e}")
                continue
        
        return news_items
    
    def _is_relevant_content(self, entry: Dict, source_category: str) -> bool:
        """Check if content is relevant to hunting/outdoors/local news"""
        title = entry.get('title', '').lower()
        summary = entry.get('summary', '').lower()
        
        # Keywords for relevant content
        hunting_keywords = [
            'hunting', 'deer', 'moose', 'bear', 'turkey', 'fishing', 'outdoor',
            'wildlife', 'game', 'season', 'license', 'permit', 'forest', 'woods'
        ]
        
        local_keywords = [
            'colebrook', 'coos county', 'berlin', 'lancaster', 'pittsburg',
            'dixville notch', 'connecticut lakes', 'new hampshire', 'nh'
        ]
        
        # Check for hunting/outdoor relevance
        if source_category == "hunting_outdoors":
            return any(keyword in title or keyword in summary for keyword in hunting_keywords)
        
        # Check for local relevance
        if source_category in ["local_newspapers", "regional_sources"]:
            return any(keyword in title or keyword in summary for keyword in local_keywords + hunting_keywords)
        
        return True  # Include all content if no specific filtering
    
    def _calculate_relevance_score(self, entry: Dict, source_category: str) -> float:
        """Calculate relevance score for news item"""
        title = entry.get('title', '').lower()
        summary = entry.get('summary', '').lower()
        
        score = 0.5  # Base score
        
        # Hunting/outdoor keywords
        hunting_keywords = [
            'hunting', 'deer', 'moose', 'bear', 'turkey', 'fishing', 'outdoor',
            'wildlife', 'game', 'season', 'license', 'permit', 'forest', 'woods'
        ]
        
        # Local keywords
        local_keywords = [
            'colebrook', 'coos county', 'berlin', 'lancaster', 'pittsburg',
            'dixville notch', 'connecticut lakes', 'new hampshire', 'nh'
        ]
        
        # Increase score for hunting keywords
        for keyword in hunting_keywords:
            if keyword in title:
                score += 0.1
            if keyword in summary:
                score += 0.05
        
        # Increase score for local keywords
        for keyword in local_keywords:
            if keyword in title:
                score += 0.15
            if keyword in summary:
                score += 0.1
        
        return min(score, 1.0)
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        timestamp_key = cache_key + "_timestamp"
        if cache_key in self.cache and timestamp_key in self.cache:
            return (time.time() - self.cache[timestamp_key]) < self.cache_duration
        return False
    
    def get_hunting_news(self, limit: int = 5) -> Dict:
        """Get hunting and outdoor specific news"""
        return self.get_local_news("hunting", limit)
    
    def get_colebrook_news(self, limit: int = 5) -> Dict:
        """Get news specifically relevant to Colebrook area"""
        try:
            cache_key = f"colebrook_news_{limit}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            # Get all news and filter for Colebrook relevance
            all_news = self.get_local_news("all", limit * 2)
            colebrook_news = []
            
            for item in all_news.get('news_items', []):
                if self._is_colebrook_relevant(item):
                    colebrook_news.append(item)
                    if len(colebrook_news) >= limit:
                        break
            
            result = {
                "source_type": "colebrook",
                "total_items": len(colebrook_news),
                "last_updated": datetime.now().isoformat(),
                "news_items": colebrook_news
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = time.time()
            
            return result
            
        except Exception as e:
            return {
                "error": f"Failed to fetch Colebrook news: {str(e)}",
                "source_type": "colebrook",
                "total_items": 0,
                "news_items": []
            }
    
    def _is_colebrook_relevant(self, news_item: Dict) -> bool:
        """Check if news item is relevant to Colebrook area"""
        title = news_item.get('title', '').lower()
        summary = news_item.get('summary', '').lower()
        area = news_item.get('area', '').lower()
        
        colebrook_keywords = [
            'colebrook', 'coos county', 'berlin', 'lancaster', 'pittsburg',
            'dixville notch', 'connecticut lakes', 'wmu a', 'wmu b', 'wmu c'
        ]
        
        return any(keyword in title or keyword in summary or keyword in area 
                  for keyword in colebrook_keywords)
    
    def get_news_sources(self) -> Dict:
        """Get available news sources"""
        return {
            "sources": self.news_sources,
            "total_sources": sum(len(category) for category in self.news_sources.values()),
            "categories": list(self.news_sources.keys())
        }
    
    def search_news(self, query: str, limit: int = 10) -> Dict:
        """Search news items by query"""
        try:
            cache_key = f"search_{query}_{limit}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            # Get all news and filter by query
            all_news = self.get_local_news("all", limit * 2)
            matching_news = []
            
            query_lower = query.lower()
            
            for item in all_news.get('news_items', []):
                title = item.get('title', '').lower()
                summary = item.get('summary', '').lower()
                
                if query_lower in title or query_lower in summary:
                    matching_news.append(item)
                    if len(matching_news) >= limit:
                        break
            
            result = {
                "query": query,
                "total_items": len(matching_news),
                "last_updated": datetime.now().isoformat(),
                "news_items": matching_news
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = time.time()
            
            return result
            
        except Exception as e:
            return {
                "error": f"Failed to search news: {str(e)}",
                "query": query,
                "total_items": 0,
                "news_items": []
            }

# Global instance
local_news_service = LocalNewsService()
