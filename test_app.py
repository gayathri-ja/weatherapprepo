import unittest
import app

class TestWeatherApp(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_get_weather_data_valid_city(self):
        # Test if the function returns data for a valid city
        city_name = 'London'
        result = app.get_weather_data(city_name)
        self.assertIsNotNone(result)
        self.assertIn('name', result)
        self.assertEqual(result['name'], city_name)

    def test_get_weather_data_invalid_city(self):
        # Test if the function returns None for an invalid city
        city_name = 'InvalidCityName'
        result = app.get_weather_data(city_name)
        self.assertIsNone(result)

    def test_weather_app_valid_city(self):
        # Test if the route works correctly for a valid city
        city_name = 'London'
        response = self.client.post('/', data={'city': city_name})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather Information for', response.data)

    def test_weather_app_invalid_city(self):
        # Test if the route handles an invalid city gracefully
        city_name = 'InvalidCityName'
        response = self.client.post('/', data={'city': city_name})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'City not found or API request failed. Please try again.', response.data)

    def test_weather_app_empty_city(self):
        # Test if the route handles an empty city name gracefully
        response = self.client.post('/', data={'city': ''})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'City not found or API request failed. Please try again.', response.data)

if __name__ == '__main__':
    unittest.main()
