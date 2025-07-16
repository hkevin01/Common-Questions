"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

import unittest
from unittest.mock import Mock, patch
import requests

class WeatherService:
    def get_temperature(self, city):
        response = requests.get(f"http://api.weather.com/{city}")
        return response.json()['temperature']

class TestWeatherService(unittest.TestCase):
    @patch('requests.get')
    def test_get_temperature(self, mock_get):
        # Arrange
        mock_response = Mock()
        mock_response.json.return_value = {'temperature': 25}
        mock_get.return_value = mock_response
        
        service = WeatherService()
        
        # Act
        temperature = service.get_temperature('London')
        
        # Assert
        self.assertEqual(temperature, 25)
        mock_get.assert_called_once_with("http://api.weather.com/London")

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
