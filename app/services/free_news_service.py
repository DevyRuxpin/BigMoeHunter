#!/usr/bin/env python3
"""
Free News Service for BigMoeHunter
Only displays articles that can be viewed for free
"""

import requests
import json
import feedparser
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time

class FreeNewsService:
    """Service for free news articles only"""
    
    def __init__(self):
        self.news_sources = self._initialize_free_news_sources()
        self.cache = {}
        self.cache_duration = 3600  # 1 hour cache
    
    def _initialize_free_news_sources(self) -> Dict:
        """Initialize only free news sources"""
        return {
            "free_sources": {
                "nh_fish_game": {
                    "name": "NH Fish & Game News",
                    "url": "https://www.wildlife.state.nh.us",
                    "rss": "https://www.wildlife.state.nh.us/news/rss.xml",
                    "area": "New Hampshire",
                    "description": "Official hunting and fishing news from NH Fish & Game",
                    "free": True
                },
                "outdoor_life": {
                    "name": "Outdoor Life",
                    "url": "https://www.outdoorlife.com",
                    "rss": "https://www.outdoorlife.com/feed",
                    "area": "National",
                    "description": "Hunting and outdoor recreation news",
                    "free": True
                },
                "field_stream": {
                    "name": "Field & Stream",
                    "url": "https://www.fieldandstream.com",
                    "rss": "https://www.fieldandstream.com/feed",
                    "area": "National",
                    "description": "Hunting and fishing news",
                    "free": True
                },
                "realtree": {
                    "name": "Realtree",
                    "url": "https://www.realtree.com",
                    "rss": "https://www.realtree.com/feed",
                    "area": "National",
                    "description": "Hunting tips and news",
                    "free": True
                }
            },
            "local_free_sources": {
                "colebrook_news": {
                    "name": "Colebrook Area News",
                    "url": "https://www.colebrooknews.com",
                    "rss": "https://www.colebrooknews.com/feed",
                    "area": "Colebrook, NH",
                    "description": "Local news for Colebrook area",
                    "free": True
                },
                "nh_public_radio": {
                    "name": "NH Public Radio",
                    "url": "https://www.nhpr.org",
                    "rss": "https://www.nhpr.org/rss.xml",
                    "area": "New Hampshire",
                    "description": "Public radio news for New Hampshire",
                    "free": True
                }
            }
        }
    
    def get_free_news(self, source_type: str = "all", limit: int = 10) -> Dict:
        """Get free news articles only"""
        try:
            cache_key = f"free_news_{source_type}_{limit}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            news_items = []
            
            if source_type == "all" or source_type == "hunting":
                news_items.extend(self._fetch_free_rss_news("free_sources", limit))
            
            if source_type == "all" or source_type == "local":
                news_items.extend(self._fetch_free_rss_news("local_free_sources", limit))
            
            # Sort by date and limit results
            news_items.sort(key=lambda x: x.get('published', ''), reverse=True)
            news_items = news_items[:limit]
            
            result = {
                "source_type": source_type,
                "total_items": len(news_items),
                "last_updated": datetime.now().isoformat(),
                "news_items": news_items,
                "note": "All articles are free to view"
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = time.time()
            
            return result
            
        except Exception as e:
            return {
                "error": f"Failed to fetch free news: {str(e)}",
                "source_type": source_type,
                "total_items": 0,
                "news_items": []
            }
    
    def _fetch_free_rss_news(self, source_category: str, limit: int) -> List[Dict]:
        """Fetch news from free RSS feeds only"""
        news_items = []
        sources = self.news_sources.get(source_category, {})
        
        for source_id, source_info in sources.items():
            try:
                if source_info.get('rss') and source_info.get('free', False):
                    feed = feedparser.parse(source_info['rss'])
                    
                    for entry in feed.entries[:limit]:
                        # Filter for relevant content
                        if self._is_relevant_content(entry, source_category):
                            news_item = {
                                "title": entry.get('title', 'No title'),
                                "summary": self._clean_summary(entry.get('summary', 'No summary available')),
                                "link": entry.get('link', ''),
                                "published": entry.get('published', ''),
                                "source": source_info['name'],
                                "source_url": source_info['url'],
                                "area": source_info['area'],
                                "category": source_category,
                                "relevance_score": self._calculate_relevance_score(entry, source_category),
                                "free_access": True
                            }
                            news_items.append(news_item)
                            
            except Exception as e:
                print(f"Error fetching RSS from {source_info['name']}: {e}")
                continue
        
        return news_items
    
    def _clean_summary(self, summary: str) -> str:
        """Clean HTML from summary and limit length"""
        import re
        # Remove HTML tags
        clean_summary = re.sub(r'<[^>]+>', '', summary)
        # Remove extra whitespace
        clean_summary = ' '.join(clean_summary.split())
        # Limit length
        if len(clean_summary) > 200:
            clean_summary = clean_summary[:200] + "..."
        return clean_summary
    
    def _is_relevant_content(self, entry: Dict, source_category: str) -> bool:
        """Check if content is relevant to hunting/outdoors/local news"""
        title = entry.get('title', '').lower()
        summary = entry.get('summary', '').lower()
        
        # Keywords for relevant content
        hunting_keywords = [
            'hunting', 'deer', 'moose', 'bear', 'turkey', 'fishing', 'outdoor',
            'wildlife', 'game', 'season', 'license', 'permit', 'forest', 'woods',
            'rifle', 'shotgun', 'bow', 'archery', 'muzzleloader'
        ]
        
        local_keywords = [
            'colebrook', 'coos county', 'berlin', 'lancaster', 'pittsburg',
            'dixville notch', 'connecticut lakes', 'new hampshire', 'nh'
        ]
        
        # Check for hunting/outdoor relevance
        if source_category == "free_sources":
            return any(keyword in title or keyword in summary for keyword in hunting_keywords)
        
        # Check for local relevance
        if source_category == "local_free_sources":
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
        """Get hunting and outdoor specific free news"""
        return self.get_free_news("hunting", limit)
    
    def get_local_news(self, limit: int = 5) -> Dict:
        """Get local free news"""
        return self.get_free_news("local", limit)
    
    def search_free_news(self, query: str, limit: int = 10) -> Dict:
        """Search free news items by query"""
        try:
            cache_key = f"search_{query}_{limit}"
            if self._is_cache_valid(cache_key):
                return self.cache[cache_key]
            
            # Get all free news and filter by query
            all_news = self.get_free_news("all", limit * 2)
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
                "news_items": matching_news,
                "note": "All articles are free to view"
            }
            
            # Cache the result
            self.cache[cache_key] = result
            self.cache[cache_key + "_timestamp"] = time.time()
            
            return result
            
        except Exception as e:
            return {
                "error": f"Failed to search free news: {str(e)}",
                "query": query,
                "total_items": 0,
                "news_items": []
            }
    
    def get_news_sources(self) -> Dict:
        """Get available free news sources"""
        return {
            "sources": self.news_sources,
            "total_sources": sum(len(category) for category in self.news_sources.values()),
            "categories": list(self.news_sources.keys()),
            "note": "All sources provide free access to articles"
        }
    
    def get_sports_news(self, keywords: List[str], limit: int = 5) -> Dict:
        """Get sports news filtered by keywords"""
        try:
            # Use working sports sources with verified RSS feeds
            sports_sources = {
                "espn": {
                    "name": "ESPN",
                    "url": "https://www.espn.com",
                    "rss": "https://www.espn.com/espn/rss/news",
                    "area": "National",
                    "description": "Sports news and updates",
                    "free": True
                },
                "cbs_sports": {
                    "name": "CBS Sports",
                    "url": "https://www.cbssports.com",
                    "rss": "https://www.cbssports.com/rss/headlines/",
                    "area": "National",
                    "description": "Sports headlines and news",
                    "free": True
                },
                "red_sox": {
                    "name": "Boston Red Sox",
                    "url": "https://www.mlb.com/redsox",
                    "rss": "https://www.mlb.com/redsox/feeds/news/rss.xml",
                    "area": "Boston",
                    "description": "Red Sox news and updates",
                    "free": True
                },
                "outdoor_life": {
                    "name": "Outdoor Life",
                    "url": "https://www.outdoorlife.com",
                    "rss": "https://www.outdoorlife.com/feed",
                    "area": "National",
                    "description": "Hunting and outdoor recreation news",
                    "free": True
                }
            }
            
            news_items = []
            
            for source_key, source_info in sports_sources.items():
                try:
                    feed = feedparser.parse(source_info["rss"])
                    
                    for entry in feed.entries[:limit]:
                        # Check if article contains sports keywords
                        title_lower = entry.title.lower()
                        summary_lower = getattr(entry, 'summary', '').lower()
                        
                        if any(keyword.lower() in title_lower or keyword.lower() in summary_lower for keyword in keywords):
                            news_item = {
                                "title": entry.title,
                                "link": entry.link,
                                "source": source_info["name"],
                                "source_url": source_info["url"],
                                "published": entry.get("published", datetime.now().isoformat()),
                                "summary": getattr(entry, 'summary', entry.title)[:300],
                                "area": source_info["area"],
                                "category": "sports",
                                "free_access": True,
                                "relevance_score": 0.8
                            }
                            news_items.append(news_item)
                            
                            if len(news_items) >= limit:
                                break
                                
                except Exception as e:
                    print(f"Error fetching from {source_key}: {e}")
                    continue
                    
                if len(news_items) >= limit:
                    break
            
            return {
                "news_items": news_items[:limit],
                "total_items": len(news_items),
                "keywords": keywords,
                "last_updated": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Error in get_sports_news: {e}")
            return {
                "news_items": [],
                "total_items": 0,
                "keywords": keywords,
                "error": str(e),
                "last_updated": datetime.now().isoformat()
            }

# Global instance
free_news_service = FreeNewsService()
